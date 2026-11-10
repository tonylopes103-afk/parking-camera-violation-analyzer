# Experimental Results — Fill In After Running the Program

This file is a worksheet for recording actual evidence. It intentionally contains no invented results.

## 1. Environment

- Date of experiment: [date]
- Computer / processor: [details]
- Installed RAM: [details]
- Operating system: [version]
- Python version: [run `python --version`]
- Dataset download date: [date]
- Dataset source: https://data.cityofnewyork.us/City-Government/Open-Parking-and-Camera-Violations/nc67-uf89/about_data

## 2. Actual input sizes

| Requested sample | Actual rows downloaded | Earliest issue date | Latest issue date | Blank summons keys |
|---:|---:|---|---|---:|
| 1,000 | [fill] | [fill] | [fill] | [fill] |
| 10,000 | [fill] | [fill] | [fill] | [fill] |
| 100,000 | [fill] | [fill] | [fill] | [fill] |

## 3. Timing results

Use median time from repeated trials. Keep sorting and index construction separate from lookup.

| Actual n | Linear lookup (s) | Binary lookup (s) | Hash lookup (s) | Sort time (s) | Hash build (s) |
|---:|---:|---:|---:|---:|---:|
| [n] | [fill] | [fill] | [fill] | [fill] | [fill] |
| [n] | [fill] | [fill] | [fill] | [fill] | [fill] |
| [n] | [fill] | [fill] | [fill] | [fill] | [fill] |

## 4. Interpretation

Answer using your measured results:

1. Which method had the fastest lookup for each input size?
2. Did the result change as n increased?
3. Did sorting or building the dictionary change which method was best for a single search?
4. Which method would you choose if the same data had to be searched 100 or 1,000 times?
5. Did your measurements follow the expected O(n), O(log n), and average O(1) lookup trends?
6. What could explain differences between theory and observed runtime?

## 5. Reproducibility commands

Download sample data (change the requested size for each experiment):

```bash
python -c "from src.data_loader import download_sample; download_sample(1000)"
python -m benchmarks.run_benchmarks
```

Repeat with 10,000 and 100,000. Save each CSV output before downloading the next sample so earlier results are not overwritten. For example, copy each output to a clearly named file such as `benchmark_1000.csv`, `benchmark_10000.csv`, and `benchmark_100000.csv`.

Run the unit tests:

```bash
python -m unittest discover -s tests -v
```

## 6. Chart requirements

Create a line chart with actual record count on the horizontal axis and median lookup time (seconds) on the vertical axis. Include one line per algorithm. If one line makes the others unreadable, use a second chart or a logarithmic vertical axis and label it clearly. Do not include made-up points.
