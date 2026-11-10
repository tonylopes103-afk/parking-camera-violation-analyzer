"""Command-line application to search a downloaded NYC violation sample."""
import argparse
from src.data_loader import load_records, download_sample
from src.algorithms import linear_search, binary_search, build_hash_index, hash_search

def main():
    parser = argparse.ArgumentParser(description="Search NYC violation records by summons number.")
    parser.add_argument("--data", default="data/violations_sample.csv")
    parser.add_argument("--summons", help="Summons number to search")
    parser.add_argument("--download", action="store_true")
    parser.add_argument("--limit", type=int, default=10000)
    args = parser.parse_args()
    if args.download:
        print(f"Downloading up to {args.limit:,} NYC records...")
        download_sample(args.limit, args.data)
    records = load_records(args.data)
    print(f"Loaded {len(records):,} records.")
    if not args.summons:
        parser.error("provide --summons NUMBER")
    ordered = sorted(records, key=lambda row: str(row.get("summons_number", "")))
    index = build_hash_index(records)
    results = [
        ("Linear search", linear_search(records, args.summons)),
        ("Binary search", binary_search(ordered, args.summons)),
        ("Hash-table search", hash_search(index, args.summons)),
    ]
    for name, (record, checks) in results:
        print(f"\n{name}: {checks} comparison(s)/probe(s)")
        if record:
            for field in ("summons_number", "issue_date", "violation", "fine_amount", "amount_due", "state", "precinct"):
                if record.get(field):
                    print(f"  {field}: {record[field]}")
        else:
            print("  Not found in this downloaded sample.")
    print("A missing sample result does not prove that no ticket exists.")

if __name__ == "__main__":
    main()
