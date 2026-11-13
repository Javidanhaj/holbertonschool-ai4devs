# Smart Bug Bounty — Fix Validation

## Source-to-Fix Comparison

The comparisons below are **between the original files in `../bug_snippets/` and their corresponding fixed files in this folder**. It is expected that a removed expression such as `.sort()` does not appear in the fixed file; it appears in the original file. No original files were edited.

Each issue was confirmed by inspecting both source versions. The fixed behavior was verified with `run_validation.py`. The test runner performs 5 checks per snippet, for 30 checks overall.

## Bug 1: `bug1.py` → `bug1_fixed.py`

- **Original issue:** List slicing returned one fewer than requested.
- **Original file:** `../bug_snippets/bug1.py`
- **Fixed file:** `bug1_fixed.py`
- **Before (original buggy code):**
```python
return items[-n + 1:]
```
- **After (corresponding corrected code):**
```python
return items[-n:]
```
- **Fix applied:** Replaced the original expression above with the corrected expression shown. Other surrounding code and validations were retained.
- **Test scenarios (5):** Last 2; last 1; zero count; oversized count; original list unchanged.
- **Test results:** **5/5 PASS**, using `python3 run_validation.py`.

## Bug 2: `bug2.py` → `bug2_fixed.py`

- **Original issue:** Average divided by all input entries, including invalid ones.
- **Original file:** `../bug_snippets/bug2.py`
- **Fixed file:** `bug2_fixed.py`
- **Before (original buggy code):**
```python
return round(total / len(scores), 2)
```
- **After (corresponding corrected code):**
```python
return round(total / count, 2)
```
- **Fix applied:** Replaced the original expression above with the corrected expression shown. Other surrounding code and validations were retained.
- **Test scenarios (5):** Invalid score excluded; normal scores; empty input; all invalid; 0/100 boundaries.
- **Test results:** **5/5 PASS**, using `python3 run_validation.py`.

## Bug 3: `bug3.js` → `bug3_fixed.js`

- **Original issue:** Product priced exactly at the limit was excluded.
- **Original file:** `../bug_snippets/bug3.js`
- **Fixed file:** `bug3_fixed.js`
- **Before (original buggy code):**
```javascript
if (product.price < maxPrice) {
```
- **After (corresponding corrected code):**
```javascript
if (product.price <= maxPrice) {
```
- **Fix applied:** Replaced the original expression above with the corrected expression shown. Other surrounding code and validations were retained.
- **Test scenarios (5):** Equal price; mixed prices; empty products; zero price; invalid negative limit.
- **Test results:** **5/5 PASS**, using `python3 run_validation.py`.

## Bug 4: `bug4.js` → `bug4_fixed.js`

- **Original issue:** Alphabetical sorting destroyed first-seen username order.
- **Original file:** `../bug_snippets/bug4.js`
- **Fixed file:** `bug4_fixed.js`
- **Before (original buggy code):**
```javascript
return result.sort();
```
- **After (corresponding corrected code):**
```javascript
return result;
```
- **Fix applied:** Replaced the original expression above with the corrected expression shown. Other surrounding code and validations were retained.
- **Test scenarios (5):** Case insensitive; empty; duplicates; insertion order; whitespace normalization.
- **Test results:** **5/5 PASS**, using `python3 run_validation.py`.

## Bug 5: `bug5.java` → `bug5_fixed.java`

- **Original issue:** Starting maximum at zero produced a wrong result for all-negative arrays.
- **Original file:** `../bug_snippets/bug5.java`
- **Fixed file:** `bug5_fixed.java`
- **Before (original buggy code):**
```java
int largest = 0;
```
- **After (corresponding corrected code):**
```java
int largest = values[0];
```
- **Fix applied:** Replaced the original expression above with the corrected expression shown. Other surrounding code and validations were retained.
- **Test scenarios (5):** Positive numbers; negatives; singleton; zero; empty array throws.
- **Test results:** **5/5 PASS**, using `python3 run_validation.py`.

## Bug 6: `bug6.java` → `bug6_fixed.java`

- **Original issue:** Exclusive end check omitted the last element.
- **Original file:** `../bug_snippets/bug6.java`
- **Fixed file:** `bug6_fixed.java`
- **Before (original buggy code):**
```java
for (int i = start; i < end; i++) {
```
- **After (corresponding corrected code):**
```java
for (int i = start; i <= end; i++) {
```
- **Fix applied:** Replaced the original expression above with the corrected expression shown. Other surrounding code and validations were retained.
- **Test scenarios (5):** Middle to end; singleton; full range; negatives; invalid range throws.
- **Test results:** **5/5 PASS**, using `python3 run_validation.py`.

## Automated Test Evidence

Run from `smart_bug_bounty/bug_fixes/`:

```bash
python3 run_validation.py
```

This runner imports the fixed Python functions, executes Node.js assertions against the fixed JavaScript modules, and compiles/runs Java assertions in a temporary directory. It exits nonzero if any check fails.

**Observed result from running the test suite during preparation:**
```text
TOTAL: 30/30 PASS
```

The full per-check output is saved in `test_results.txt`.

## Scope

The test scenarios verify the six originally identified defects and selected boundary cases. They do not establish that the code is error-free for every possible input.
