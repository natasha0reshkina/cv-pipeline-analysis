from pathlib import Path

def list_images(input_dir: str, limit: int | None = None) -> list[str]:
    p = Path(input_dir)
    exts = {".jpg", ".jpeg", ".png"}
    files = [str(x) for x in sorted(p.rglob("*")) if x.suffix.lower() in exts]
    if limit is not None:
        files = files[:limit]
    return files
