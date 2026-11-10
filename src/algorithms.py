"""Three student-implemented searches for violation records."""
def linear_search(records, target):
    """Return (record or None, comparisons); worst-case O(n)."""
    comparisons = 0
    for record in records:
        comparisons += 1
        if str(record.get("summons_number", "")) == str(target):
            return record, comparisons
    return None, comparisons

def binary_search(sorted_records, target):
    """Binary search records already sorted by summons_number; O(log n)."""
    low, high = 0, len(sorted_records) - 1
    target = str(target)
    comparisons = 0
    while low <= high:
        middle = (low + high) // 2
        value = str(sorted_records[middle].get("summons_number", ""))
        comparisons += 1
        if value == target:
            return sorted_records[middle], comparisons
        if value < target:
            low = middle + 1
        else:
            high = middle - 1
    return None, comparisons

def build_hash_index(records):
    """Build a dictionary index; expected O(n) time and O(n) space."""
    index = {}
    for record in records:
        key = str(record.get("summons_number", ""))
        if key:
            index[key] = record
    return index

def hash_search(index, target):
    """Dictionary lookup; average O(1), worst-case O(n)."""
    return index.get(str(target)), 1
