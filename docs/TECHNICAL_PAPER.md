# Searching NYC Parking and Camera Violations: An Algorithmic Comparison

**Course:** CPS 3440 — Analysis of Algorithms  
**Project:** Parking and Camera Violation Analyzer  
**Student:** [Add your name]  
**Date:** [Add submission date]

> **Submission note:** This is a complete written draft of the project analysis based on the repository's current implementation. The bracketed experiment fields must be completed after running the program on your computer. Do not submit invented measurements. Record the exact sample size, computer/software environment, and measured times from your own runs.

## Abstract

New York City publishes a large public dataset of parking and camera violation records. Finding a record by its summons number is a simple task, but the time required can change significantly depending on how the records are organized and which search algorithm is used. This project implements and compares three approaches in Python: linear search, binary search, and hash-table lookup. Linear search checks records one at a time. Binary search repeatedly halves a sorted search range. Hash-table lookup uses a Python dictionary that is built before the search. The project uses a downloadable sample of the NYC Open Parking and Camera Violations dataset (nc67-uf89), rather than attempting to store the entire public dataset in the repository. The theoretical analysis predicts O(n) worst-case time for linear search, O(log n) time for binary search after sorting, and O(1) average lookup time for a hash table after O(n) index construction. The repository includes tests and a repeatable benchmark script. The final measured results must be inserted after executing the experiments; this paper distinguishes theoretical expectations from results that have not yet been measured.

## 1. Introduction

Public agencies publish data so that residents, researchers, and developers can examine government activity. However, a large dataset is only useful when people can locate and interpret the information they need. The NYC Open Parking and Camera Violations dataset contains records issued by the City of New York. A person or analyst may want to locate one record using its summons number.

The main problem in this project is therefore a search problem: given a collection of violation records and a target summons number, return the matching record or report that no match exists in the collection. The project does not decide whether a ticket is legally valid, whether a person owes money, or whether a ticket should be appealed. It studies the efficiency of searching the records available in the downloaded sample.

The research question is: **How do linear search, binary search, and hash-table lookup compare when finding a summons number in a growing collection of NYC violation records, and what are the costs of preparing the data for each method?**

The objectives are to (1) obtain a reproducible sample of public data, (2) implement the three search methods, (3) explain their correctness and time/space complexity, (4) test the implementations, and (5) measure performance across multiple input sizes. A fair comparison must include preprocessing costs. Binary search requires sorted data, while hash lookup requires constructing a dictionary index.

## 2. Dataset

The project uses the **Open Parking and Camera Violations** dataset, dataset ID **nc67-uf89**, published through NYC Open Data and provided by the NYC Department of Finance. The official dataset page is https://data.cityofnewyork.us/City-Government/Open-Parking-and-Camera-Violations/nc67-uf89/about_data. The public CSV API used by the loader is https://data.cityofnewyork.us/resource/nc67-uf89.csv.

The source describes records of parking and camera violations. Its data is updated over time; the city describes different update schedules for new/open violations and for records whose status has changed. Therefore, a downloaded copy is a snapshot and may not match the live source later. The project downloads a limited sample, ordered by issue date, so it can be reproduced without committing a very large data file to GitHub.

The current loader selects these fields:

- `summons_number`: the identifier used as the search key.
- `issue_date`: the date associated with the violation.
- `violation`: the violation description.
- `fine_amount`: the listed fine amount.
- `amount_due`: the listed amount due.
- `state`: the vehicle registration state.
- `precinct`: the associated precinct field.

Before final submission, record the download date, exact number of rows in `data/violations_sample.csv`, any missing or blank summons numbers, and the date range represented by the sample. These values depend on the actual download and must be measured rather than guessed. The program searches only the local sample. If a summons number is not found in the sample, that does not prove the record is absent from the complete NYC dataset.

## 3. Problem Formulation

Let (R = [r_0,r_1,\ldots,r_{n-1}]) be a collection of (n) violation records. Each record contains a summons number. Let (k) be the target summons number supplied by the user.

**Input:** a collection of records (R) and a target key (k).  
**Output:** the record (r_i) whose summons number equals (k), if one exists; otherwise, a not-found result.

The three algorithms solve the same task. They differ in the order in which they examine records and in the data structures they use. For the binary-search method, records must be sorted by summons number using the same string comparison rule used during searching. For the hash method, a dictionary maps each non-empty summons number to its record. The implementation assumes that a summons number identifies one record for the purpose of this demonstration. If duplicate keys occur, the dictionary construction keeps the last record encountered; this behavior should be checked when validating the downloaded data.

## 4. Algorithms

### 4.1 Linear search

Linear search starts at the first record and compares its summons number with the target. If the keys match, it returns the record. Otherwise, it continues until a match is found or every record has been checked.

**Pseudocode**

```text
LINEAR-SEARCH(records, target)
    for each record in records
        if record.summons_number equals target
            return record
    return NOT-FOUND
```

The method works whether or not the records are sorted. If the first record matches, the best case is O(1). If the match is last or the key is absent, it may inspect all n records, giving O(n) worst-case time. It uses O(1) auxiliary space because it does not build another collection.

### 4.2 Binary search

Binary search requires records sorted by summons number. It compares the target with the middle record. If the target is smaller, it continues in the left half; if larger, it continues in the right half. Each step discards approximately half of the remaining candidates.

**Pseudocode**

```text
BINARY-SEARCH(sorted_records, target)
    low = 0
    high = number of records - 1
    while low <= high
        middle = floor((low + high) / 2)
        if sorted_records[middle].summons_number equals target
            return sorted_records[middle]
        if sorted_records[middle].summons_number is less than target
            low = middle + 1
        else
            high = middle - 1
    return NOT-FOUND
```

The implementation uses an iterative loop. Each comparison cuts the remaining search interval roughly in half, so the worst-case number of comparisons is O(log n). The iterative implementation uses O(1) auxiliary space. However, sorting the records first has a cost, typically O(n log n) time for comparison sorting and O(n) storage for a separate sorted list in this project. If the data is already sorted and many searches will be performed, the sorting cost can be amortized over those searches.

### 4.3 Hash-table lookup

The hash approach builds a dictionary in which the key is the summons number and the value is the full record. A lookup then asks the dictionary for the target key.

**Pseudocode**

```text
BUILD-INDEX(records)
    index = empty dictionary
    for each record in records
        if record has a non-empty summons number
            index[record.summons_number] = record
    return index

HASH-SEARCH(index, target)
    return index.get(target)
```

Building the dictionary requires one pass through the records, so expected construction time is O(n) and auxiliary storage is O(n). A dictionary lookup is O(1) on average, although collisions can make worst-case lookup O(n). The hash method is attractive when the same dataset will be searched many times because the one-time index construction can be reused.

## 5. Correctness and Complexity Analysis

**Linear search correctness:** The algorithm checks every record in the collection in order. If a matching record exists, it will eventually be checked and returned. If the loop ends without finding a match, no record in the collection matched the target. Therefore, the returned answer is correct.

**Binary search correctness:** The sorted order provides the key property. When the middle key is smaller than the target, every key at or to the left of the middle is also smaller, so that half cannot contain the target. When the middle key is larger, every key at or to the right is also larger, so that half cannot contain the target. The algorithm only removes a half that cannot contain a match. If the search interval becomes empty, no matching key exists. Therefore, the result is correct when the input is sorted using the same ordering rule.

**Hash lookup correctness:** During index construction, each non-empty key is associated with its record. A dictionary lookup returns the value stored for the target key, or no value when the key is absent. Under the stated key assumption, this returns the matching record or not-found.

| Method | Best lookup | Average lookup | Worst lookup | Extra space / preparation |
|---|---:|---:|---:|---|
| Linear search | O(1) | O(n) | O(n) | O(1) extra space |
| Binary search | O(1) | O(log n) | O(log n) | O(1) lookup space; sorting costs O(n log n) time |
| Hash table | O(1) average | O(1) average | O(n) | O(n) index space; expected O(n) build time |

The table separates lookup complexity from preparation. Comparing only lookup time would make binary search and hashing appear free to prepare, which would not be a fair description of the full workflow.

## 6. Implementation

The project is implemented in Python and organized into separate modules:

- `src/data_loader.py` downloads a limited CSV sample from the NYC Open Data API and reads records into Python dictionaries.
- `src/algorithms.py` contains the linear search, binary search, dictionary-index construction, and hash lookup functions.
- `src/main.py` provides a command-line search by summons number.
- `tests/test_algorithms.py` checks found and not-found cases for the search methods.
- `benchmarks/run_benchmarks.py` measures repeated lookup times and writes a CSV result file.
- `index.html` provides the project portfolio website and a small illustrative browser demo.

The browser demo uses clearly labeled fictional example records. It is not connected to the NYC live dataset and must not be presented as a real ticket lookup service. The Python application is the component that searches the downloaded public-data sample.

## 7. Experimental Methodology

The experiment should compare all three methods on the same records and target key. Download samples of increasing sizes, for example 1,000, 10,000, and 100,000 records where the public API and available computer resources permit. Keep the computer, Python version, and measurement procedure consistent.

For each size:

1. Download the sample and record its actual row count.
2. Select a target that is present in the sample and record its position in the unsorted list. Also consider a target that is not present.
3. Run linear search repeatedly and record lookup time.
4. Sort a copy of the records by summons number, time the sorting step separately, and run binary search repeatedly.
5. Build the dictionary index, time index construction separately, and run dictionary lookup repeatedly.
6. Use the median of repeated trials to reduce the effect of unusually short or long runs.
7. Save the results and create a graph of input size against lookup time.

The repository benchmark currently performs seven timing trials and saves the measured times and hash-index build time to `results/benchmark_results.csv`. Its current run uses one target from the downloaded records. For a stronger final experiment, repeat across multiple input sizes and test both present and absent targets. Record the exact command and any changes made to the benchmark script. A useful additional metric is the number of record comparisons for linear and binary search. A hash lookup probe is not directly equivalent to a record-by-record comparison, so report it separately.

**Environment used:** [Computer/processor and RAM]  
**Operating system:** [Windows/macOS/Linux and version]  
**Python version:** [Run `python --version`]  
**Download date:** [Date]  
**Actual row counts:** [Insert counts for each sample]

## 8. Results

Do not fill this section with estimates. Insert the CSV measurements produced by the program. A results table should look like this:

| Actual records | Linear median (s) | Binary median (s) | Hash median (s) | Sort time (s) | Hash build time (s) |
|---:|---:|---:|---:|---:|---:|
| 1,000 | [measure] | [measure] | [measure] | [measure] | [measure] |
| 10,000 | [measure] | [measure] | [measure] | [measure] | [measure] |
| 100,000 | [measure] | [measure] | [measure] | [measure] | [measure] |

**What the measurements show:** [After running the experiment, identify which method had the lowest lookup time at each size. Explain whether preparation costs change the best choice. Mention any surprising result and repeat the test if needed.]

**Graph:** [Insert a chart with input size on the horizontal axis and median lookup time on the vertical axis. Use a separate chart or a clearly readable scale if one method makes the others difficult to see.]

## 9. Theory vs. Observed Performance

The theoretical prediction is that linear search grows in proportion to the number of records in the worst case, binary search grows much more slowly because it halves the search interval, and dictionary lookup is expected to remain approximately constant on average after the index has been built. The measured results should be compared with these trends rather than expected to match exact mathematical values.

Real runtime is affected by constant factors and implementation details. Python function-call overhead, string conversion, memory layout, CPU speed, operating-system activity, and cache behavior can affect the measured times. Sorting and building a dictionary also require work before lookup. For one search on a small dataset, setup time may outweigh the benefit of a faster lookup. For many searches on the same records, the setup cost can be spread across the searches. The final analysis should use the actual table and graph to say whether the observed trends agree with theory.

## 10. Algorithmic Efficiency vs. Computational Hardness

This project is primarily an example of algorithmic efficiency, not an inherently computationally hard problem. Searching for an exact key in a collection has straightforward solutions. Linear search can be inefficient on a large unsorted collection because it may examine every record. Binary search and hash indexing improve lookup efficiency by using data organization and preprocessing. The problem itself is not made NP-hard simply because a slow search implementation is used.

Computational hardness describes problems for which no known algorithm can solve every instance efficiently as input size grows, under widely believed complexity assumptions. A related but different problem would be finding an optimal route that visits many required locations while minimizing total travel distance. The traveling-salesperson problem is a well-known NP-hard optimization problem. It is not what this project implements; it is included only to clarify the difference between choosing an inefficient search method and facing a problem with much greater inherent computational difficulty.

## 11. Limitations and Ethical / Societal Considerations

The application uses a sample, not the entire NYC dataset. A not-found result means only that the target was not found in the local sample. Public data can change after download, and some fields may be blank or incomplete. The browser demonstration contains fictional records and is for illustrating search behavior only. It does not connect to official ticket systems, verify a ticket, provide legal advice, or determine whether a balance is owed.

The project should avoid publishing unnecessary personal or vehicle information. Even when information is publicly accessible, it should be used only for the educational purpose of this assignment. Results should be described accurately so that a reader does not mistake the project for an official City of New York service.

## 12. Course Learning Objective Reflection

### CLO A — Efficiency

The project demonstrates why efficiency matters by comparing the work required to find the same summons number as the collection grows. After completing the benchmark, insert one concrete measured comparison here: **[state the input size, the measured linear-search time, the measured alternative time, and the difference].** This evidence will show whether the faster theoretical approach also provided a practical benefit in the experiment.

### CLO B — Complexity

Binary search is a useful example because each comparison removes approximately half of the remaining sorted records. Its worst-case lookup time is O(log n), and the iterative implementation uses O(1) auxiliary space. Sorting the records first has a separate cost, typically O(n log n). Compare these predictions with the measured results: **[describe whether the benchmark trend agreed with theory and explain any differences].**

### CLO C — Hardness

The summons-number lookup problem is not inherently computationally hard. A linear search may be inefficient because it uses a method that checks records one by one. Better data organization makes the same task faster. This differs from an NP-hard optimization problem such as finding the shortest route through a large set of required stops, where the difficulty is inherent to the problem rather than only a poor implementation choice.

### CLO D — Algorithm Selection

The project investigates linear search, binary search, and hash-table lookup. For a one-time search in unsorted data, linear search is simple and requires no preparation. For repeated searches on a dataset that can be sorted once, binary search offers predictable O(log n) lookup with low extra lookup space. For many exact-key lookups on the same dataset, a hash table is the recommended practical approach because its average lookup time is O(1), provided that the O(n) index-building time and memory cost are acceptable. The final recommendation should be checked against the actual benchmark results and the expected number of searches.

## 13. Conclusion

This project examines how the choice of search algorithm affects the task of finding one summons number in public violation data. Linear search is easy to implement and works on unsorted records, but its worst-case work grows linearly. Binary search reduces the search interval quickly but requires sorted input. Hash-table lookup is expected to be constant time on average after an index has been built, at the cost of additional memory and preparation time. The best method depends on whether the data is already organized and how many searches will be performed. Completing the experiments with real measurements is necessary to confirm the practical recommendation.

## References

City of New York, Department of Finance. (n.d.). *Open Parking and Camera Violations* [Data set]. NYC Open Data. https://data.cityofnewyork.us/City-Government/Open-Parking-and-Camera-Violations/nc67-uf89/about_data

Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2022). *Introduction to algorithms* (4th ed.). MIT Press.

[Add the course textbook or lecture materials if your instructor requires them. Check the required citation style before submission.]
