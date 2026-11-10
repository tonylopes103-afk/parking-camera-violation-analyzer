# Algorithm notes

## Input and output
Input: a list of dictionaries containing summons_number and one target summons number. Output: matching record or None.

## Linear search pseudocode
FOR each record: compare its summons number with target; return if equal. If the loop ends, return not found. Correctness: every record is inspected, so any matching record in the list will be found.

## Binary search pseudocode
Set low and high. While low <= high, inspect the middle. If equal, return. If middle is smaller, continue right; otherwise continue left. Return not found if the interval becomes empty. Correctness: because the list is sorted, the discarded half cannot contain the target.

## Hash table
Build a dictionary from summons number to record. Average lookup is O(1); building the dictionary takes expected O(n) time and O(n) space.

## Efficiency versus hardness
The lookup task has efficient solutions. Linear search is slower because of the selected strategy, not because the task is inherently computationally hard. A related optimal multi-stop route planning problem can be computationally harder. Explain the distinction in your own words in the final paper.
