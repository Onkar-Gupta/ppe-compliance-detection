# X05: accuracy + cross-dataset axes (frozen TEST splits)

Per-run numbers, scored on the held-out test partitions that no training run has
read. **Not results yet:** nothing here is a finding until seeds are aggregated with
a 95 % BCa CI and the named test. No 'X beats Y' from this table.

| run | trained on | seed | in-domain mAP50 | cross mAP50 | delta | in mAP50-95 | cross mAP50-95 |
|---|---|---|---|---|---|---|---|
| X04-y8n-s2-chv | chv | 2 | 0.9009 | 0.5341 | -0.3668 | 0.5071 | 0.3043 |

## Per-class mAP50, in-domain (vest support is thin: F1)

| run | person | helmet | vest |
|---|---|---|---|
| X04-y8n-s2-chv | 0.8942 | 0.9111 | 0.8974 |
