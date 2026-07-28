import subprocess
import sys
import platform


def detect_cuda_version() -> str:
    try:
        output = subprocess.check_output(["nvidia-smi", "--query-gpu=driver_version", "--format=csv,noheader"], text=True).strip()
        return output.split(".")[0]
    except Exception:
        return "11.8"


def install_ultralytics():
    subprocess.check_call(
        [sys.executable, "-m", "pip", "install", "--no-cache-dir", "ultralytics"],
    )


def install_detectron2():
    cuda_version = detect_cuda_version()
    torch_version = subprocess.check_output(
        [sys.executable, "-c", "import torch; print(torch.__version__)"],
        text=True,
    ).strip()
    major, minor = torch_version.split(".")[:2]
    wheel_url = f"https://dl.fbaipublicfiles.com/detectron2/wheels/cu{cuda_version}/torch{major}.{minor}/index.html"
    subprocess.check_call(
        [sys.executable, "-m", "pip", "install", "--no-cache-dir", f"detectron2", "-f", wheel_url],
    )


def install_pytorch():
    subprocess.check_call(
        [sys.executable, "-m", "pip", "install", "--no-cache-dir", "torch", "torchvision"],
    )


def install_all():
    install_pytorch()
    install_ultralytics()
    install_detectron2()


if __name__ == "__main__":
    install_all()