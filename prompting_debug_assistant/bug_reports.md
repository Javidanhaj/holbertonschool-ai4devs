# Structured Bug Reports — AI-Assisted Debugging

**Project:** Prompting Debug Assistant  
**AI assistant:** ChatGPT  
**Date:** 2026-11-11  
**Original files:** `bug_snippets/`  
**Corrected files:** `bug_fixes/`  
**Test evidence:** `bug_fixes/fix_validation.md` and `bug_fixes/validate_fixes.py`

Each report describes a bug found in an intentionally flawed snippet. ChatGPT identified the cause and suggested a correction; the correction was saved in a separate `_fixed` file, leaving the original snippet unchanged. The fixes were checked against both sample inputs and additional edge cases. The test runner reported **28/28 passing checks**.

## Bug Report 1 — `bug_snippets/bug1.py` (Python)

- **Bug summary:** `last_n` returns too few items when `n > 0` and returns most of the list when `n == 0`.
- **Root cause:** The original slice `items[-n + 1:]` starts one element too far to the right. At `n == 0`, it becomes `items[1:]`. Simply using `items[-n:]` would also be wrong at zero because `-0` is `0` in Python.
- **Resolution — AI suggestion:** Handle `n == 0` explicitly with `return []`, then use `return items[-n:]` for other valid values. Preserve the existing negative-number and oversized-`n` checks.
- **Manual edits beyond the AI suggestion:** None. The original snippet remains in `bug_snippets/`; the solution is in `bug_fixes/bug1_fixed.py`.
- **Validation:** `last_n([10, 20, 30, 40, 50], 2)` returned `[40, 50]` as expected; `last_n(..., 0)` returned `[]`. **5/5 tests passed.**
- **Lessons learned:** Python slicing can hide boundary mistakes. Test zero, full-length, oversized, and negative inputs—not only ordinary cases.

**Before:** `return items[-n + 1:]`  
**After:**

```python
if n == 0:
    return []
return items[-n:]
```

## Bug Report 2 — `bug_snippets/bug2.py` (Python)

- **Bug summary:** Summing order prices crashes when an order does not include a `price` field.
- **Root cause:** `order["price"]` raises `KeyError: 'price'` for a dictionary such as `{"item": "Free sample"}`.
- **Resolution — AI suggestion:** Only add a value when the dictionary contains the `price` key: `if "price" in order:`.
- **Manual edits beyond the AI suggestion:** None. The corrected version is `bug_fixes/bug2_fixed.py`.
- **Validation:** Orders with prices `12`, `3`, and `5` plus one missing-price order returned `20` rather than crashing. **4/4 tests passed.**
- **Lessons learned:** Check whether required keys exist before indexing optional dictionary fields. Include incomplete records in test data.

**Before:** `total += order["price"]`  
**After:**

```python
if "price" in order:
    total += order["price"]
```

## Bug Report 3 — `bug_snippets/bug3.js` (JavaScript)

- **Bug summary:** The program cannot run even though the average calculation is otherwise correct.
- **Root cause:** The sample line `console.log("Average:", average;` is missing the closing `)`; Node.js rejects the file with `SyntaxError: missing ) after argument list`.
- **Resolution — AI suggestion:** Close the `console.log` call: `console.log("Average:", average);`.
- **Manual edits beyond the AI suggestion:** None. The corrected version is `bug_fixes/bug3_fixed.js`.
- **Validation:** The corrected program printed `Average: 80` for `[70, 80, 90]`; the helper returned `0` for an empty array. **4/4 tests passed.**
- **Lessons learned:** A small punctuation error can stop a whole script before runtime. Check parser errors first and avoid modifying working logic unnecessarily.

**Before:** `console.log("Average:", average;`  
**After:** `console.log("Average:", average);`

## Bug Report 4 — `bug_snippets/bug4.js` (JavaScript)

- **Bug summary:** The discount function returns the money saved rather than the final purchase price.
- **Root cause:** `price * discountRate` calculates only the discount amount. For example, a 10% discount on `$100` produces `$10`, not the desired final price of `$90`.
- **Resolution — AI suggestion:** Multiply by the remaining percentage using `price * (1 - discountRate)`. Keep the existing input-rate validation.
- **Manual edits beyond the AI suggestion:** None. The corrected version is `bug_fixes/bug4_fixed.js`.
- **Validation:** `applyDiscount(100, 0.10)` returned `90` and `applyDiscount(40, 0.25)` returned `30`. Boundary-rate checks also passed. **7/7 tests passed.**
- **Lessons learned:** A program can run without errors and still be logically wrong. Verify the meaning of each calculation with simple expected values.

**Before:** `return price * discountRate;`  
**After:** `return price * (1 - discountRate);`

## Bug Report 5 — `bug_snippets/bug5.c` (C)

- **Bug summary:** The array-summing function processes too few elements and returns the wrong total.
- **Root cause:** An array parameter declared as `int numbers[]` is adjusted to a pointer parameter inside the function. Thus, `sizeof(numbers)` measures the pointer, not the original array. The initial program produced a compiler warning and, on the tested environment, printed `Sum: 3` rather than `15`.
- **Resolution — AI suggestion:** Pass the number of elements as a separate `size_t count` parameter. Iterate while `i < count`, and calculate the element count in `main` with `sizeof(values) / sizeof(values[0])`, where `values` is a real array. Include `<stddef.h>` for `size_t`.
- **Manual edits beyond the AI suggestion:** None. The corrected version is `bug_fixes/bug5_fixed.c`.
- **Validation:** `{1, 2, 3, 4, 5}` returned `15`; three-element and zero-count tests passed. Strict compilation used `-std=c11 -Wall -Wextra -Werror -pedantic`. **4/4 tests passed.**
- **Lessons learned:** An array's size is not available from a pointer parameter. Pass explicit length information and pay attention to compiler warnings.

**Before:** `int count = sizeof(numbers) / sizeof(numbers[0]);` inside `sum_array`  
**After:** Use `int sum_array(const int numbers[], size_t count)` and call it with `sum_array(values, sizeof(values) / sizeof(values[0]))`.

## Bug Report 6 — `bug_snippets/bug6.c` (C)

- **Bug summary:** A character array containing `"admin"` is incorrectly classified as a regular user.
- **Root cause:** `username == "admin"` compares pointer addresses rather than the strings' characters; identical text does not imply identical addresses.
- **Resolution — AI suggestion:** Include `<string.h>` and compare contents with `strcmp(username, "admin") == 0`.
- **Manual edits beyond the AI suggestion:** None. The corrected version is `bug_fixes/bug6_fixed.c`.
- **Validation:** `"admin"` was recognized, while `"guest"` and uppercase `"ADMIN"` were not. Strict compilation used `-std=c11 -Wall -Wextra -Werror -pedantic`. **4/4 tests passed.**
- **Lessons learned:** Use a string comparison function, not `==`, for C strings. Test both matching and nonmatching values, including letter-case differences.

**Before:** `if (username == "admin")`  
**After:** `if (strcmp(username, "admin") == 0)`

## Overall Results and AI-Assisted Debugging Reflection

| Original file | Fixed file | Issue type | Verified result |
| --- | --- | --- | --- |
| `bug1.py` | `bug1_fixed.py` | Off-by-one / slice boundary | **5/5 PASS** |
| `bug2.py` | `bug2_fixed.py` | Missing dictionary key / exception | **4/4 PASS** |
| `bug3.js` | `bug3_fixed.js` | Syntax error | **4/4 PASS** |
| `bug4.js` | `bug4_fixed.js` | Arithmetic logic error | **7/7 PASS** |
| `bug5.c` | `bug5_fixed.c` | `sizeof` on pointer parameter | **4/4 PASS** |
| `bug6.c` | `bug6_fixed.c` | C string/pointer comparison | **4/4 PASS** |

**Total:** **28/28 tests passed**, using the reproducible test runner in `bug_fixes/validate_fixes.py`. No additional manual code changes were required beyond the AI-suggested corrections; test cases, validation tooling, and these reports were added to document and verify the work. AI assistance helped identify different classes of errors, but the final decision depended on running the corrected programs and comparing actual outputs with expectations.
