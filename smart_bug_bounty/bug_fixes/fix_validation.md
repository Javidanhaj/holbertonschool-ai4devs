# Smart Bug Bounty — Fix Validation

## Validation Method

All six files were corrected using minimal changes. The original buggy snippets in `bug_snippets/` remain unchanged. The corrected files were executed using Python assertions, Node.js assertions, and temporary Java assertion harnesses. Five checks were executed for each fix (30 checks total). These tests ran locally when this package was prepared; rerun them on your own machine before submitting.

| Original file | Fixed file | Original issue | Fix applied | Test cases | Result |
|---|---|---|---|---:|---|
| `bug1.py` | `bug1_fixed.py` | Off-by-one list slice | Changed `items[-n + 1:]` to `items[-n:]`. | 5 | PASS |
| `bug2.py` | `bug2_fixed.py` | Divided by all entries instead of valid entries | Changed denominator from `len(scores)` to `count`. | 5 | PASS |
| `bug3.js` | `bug3_fixed.js` | Excluded price equal to maximum | Changed `< maxPrice` to `<= maxPrice`. | 5 | PASS |
| `bug4.js` | `bug4_fixed.js` | Sorted deduplicated names alphabetically | Removed `.sort()` to preserve insertion order. | 5 | PASS |
| `bug5.java` | `bug5_fixed.java` | Initialized maximum to 0 | Initialized `largest` to `values[0]` after the existing empty check. | 5 | PASS |
| `bug6.java` | `bug6_fixed.java` | Skipped last index of inclusive range | Changed loop condition from `i < end` to `i <= end`. | 5 | PASS |

## Test Details

### bug1.py
- **Original issue:** Off-by-one list slice.
- **Fix applied:** Changed `items[-n + 1:]` to `items[-n:]`.
- **Tests:** Last 2; last 1; zero; n greater than length; input unchanged.
- **Result:** 5/5 checks passed.

### bug2.py
- **Original issue:** Divided by all entries instead of valid entries.
- **Fix applied:** Changed denominator from `len(scores)` to `count`.
- **Tests:** Invalid entries; normal average; empty; all invalid; boundary values.
- **Result:** 5/5 checks passed.

### bug3.js
- **Original issue:** Excluded price equal to maximum.
- **Fix applied:** Changed `< maxPrice` to `<= maxPrice`.
- **Tests:** Boundary price; mixed prices; empty; zero max; negative max rejection.
- **Result:** 5/5 checks passed.

### bug4.js
- **Original issue:** Sorted deduplicated names alphabetically.
- **Fix applied:** Removed `.sort()` to preserve insertion order.
- **Tests:** Mixed case duplicates; empty list; repeats; unsorted first appearance; whitespace.
- **Result:** 5/5 checks passed.

### bug5.java
- **Original issue:** Initialized maximum to 0.
- **Fix applied:** Initialized `largest` to `values[0]` after the existing empty check.
- **Tests:** Positive values; negatives; singleton; zero; empty rejection.
- **Result:** 5/5 checks passed.

### bug6.java
- **Original issue:** Skipped last index of inclusive range.
- **Fix applied:** Changed loop condition from `i < end` to `i <= end`.
- **Tests:** Middle-to-end; singleton; full array; negative values; invalid range rejection.
- **Result:** 5/5 checks passed.

## Reproduce the Tests

Python and Node.js snippets can be verified by importing the functions from the `bug_fixes/` directory and applying the examples in this document. For Java, compile `bug5_fixed.java` and `bug6_fixed.java` separately (`javac bug5_fixed.java bug6_fixed.java`) and exercise `Bug5.maxValue` and `Bug6.rangeSum` with a small Java test runner. Java classes remain package-private to support the assignment-required filenames.

## Limitations

These checks demonstrate the specified bug fixes; they are not exhaustive proofs of correctness. In particular, the minimal fixes intentionally do not redesign input validation for unrelated malformed inputs.
