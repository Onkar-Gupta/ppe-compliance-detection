# X05: violation-recall axis (zero-shot, Pictor-PPE)

Per-run numbers only. **Nothing here is a result until S5 aggregates it across seeds
with a 95 % BCa CI and the named test**; no 'X beats Y' from this table.

Helmet is the headline. Vest is shown beside its always-flag trivial baseline and its
support count, because only 1.6 % of the available workers wear one.

| run | helmet recall | helmet prec | helmet F1 | vest recall | vest trivial prec | vest support | person det. |
|---|---|---|---|---|---|---|---|
| X04-y8n-s1-sh17 | 0.7300 | 0.4811 | 0.5800 | 0.6954 | 0.9836 | 2456 | 0.713 |
| X04-y8n-s0-sh17 | 0.7277 | 0.4683 | 0.5699 | 0.7081 | 0.9836 | 2456 | 0.723 |
| X04-y11n-s0-sh17 | 0.7254 | 0.4648 | 0.5666 | 0.7166 | 0.9836 | 2456 | 0.730 |
| X04-y8n-s2-sh17 | 0.7231 | 0.4832 | 0.5793 | 0.6971 | 0.9836 | 2456 | 0.715 |
| X04-y11n-s1-sh17 | 0.7185 | 0.4801 | 0.5756 | 0.7003 | 0.9836 | 2456 | 0.719 |
| X04-y11n-s2-sh17 | 0.7082 | 0.4806 | 0.5726 | 0.6930 | 0.9836 | 2456 | 0.714 |
| X04-y26n-s0-sh17 | 0.6934 | 0.4848 | 0.5706 | 0.6694 | 0.9836 | 2456 | 0.675 |
| X04-y26n-s1-sh17 | 0.6922 | 0.4749 | 0.5633 | 0.6621 | 0.9836 | 2456 | 0.676 |
| X04-y26n-s2-sh17 | 0.6865 | 0.5025 | 0.5803 | 0.6543 | 0.9836 | 2456 | 0.670 |
| X04-y8n-s2-chv | 0.5515 | 0.6309 | 0.5885 | 0.6592 | 0.9836 | 2456 | 0.676 |
| X04-y26n-s2-chv | 0.5400 | 0.7119 | 0.6142 | 0.5998 | 0.9836 | 2456 | 0.610 |
| X04-y11n-s1-chv | 0.5366 | 0.6364 | 0.5822 | 0.6397 | 0.9836 | 2456 | 0.654 |
| X04-y26n-s1-chv | 0.5343 | 0.6818 | 0.5991 | 0.6364 | 0.9836 | 2456 | 0.646 |
| X04-y26n-s0-chv | 0.5332 | 0.6976 | 0.6044 | 0.6079 | 0.9836 | 2456 | 0.618 |
| X04-y11n-s2-chv | 0.5160 | 0.6299 | 0.5673 | 0.6417 | 0.9836 | 2456 | 0.660 |
| X04-y8n-s0-chv | 0.4977 | 0.6435 | 0.5613 | 0.6356 | 0.9836 | 2456 | 0.655 |
| X04-y11n-s0-chv | 0.4691 | 0.6529 | 0.5459 | 0.5680 | 0.9836 | 2456 | 0.592 |
| X04-y8n-s1-chv | 0.4634 | 0.6289 | 0.5336 | 0.6120 | 0.9836 | 2456 | 0.631 |

Settings: confidence 0.25, person match IoU 0.5, association threshold calibrated on SH17/CHV train splits only.
Scored on 774 images / 2497 labelled workers (whole crowd-sourced release; Pictor was never trained on).

An undetected worker counts as a violation missed, not as an absent sample; see
`violations_missed_because_person_undetected` in each run's JSON.
