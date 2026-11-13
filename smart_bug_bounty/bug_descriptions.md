# Smart Bug Bounty — Bug Descriptions

## Purpose
Six deliberately flawed, standalone programming exercises for debugging and AI-assisted code review. Each snippet is 10–40 lines long and contains a reproducible logic bug. The intended behavior below defines what a successful fix must achieve; the files in `bug_snippets/` are **intentionally not fixed**.

## bug1.py — Last N Items (Python)
- **Intended behavior:** `last_items(items, n)` returns the final `n` list items in their original order. `n=0` returns an empty list; `n` greater than list length returns all items. Input must not be mutated.
- **Current issue:** An off-by-one error in the slice omits the earliest of the requested items.
- **Reproduce:** `last_items([10, 20, 30, 40], 2)` should return `[30, 40]`, but returns `[40]`.
- **Edge cases:** `n=1`, `n=0`, `n=len(items)`, and `n>len(items)`.

## bug2.py — Average Valid Scores (Python)
- **Intended behavior:** `average_score(scores)` calculates the average of numeric scores from 0 through 100, ignoring invalid entries and booleans. Return `0.0` if no valid scores remain, rounded to two decimals.
- **Current issue:** The sum is divided by the length of the original input rather than the number of valid entries.
- **Reproduce:** `average_score([80, 90, None])` should return `85.0`, but returns `56.67`.
- **Edge cases:** Empty lists, all-invalid lists, boundaries 0 and 100.

## bug3.js — Price Filtering (JavaScript)
- **Intended behavior:** `filterByPrice(products, maxPrice)` returns products whose numeric price is **less than or equal to** `maxPrice`, preserving input order.
- **Current issue:** The comparison excludes items priced exactly at the limit.
- **Reproduce:** With `[{name: "Notebook", price: 5}]` and limit `5`, expected one item, actual empty list.
- **Edge cases:** An empty product list, price equal to threshold, zero threshold.

## bug4.js — Unique Usernames (JavaScript)
- **Intended behavior:** `uniqueUsernames(users)` trims whitespace, compares names case-insensitively, and returns unique lowercase usernames **in order of first appearance**.
- **Current issue:** Sorting at the end changes the original first-seen order.
- **Reproduce:** `uniqueUsernames(["Zara", " ali ", "ZARA", "Mina"])` should return `["zara", "ali", "mina"]` but returns `["ali", "mina", "zara"]`.
- **Edge cases:** Repeated names, mixed case, whitespace, empty list.

## bug5.java — Maximum Array Value (Java)
- **Intended behavior:** `Bug5.maxValue(int[] values)` returns the largest array element. Reject null and empty arrays with `IllegalArgumentException`.
- **Current issue:** The initial maximum is `0`, which produces incorrect results if every value is negative.
- **Reproduce:** `Bug5.maxValue(new int[]{-9, -3, -7})` should return `-3`, but returns `0`.
- **Edge cases:** All-negative arrays, one element, zeros, repeated maximums.

## bug6.java — Inclusive Range Sum (Java)
- **Intended behavior:** `Bug6.rangeSum(values, start, end)` sums elements at indexes `start` through `end`, **including both endpoints**. Invalid ranges should throw `IllegalArgumentException`.
- **Current issue:** The loop excludes the value at `end`.
- **Reproduce:** For `{2, 4, 6, 8}` and indexes `1, 3`, expected `18`, actual `10`.
- **Edge cases:** Single-element ranges, the final index, full array, invalid indexes.

## Suggested Debugging Workflow
1. Read the expected behavior and run each snippet (Python 3, Node.js, or JDK).
2. Confirm the reported incorrect result.
3. Identify the defect and make the smallest justified change.
4. Add tests for the reproducible case and edge cases.
5. Record the fix and explain why it works.

## Running the Snippets
```bash
python3 bug_snippets/bug1.py
python3 bug_snippets/bug2.py
node bug_snippets/bug3.js
node bug_snippets/bug4.js
javac bug_snippets/bug5.java bug_snippets/bug6.java
java -cp bug_snippets Bug5
java -cp bug_snippets Bug6
```

**Java filename note:** The assignment requests `bug5.java` and `bug6.java`, so their classes should not be `public` when compiled directly with these filenames. Both class declarations in the submitted snippets are intentionally non-public to support `javac bug5.java bug6.java`; run them with `java -cp bug_snippets Bug5` and `java -cp bug_snippets Bug6` after compiling.
