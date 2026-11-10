"""Download and load a sample from NYC Open Data."""
import csv
from pathlib import Path
from urllib.request import Request, urlopen

DATASET_ID = "nc67-uf89"
API_URL = f"https://data.cityofnewyork.us/resource/{DATASET_ID}.csv"
FIELDS = "summons_number,issue_date,violation,fine_amount,amount_due,state,precinct"

def download_sample(limit=10000, output_path="data/violations_sample.csv"):
    if limit < 1:
        raise ValueError("limit must be at least 1")
    query = f"?$select={FIELDS}&$limit={int(limit)}&$order=issue_date DESC"
    request = Request(API_URL + query, headers={"User-Agent": "CPS3440-Student-Project/1.0"})
    with urlopen(request, timeout=90) as response:
        content = response.read()
    destination = Path(output_path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(content)
    return destination

def load_records(path="data/violations_sample.csv"):
    with open(path, "r", newline="", encoding="utf-8-sig") as file:
        return list(csv.DictReader(file))
