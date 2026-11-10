# Algorithm Notes and Correctness

## Task definition

Input: a list of records and a target summons number. Output: the matching record, or `None` if the target is absent from that list. The Python implementation converts the key to a string consistently. Binary search sorts and compares using the same string representation.

## Linear search

**Idea:** inspect records in their existing order.

```text
for each record:
    if record.key == target:
        return record
return NOT_FOUND
```

**Correctness:** every record is inspected unless a match is found. Therefore, a matching record is returned; if the loop finishes, no record matched.

**Complexity:** best O(1), average/worst O(n), auxiliary space O(1).

## Binary search

**Precondition:** records are sorted by the summons-number key in ascending order.

```text
low = 0
high = n - 1
while low <= high:
    mid = floor((low + high) / 2)
    if records[mid].key == target:
        return records[mid]
    if records[mid].key < target:
        low = mid + 1
    else:
        high = mid - 1
return NOT_FOUND
```

**Correctness:** sorted order proves that the half discarded after each comparison cannot contain the target. When the interval is empty, no match remains.

**Complexity:** best O(1), average/worst O(log n) comparisons, iterative auxiliary space O(1). Sorting beforehand is typically O(n log n) time and may require O(n) space for a separate sorted list.

## Hash-table lookup

**Idea:** create a dictionary mapping each summons number to its record.

```text
index = empty dictionary
for each record:
    if record.key is not empty:
        index[record.key] = record
return index.get(target)
```

**Correctness:** each valid key is stored with its record. Looking up the target returns the record associated with that key, or no value when the key is absent.

**Complexity:** expected O(n) time to build and O(n) auxiliary space. Lookup is O(1) average and O(n) worst case.

## Fair comparison

Report lookup time separately from preparation time. Binary search requires sorting; hash lookup requires building the index. For a one-time lookup, setup costs matter. For repeated searches over the same data, setup can be reused. A dictionary probe is not exactly the same unit as a record-by-record comparison, so do not claim the comparison counts are directly equivalent.

## Efficiency versus computational hardness

A linear search can be inefficient without the underlying problem being computationally hard. Exact-key lookup has efficient methods. The traveling-salesperson optimization problem is a separate example of an NP-hard problem; it is not solved by this project.
