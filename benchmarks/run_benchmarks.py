"""Run repeatable lookup timing and save actual measured results."""
import csv
import statistics
import time
from pathlib import Path
from src.data_loader import load_records
from src.algorithms import linear_search, binary_search, build_hash_index, hash_search

def median_time(function, repeats=7):
    samples = []
    for _ in range(repeats):
        start = time.perf_counter()
        function()
        samples.append(time.perf_counter() - start)
    return statistics.median(samples)

def main():
    records = load_records()
    if not records:
        raise SystemExit("No records found. Download data first.")
    sorted_records = sorted(records, key=lambda row: str(row.get("summons_number", "")))
    start = time.perf_counter()
    index = build_hash_index(records)
    hash_build = time.perf_counter() - start
    target = str(records[-1].get("summons_number", ""))
    linear = median_time(lambda: linear_search(records, target))
    binary = median_time(lambda: binary_search(sorted_records, target))
    hashed = median_time(lambda: hash_search(index, target))
    output = Path("results/benchmark_results.csv")
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["records","target","linear_seconds","binary_seconds","hash_seconds","hash_build_seconds","trials"])
        writer.writerow([len(records),target,f"{linear:.10f}",f"{binary:.10f}",f"{hashed:.10f}",f"{hash_build:.10f}",7])
    print("Median lookup seconds (7 trials):", linear, binary, hashed)
    print("Hash index build seconds:", hash_build)
    print("Saved:", output)

if __name__ == "__main__":
    main()
