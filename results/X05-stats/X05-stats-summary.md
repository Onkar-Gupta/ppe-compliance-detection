# X05: seed aggregation + significance (the graduation gate)

Mean +/- 95 % BCa bootstrap CI over seeds, with paired sign-flip tests and
Friedman/Nemenyi across architectures. **CI-first:** the interval is the claim; the
tests support it. Numbers here are cleared to enter the dissertation.

> **Power warning.** Three seeds is the cited floor, not a comfortable sample. An
> exact paired sign-flip on n=3 cannot return p<0.25 however large the effect, so a
> null result at that n means *underpowered*, never *equivalent*. Each test states
> its own minimum attainable p.

## map50_in (accuracy, in-domain)

| group | mean | 95 % CI | width | n | method |
|---|---|---|---|---|---|
| y11n | trained on chv | 0.8933 | [0.8867, 0.8986] | 0.0118 | 3 | BCa (10000 draws) |
| y11n | trained on sh17 | 0.6713 | [0.6634, 0.6770] | 0.0136 | 3 | BCa (10000 draws) |
| y26n | trained on chv | 0.8813 | [0.8760, 0.8843] | 0.0083 | 3 | BCa (10000 draws) |
| y26n | trained on sh17 | 0.6646 | [0.6599, 0.6688] | 0.0088 | 3 | BCa (10000 draws) |
| y8n | trained on chv | 0.8921 | [0.8820, 0.8984] | 0.0164 | 3 | BCa (10000 draws) |
| y8n | trained on sh17 | 0.6663 | [0.6621, 0.6693] | 0.0071 | 3 | BCa (10000 draws) |

**Pooled across both training directions:**

| model | mean | 95 % CI | n |
|---|---|---|---|
| y11n | 0.7823 | [0.7044, 0.8600] | 6 |
| y26n | 0.7729 | [0.6979, 0.8477] | 6 |
| y8n | 0.7792 | [0.7014, 0.8582] | 6 |

**Pairwise (exact paired sign-flip):**

| comparison | mean diff | p | min attainable p | significant |
|---|---|---|---|---|
| y11n vs y26n | +0.0094 | 0.0312 | 0.0312 | yes |
| y11n vs y8n | +0.0031 | 0.2812 | 0.0312 | no |
| y26n vs y8n | -0.0063 | 0.0938 | 0.0312 | no |

**Friedman:** chi2 = 7.0000, p = 0.0302, 6 blocks; significant at 0.05.
Mean ranks: {'y11n': 1.333, 'y26n': 2.833, 'y8n': 1.833} · critical difference 1.353

## map50_cross (cross-dataset)

| group | mean | 95 % CI | width | n | method |
|---|---|---|---|---|---|
| y11n | trained on chv | 0.5066 | [0.4896, 0.5201] | 0.0305 | 3 | BCa (10000 draws) |
| y11n | trained on sh17 | 0.7844 | [0.7693, 0.7923] | 0.0231 | 3 | BCa (10000 draws) |
| y26n | trained on chv | 0.5236 | [0.5161, 0.5299] | 0.0138 | 3 | BCa (10000 draws) |
| y26n | trained on sh17 | 0.7593 | [0.7414, 0.7704] | 0.0290 | 3 | BCa (10000 draws) |
| y8n | trained on chv | 0.5241 | [0.5111, 0.5317] | 0.0206 | 3 | BCa (10000 draws) |
| y8n | trained on sh17 | 0.7915 | [0.7857, 0.7945] | 0.0088 | 3 | BCa (10000 draws) |

**Pooled across both training directions:**

| model | mean | 95 % CI | n |
|---|---|---|---|
| y11n | 0.6455 | [0.5447, 0.7445] | 6 |
| y26n | 0.6414 | [0.5574, 0.7258] | 6 |
| y8n | 0.6578 | [0.5633, 0.7496] | 6 |

**Pairwise (exact paired sign-flip):**

| comparison | mean diff | p | min attainable p | significant |
|---|---|---|---|---|
| y11n vs y26n | +0.0040 | 0.8125 | 0.0312 | no |
| y11n vs y8n | -0.0123 | 0.1875 | 0.0312 | no |
| y26n vs y8n | -0.0164 | 0.1250 | 0.0312 | no |

**Friedman:** chi2 = 1.3333, p = 0.5134, 6 blocks; not significant at 0.05.
Mean ranks: {'y11n': 2.0, 'y26n': 2.333, 'y8n': 1.667} · critical difference 1.353

## transfer_delta (in -> cross)

| group | mean | 95 % CI | width | n | method |
|---|---|---|---|---|---|
| y11n | trained on chv | -0.3867 | [-0.4026, -0.3713] | 0.0313 | 3 | BCa (10000 draws) |
| y11n | trained on sh17 | 0.1130 | [0.0991, 0.1233] | 0.0242 | 3 | BCa (10000 draws) |
| y26n | trained on chv | -0.3578 | [-0.3635, -0.3532] | 0.0103 | 3 | BCa (10000 draws) |
| y26n | trained on sh17 | 0.0948 | [0.0815, 0.1016] | 0.0201 | 3 | BCa (10000 draws) |
| y8n | trained on chv | -0.3680 | [-0.3709, -0.3665] | 0.0044 | 3 | BCa (10000 draws) |
| y8n | trained on sh17 | 0.1252 | [0.1196, 0.1294] | 0.0098 | 3 | BCa (10000 draws) |

**Pooled across both training directions:**

| model | mean | 95 % CI | n |
|---|---|---|---|
| y11n | -0.1368 | [-0.3130, 0.0386] | 6 |
| y26n | -0.1315 | [-0.2865, 0.0231] | 6 |
| y8n | -0.1214 | [-0.2871, 0.0456] | 6 |

**Pairwise (exact paired sign-flip):**

| comparison | mean diff | p | min attainable p | significant |
|---|---|---|---|---|
| y11n vs y26n | -0.0053 | 0.9062 | 0.0312 | no |
| y11n vs y8n | -0.0154 | 0.1562 | 0.0312 | no |
| y26n vs y8n | -0.0101 | 0.3125 | 0.0312 | no |

**Friedman:** chi2 = 0.3333, p = 0.8465, 6 blocks; not significant at 0.05.
Mean ranks: {'y11n': 2.167, 'y26n': 2.0, 'y8n': 1.833} · critical difference 1.353

## helmet_violation_recall

| group | mean | 95 % CI | width | n | method |
|---|---|---|---|---|---|
| y11n | trained on chv | 0.5072 | [0.4691, 0.5297] | 0.0606 | 3 | BCa (10000 draws) |
| y11n | trained on sh17 | 0.7174 | [0.7082, 0.7231] | 0.0149 | 3 | BCa (10000 draws) |
| y26n | trained on chv | 0.5358 | [0.5332, 0.5381] | 0.0049 | 3 | BCa (10000 draws) |
| y26n | trained on sh17 | 0.6907 | [0.6865, 0.6930] | 0.0065 | 3 | BCa (10000 draws) |
| y8n | trained on chv | 0.5042 | [0.4634, 0.5336] | 0.0702 | 3 | BCa (10000 draws) |
| y8n | trained on sh17 | 0.7269 | [0.7231, 0.7292] | 0.0061 | 3 | BCa (10000 draws) |

**Pooled across both training directions:**

| model | mean | 95 % CI | n |
|---|---|---|---|
| y11n | 0.6123 | [0.5263, 0.6888] | 6 |
| y26n | 0.6133 | [0.5601, 0.6663] | 6 |
| y8n | 0.6156 | [0.5193, 0.6979] | 6 |

**Pairwise (exact paired sign-flip):**

| comparison | mean diff | p | min attainable p | significant |
|---|---|---|---|---|
| y11n vs y26n | -0.0010 | 0.9688 | 0.0312 | no |
| y11n vs y8n | -0.0033 | 0.8438 | 0.0312 | no |
| y26n vs y8n | -0.0023 | 0.8438 | 0.0312 | no |

**Friedman:** chi2 = 2.3333, p = 0.3114, 6 blocks; not significant at 0.05.
Mean ranks: {'y11n': 2.167, 'y26n': 2.333, 'y8n': 1.5} · critical difference 1.353

## person_detection_rate

| group | mean | 95 % CI | width | n | method |
|---|---|---|---|---|---|
| y11n | trained on chv | 0.6354 | [0.5923, 0.6581] | 0.0658 | 3 | BCa (10000 draws) |
| y11n | trained on sh17 | 0.7209 | [0.7137, 0.7262] | 0.0125 | 3 | BCa (10000 draws) |
| y26n | trained on chv | 0.6247 | [0.6099, 0.6369] | 0.0270 | 3 | BCa (10000 draws) |
| y26n | trained on sh17 | 0.6736 | [0.6704, 0.6753] | 0.0049 | 3 | BCa (10000 draws) |
| y8n | trained on chv | 0.6540 | [0.6308, 0.6692] | 0.0384 | 3 | BCa (10000 draws) |
| y8n | trained on sh17 | 0.7169 | [0.7133, 0.7201] | 0.0068 | 3 | BCa (10000 draws) |

**Pooled across both training directions:**

| model | mean | 95 % CI | n |
|---|---|---|---|
| y11n | 0.6782 | [0.6341, 0.7109] | 6 |
| y26n | 0.6492 | [0.6247, 0.6687] | 6 |
| y8n | 0.6855 | [0.6537, 0.7092] | 6 |

**Pairwise (exact paired sign-flip):**

| comparison | mean diff | p | min attainable p | significant |
|---|---|---|---|---|
| y11n vs y26n | +0.0290 | 0.0938 | 0.0312 | no |
| y11n vs y8n | -0.0073 | 0.7188 | 0.0312 | no |
| y26n vs y8n | -0.0363 | 0.0625 | 0.0312 | no |

**Friedman:** chi2 = 4.0000, p = 0.1353, 6 blocks; not significant at 0.05.
Mean ranks: {'y11n': 1.667, 'y26n': 2.667, 'y8n': 1.667} · critical difference 1.353
