# Results files

These are the small output files behind every number in the main README. They were copied unchanged from the machine that ran the experiments (the only edits are punctuation in the generated `.md` summaries, where an older version of the report code used dashes). No dataset images and no model weights are included.

| Folder | What it holds | Produced by |
|---|---|---|
| `X05-accuracy/` | In-domain and cross-dataset mAP50 and mAP50-95 for all 18 runs, scored on the frozen **test** splits. **This is the table the reported accuracy comes from.** | `python -m src.score` |
| `X05-violation/` | Violation recall per run, zero-shot on Pictor-PPE, plus the summary | `python -m src.violation` |
| `X05-efficiency/` | Latency, throughput and model size | `python -m src.efficiency` |
| `X05-stats/` | Seed aggregation (mean with 95 % BCa interval) and the significance tests | `python -m src.stats` |
| `X05-figures/` | The six figures, PNG and PDF | `python -m src.figures` |
| `X04-runs/` | `summary.json` and `results.csv` for each of the 18 training runs | `python -m src.run` |
| `X03-timing/` | Epoch times before and after the offline pre-resize fix (the I/O bottleneck). Mean epoch time: 244.8 s over 42 epochs before, 45.0 s over 3 epochs after, about 5.4 times faster. One pilot run each, so a rough figure. | `python -m src.run` |
| `X01-associate/` | Calibration of the person-to-PPE association threshold, with its charts | `python -m src.associate` |
| `X01-harmonise/` | The label-harmonisation report | `python -m src.harmonise` |
| `S7-repro-clean/` | A clean-checkout reproduction of the accuracy table | `python -m src.score` |

## Read this before comparing numbers

The per-run `summary.json` files in `X04-runs/` were written at the end of each training run and score the **validation** split. The numbers in `X05-accuracy/` score the **test** split, which no training run read. They differ, and the test-split numbers are the ones to quote. For example, run `X04-y8n-s2-chv` has an in-domain mAP50 of 0.8954 in its `summary.json` (validation) and 0.9009 in `X05-accuracy` (test).

The run IDs (`X04-y8n-s2-chv`) follow `X##-<model>-<seed>-<training dataset>`. `y8n`, `y11n` and `y26n` are YOLOv8n, YOLO11n and YOLO26n; `chv` and `sh17` are the dataset the run trained on.

The weights are not distributed, so the files here cannot be regenerated without retraining. The code and frozen configs are in the repo.
