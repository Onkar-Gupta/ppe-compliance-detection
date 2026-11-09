# X05: efficiency axis (proxy; NOT edge hardware)

Measured on NVIDIA GeForce RTX 4070 Laptop GPU and Intel64 Family 6 Model 170 Stepping 4, GenuineIntel. Batch 1, imgsz 640, end-to-end (pre-process + inference + post-process), warm-up discarded, models interleaved.

**This is a proxy for deployment cost, not a measurement on an edge device.** No
embedded hardware was used; the comparison is relative and like-for-like.

## Architecture constants (identical across seeds by construction)

| architecture | params (M) | GFLOPs | weights (MB) |
|---|---|---|---|
| y11n | 2.590 | 6.44 | 5.46 |
| y26n | 2.505 | 5.78 | 5.38 |
| y8n | 3.011 | 8.20 | 6.24 |

## GPU latency (mean over runs of the same architecture)

| architecture | latency ms | FPS | measurement SD (ms) | n runs |
|---|---|---|---|---|
| y11n | 12.63 | 79.2 | 0.637 | 6 |
| y26n | 13.68 | 73.1 | 1.318 | 6 |
| y8n | 10.61 | 94.3 | 0.682 | 6 |

## CPU-constrained latency (mean over runs of the same architecture)

| architecture | latency ms | FPS | measurement SD (ms) | n runs |
|---|---|---|---|---|
| y11n | 51.46 | 19.4 | 0.556 | 1 |
| y26n | 68.06 | 14.7 | 5.984 | 1 |
| y8n | 49.82 | 20.1 | 4.825 | 1 |

The spread above is **measurement** noise across repeats of identical weights, not the
seed variance reported on the accuracy axis. The two must not be pooled.

⚠️ Sustained load throttles this laptop's GPU, so models were timed in randomised
interleaved order; a drift over the session cannot favour one architecture.
