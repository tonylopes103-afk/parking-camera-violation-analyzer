# Presentation: NYC Parking & Camera Violation Analyzer

**CPS 3440 — Analysis of Algorithms**  
**Suggested length:** 10–12 minutes  
**Student:** [Add your name]

Use this as the complete slide-by-slide content and speaking guide. Replace every bracketed item with your own measured result or personal details. Do not show estimated benchmark results as if they were measured.

## Slide 1 — Title (30 seconds)

**NYC Parking & Camera Violation Analyzer**  
Comparing Search Algorithms on Public NYC Data

- CPS 3440 — Analysis of Algorithms
- [Your name]
- Fall 2026

**Speaker notes:** My project compares three ways of finding a parking or camera violation record using its summons number. I use public data from New York City and focus on how the search method affects performance.

## Slide 2 — The Problem (1 minute)

- NYC publishes a large collection of parking and camera violation records.
- Finding one record by summons number is a search problem.
- Checking every row can take longer as the dataset grows.
- Research question: Which search approach is most suitable, when setup costs are included?

**Speaker notes:** The goal is not to decide whether a ticket is correct or whether money is owed. The goal is to compare algorithms that find a record in a collection.

## Slide 3 — Dataset (1 minute)

- Source: NYC Department of Finance / NYC Open Data
- Dataset: Open Parking and Camera Violations
- Dataset ID: nc67-uf89
- Fields used: summons number, issue date, violation, fine amount, amount due, state, and precinct
- The program downloads a limited CSV sample.

**Speaker notes:** The source changes over time, so I record the date I downloaded the data and the number of records in my sample. If a summons number is missing from my sample, it may still exist in the full dataset.

## Slide 4 — Problem Formulation (45 seconds)

**Input:** A list of violation records and one target summons number.  
**Output:** The matching record or “not found.”

- All three algorithms receive the same target.
- Binary search uses a sorted copy.
- Hash search uses a dictionary built from the records.

**Speaker notes:** This makes the comparison fair because the algorithms solve the same task. The difference is how the records are organized and checked.

## Slide 5 — Algorithm 1: Linear Search (1 minute)

- Start at the first record.
- Compare its summons number with the target.
- Stop when it matches or the list ends.
- Worst-case time: O(n)
- Extra space: O(1)

**Speaker notes:** Linear search is the easiest method to understand. If the record is at the end or is not present, the algorithm may have to check every record. It does not need the data to be sorted.

## Slide 6 — Algorithm 2: Binary Search (1 minute)

- The records must be sorted by summons number.
- Check the middle record.
- Keep only the half that could contain the target.
- Worst-case lookup: O(log n)
- Iterative extra space: O(1)
- Sorting is a separate preparation cost, typically O(n log n).

**Speaker notes:** Binary search is faster because it removes about half of the remaining search area each time. It cannot be used correctly on an unsorted list.

## Slide 7 — Algorithm 3: Hash-Table Search (1 minute)

- Build a dictionary: summons number → record.
- Look up the target key in the dictionary.
- Average lookup: O(1)
- Worst-case lookup: O(n)
- Index construction: expected O(n) time and O(n) space.

**Speaker notes:** The dictionary takes time and memory to build. If I search the same dataset many times, that one-time cost can be worthwhile. If I only search once, setup time matters more.

## Slide 8 — Complexity Comparison (1 minute)

| Method | Average/worst lookup | Preparation |
|---|---|---|
| Linear | O(n) | None |
| Binary | O(log n) | Sort records |
| Hash table | O(1) average; O(n) worst | Build dictionary |

**Speaker notes:** Big-O explains how the work grows as the number of records increases. It does not tell me the exact number of seconds. I measure setup separately so the comparison does not hide the cost of sorting or building the index.

## Slide 9 — Experiment and Results (1–2 minutes)

- Dataset sizes tested: [insert actual row counts]
- Computer and Python version: [insert details]
- Repeated trials: 7 per method in the current benchmark
- Measurement: median lookup time; hash-index build time reported separately
- Results table/chart: [insert actual benchmark output]

| Records | Linear (s) | Binary (s) | Hash (s) |
|---:|---:|---:|---:|
| [actual] | [actual] | [actual] | [actual] |
| [actual] | [actual] | [actual] | [actual] |
| [actual] | [actual] | [actual] | [actual] |

**Speaker notes:** Explain what the measurements actually show. Do not claim one method won unless the results support that statement. Mention whether sorting or index construction changed the best choice.

## Slide 10 — Theory vs. Measured Performance (1 minute)

- Did the measured trend match the Big-O prediction?
- Did the dataset size change the gap between methods?
- Did sorting or index construction take noticeable time?
- Possible influences: Python overhead, memory, caching, input order, and computer activity.

**Speaker notes:** Big-O describes growth, not exact runtime. Real measurements can differ because of implementation details and the cost of preparing the data.

## Slide 11 — Efficiency vs. Computational Hardness (45 seconds)

- A slow linear search is an inefficient algorithm choice.
- Exact-key lookup has efficient solutions.
- This lookup task is not an NP-hard problem.
- A related harder problem is finding an optimal route through many required stops, a version related to the NP-hard traveling-salesperson problem.

**Speaker notes:** The difficulty here is mostly about choosing and organizing the data for an efficient search, not about an inherently hard problem.

## Slide 12 — Recommendation and Conclusion (45 seconds)

- Linear search: good for small or unsorted data and one-off searches.
- Binary search: useful when records are sorted and extra memory should stay low.
- Hash table: recommended for repeated exact-key searches when index memory is available.
- Final recommendation: [confirm using your measured results].

**Speaker notes:** I recommend the method that best fits the expected use. For many repeated summons-number lookups, a hash table is likely the practical choice after the index is built. I will compare this recommendation with the actual benchmark results.

## Final demo checklist

- Download the sample dataset.
- Choose a summons number that appears in the downloaded CSV.
- Run the Python search command.
- Run the unit tests.
- Run the benchmark and show the generated CSV.
- Explain that the website's browser demo uses fictional example records, not live ticket data.

## Questions to prepare for

1. Why does binary search require sorted data?
2. What is the cost of building the hash table?
3. Why can a hash lookup be O(1) on average but O(n) in the worst case?
4. Why is the local sample not the same as the full NYC dataset?
5. What is the difference between an inefficient algorithm and an NP-hard problem?
