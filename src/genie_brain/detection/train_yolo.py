from ultralytics import YOLO


def train_riverine_waste(
    model_path: str = "yolov8n.pt",
    data_yaml: str = "riverine_waste.yaml",
    epochs: int = 50,
    imgsz: int = 640,
    batch: int = 16,
    patience: int = 50,
    device: str = "0",
    project: str = "runs/detect",
    name: str = "riverine_waste",
    pretrained: bool = True,
):
    model = YOLO(model_path)

    if not pretrained:
        model = YOLO("yolov8n.yaml")
        model.train(
            data=data_yaml,
            epochs=epochs,
            imgsz=imgsz,
            batch=batch,
            patience=patience,
            device=device,
            project=project,
            name=name,
            pretrained=False,
        )
    else:
        model.train(
            data=data_yaml,
            epochs=epochs,
            imgsz=imgsz,
            batch=batch,
            patience=patience,
            device=device,
            project=project,
            name=name,
        )
    return model


def evaluate_yolo(model_path: str = "runs/detect/riverine_waste/weights/best.pt", data_yaml: str = "riverine_waste.yaml"):
    from ultralytics import YOLO
    model = YOLO(model_path)
    metrics = model.val(data=data_yaml, imgsz=640, batch=16)
    return {
        "box_ap50": metrics.box.ap50,
        "box_ap50_95": metrics.box.ap,
        "fitness": metrics.fitness,
    }


if __name__ == "__main__":
    model = train_riverine_waste()
    print("Training complete. Evaluating...")
    results = evaluate_yolo()
    print(f"Evaluation results: {results}")