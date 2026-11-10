# CPS 3440 Technical Paper Template

Target length: 6–10 pages. Replace every instruction with your own explanation and measured evidence. Do not submit placeholder text or invented benchmark results.

## Abstract
Briefly describe the real-world problem, dataset, three algorithms, experiment design, and main measured finding.

## 1. Introduction
Explain why searching large violation datasets matters. State the research question and project objectives.

## 2. Dataset
Identify NYC Open Data dataset nc67-uf89, provider, official URL, date downloaded, exact number of rows, fields used, missing values, preprocessing, licensing/usage notes, and limitations. Explain that the program searches only the sample downloaded.

## 3. Problem Formulation
Define the input as a list of violation records and a target summons number. Define the output as the matching record or not-found result.

## 4. Algorithms
For linear search, binary search, and hash-table search: describe the approach, give pseudocode, explain required data structures, and state assumptions. Explain that binary search requires sorted data and hash search requires building an index.

## 5. Correctness and Complexity Analysis
Give a correctness argument for each method. Analyze best, average where meaningful, and worst-case time. Include auxiliary space and preprocessing costs.

## 6. Implementation
Describe Python modules, data loading, tests, and how to reproduce the project.

## 7. Experimental Methodology
Describe computer/OS/Python version, dataset sizes, target selection, number of trials, median measurement, and metrics. Separate sorting and hash-index construction from lookup time.

## 8. Results
Insert your real tables and graphs. Include 1,000, 10,000, and 100,000 records where feasible. Explain trends; do not fabricate values.

## 9. Theory vs. Observed Performance
Explain whether measurements follow Big-O expectations. Discuss constants, Python dictionary implementation, memory, data ordering, caching, preprocessing, and system noise.

## 10. Algorithmic Efficiency vs. Computational Hardness
Explain that this lookup task has efficient solutions and that linear search is an algorithm-choice issue, not inherently a hard problem. Discuss a related computationally harder problem if appropriate.

## 11. Limitations and Ethical / Societal Considerations
Discuss data freshness, incomplete samples, public-record limitations, privacy, and the risk of treating a sample search as official ticket status.

## 12. Course Learning Objective Reflection
- CLO A: Give one measured result demonstrating why efficiency matters.
- CLO B: Explain one algorithm's time and space complexity and compare theory with measurements.
- CLO C: Explain inefficient algorithm choice versus inherent computational hardness.
- CLO D: Compare the investigated algorithms and justify the recommended method.

## 13. Conclusion
Summarize findings and future improvements.

## References
Cite the NYC Open Data dataset and any course/textbook or external sources used, following the instructor's required citation style.
