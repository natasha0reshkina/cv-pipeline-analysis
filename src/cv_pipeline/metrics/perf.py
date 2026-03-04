import time
import psutil

def measure_pipeline_run(fn, *args, **kwargs) -> dict:
    proc = psutil.Process()
    rss_before = proc.memory_info().rss
    t0 = time.perf_counter()
    out = fn(*args, **kwargs)
    t1 = time.perf_counter()
    rss_after = proc.memory_info().rss
    return {
        "total_ms": (t1 - t0) * 1000.0,
        "rss_mb_delta": (rss_after - rss_before) / (1024.0 * 1024.0),
        "output": out,
    }
