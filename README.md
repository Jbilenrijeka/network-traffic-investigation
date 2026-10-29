# Network Event Investigation

## Objective
Practice triaging a small dataset of DNS and connection metadata without handling live traffic.

## Run
```bash
python analyze_network_events.py data/network_events.csv
```

## What the script does
Summarizes DNS query frequency and flags domains that appear on the explicitly fictional training watchlist. The watchlist is not real threat intelligence.
