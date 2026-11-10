# NYC Parking & Camera Violation Analyzer

CPS 3440 — Analysis of Algorithms, Fall 2026.

This Python project compares linear search, binary search, and hash-table lookup for finding a summons number in NYC's public Open Parking and Camera Violations dataset.

## Dataset
- Provider: NYC Department of Finance / NYC Open Data
- Dataset ID: nc67-uf89
- Official page: https://data.cityofnewyork.us/City-Government/Open-Parking-and-Camera-Violations/nc67-uf89/about_data
- API: https://data.cityofnewyork.us/resource/nc67-uf89.csv
- Fields: summons_number, issue_date, violation, fine_amount, amount_due, state, precinct.
- Download a manageable sample; do not commit the huge full dataset. A missing record in your sample may still exist in the full dataset.

## Algorithms
1. Linear search: worst O(n), extra space O(1).
2. Binary search: worst O(log n), iterative extra space O(1); input must be sorted.
3. Hash table: average O(1), worst O(n); building the index takes expected O(n) time and O(n) space.

Report sorting and hash-index construction separately from lookup time.

## Setup
Python 3.10+; no third-party packages required.

Download up to 10,000 records:
```bash
python -c "from src.data_loader import download_sample; download_sample(10000)"
```
Search for a summons number from the CSV:
```bash
python -m src.main --summons YOUR_SUMMONS_NUMBER
```
Run tests:
```bash
python -m unittest discover -s tests -v
```
Run benchmark:
```bash
python -m benchmarks.run_benchmarks
```
Benchmark results are saved to results/benchmark_results.csv. Repeat with 1,000, 10,000, and 100,000 rows and report only actual measurements.

## GitHub Pages
In repository Settings > Pages, select GitHub Actions. The workflow deploys after pushes to main.
Website: https://tonylopes103-afk.github.io/parking-camera-violation-analyzer/

## Academic note
Understand and test all code, and follow your instructor's AI policy. The technical paper, actual experiments, charts, CLO A-D reflections, and presentation still need to be completed and explained by you.