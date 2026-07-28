import os
from typing import Optional


class MaskRCNNConfig:
    def __init__(
        self,
        weights: str = "COCO-Detection/faster_rcnn_X_101_32x8d_FPN_3x_coco",
        num_classes: int = 8,
        image_size: int = 640,
        batch_size: int = 2,
        learning_rate: float = 0.005,
        momentum: float = 0.9,
        weight_decay: float = 0.0001,
        lr_scheduler: str = "StepLR",
        lr_step_size: int = 3,
        lr_gamma: float = 0.1,
        max_iterations: int = 90000,
        print_freq: int = 20,
        output_dir: str = "runs/mask_rcnn",
    ):
        self.weights = weights
        self.num_classes = num_classes
        self.image_size = image_size
        self.batch_size = batch_size
        self.learning_rate = learning_rate
        self.momentum = momentum
        self.weight_decay = weight_decay
        self.lr_scheduler = lr_scheduler
        self.lr_step_size = lr_step_size
        self.lr_gamma = lr_gamma
        self.max_iterations = max_iterations
        self.print_freq = print_freq
        self.output_dir = output_dir


class MaskRCNNPipeline:
    def __init__(self, config: Optional[MaskRCNNConfig] = None):
        self.config = config or MaskRCNNConfig()
        self.model = None

    def build_model(self):
        try:
            from torchvision.models.detection import maskrcnn_resnet50_fpn_v2
            from torchvision.models.detection.mask_rcnn import MaskRCNN_ResNet50_FPN_V2_Weights

            weights = MaskRCNN_ResNet50_FPN_V2_Weights.DEFAULT
            self.model = maskrcnn_resnet50_fpn_v2(weights=weights)
            in_features = self.model.roi_heads.box_predictor.cls_score.in_features
            self.model.roi_heads.box_predictor = torch.nn.Linear(in_features, self.config.num_classes + 1)
            in_features_mask = self.model.roi_heads.mask_predictor.conv5_mask.in_channels
            self.model.roi_heads.mask_predictor = torch.nn.Conv2d(in_features_mask, self.config.num_classes + 1, kernel_size=1)
        except ImportError:
            raise ImportError("torchvision with Mask R-CNN support is required. Install: pip install torch torchvision")
        return self.model

    def train(self, train_loader, val_loader, num_epochs: int = 30):
        import torch
        if self.model is None:
            self.build_model()
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(device)
        optimizer = torch.optim.SGD(
            self.model.parameters(),
            lr=self.config.learning_rate,
            momentum=self.config.momentum,
            weight_decay=self.config.weight_decay,
        )
        scheduler = torch.optim.lr_scheduler.StepLR(optimizer, step_size=self.config.lr_step_size, gamma=self.config.lr_gamma)
        self.model.train()
        for epoch in range(num_epochs):
            for batch_idx, batch in enumerate(train_loader):
                images = list(img.to(device) for img in batch["images"])
                targets = [{k: v.to(device) for k, v in t.items()} for t in batch["targets"]]
                loss_dict = self.model(images, targets)
                losses = sum(loss for loss in loss_dict.values())
                optimizer.zero_grad()
                losses.backward()
                optimizer.step()
            scheduler.step()
            if epoch % self.config.print_freq == 0:
                print(f"Epoch {epoch}/{num_epochs}, Loss: {losses.item():.4f}")
        os.makedirs(self.config.output_dir, exist_ok=True)
        torch.save(self.model.state_dict(), os.path.join(self.config.output_dir, "model_final.pth"))

    def run_inference(self, image_path: str):
        import torch
        from PIL import Image
        from torchvision import transforms as T
        if self.model is None:
            self.build_model()
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(device)
        self.model.eval()
        img = Image.open(image_path).convert("RGB")
        transform = T.ToTensor()
        img_tensor = transform(img).unsqueeze(0).to(device)
        with torch.no_grad():
            predictions = self.model(img_tensor)
        return predictions[0]