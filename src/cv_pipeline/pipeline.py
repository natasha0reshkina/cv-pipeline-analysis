from pathlib import Path
from PIL import Image
import numpy as np
import time

def run_pipeline(image_path: str, input_size: int = 640) -> dict:
    t0 = time.perf_counter()
    img = Image.open(image_path).convert("RGB")
    t1 = time.perf_counter()

    img = img.resize((input_size, input_size))
    arr = np.asarray(img, dtype=np.float32) / 255.0
    t2 = time.perf_counter()

    _ = arr.mean()
    t3 = time.perf_counter()

    result = {"score": float(arr.mean())}
    t4 = time.perf_counter()

    return {
        "image_path": str(Path(image_path)),
        "input_size": input_size,
        "load_ms": (t1 - t0) * 1000.0,
        "preprocess_ms": (t2 - t1) * 1000.0,
        "inference_ms": (t3 - t2) * 1000.0,
        "postprocess_ms": (t4 - t3) * 1000.0,
        "total_ms": (t4 - t0) * 1000.0,
        "result": result,
    }
