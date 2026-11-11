# Fix Validation Report

**Project:** AI-Assisted Debugging  
**AI assistant:** ChatGPT  
**Files validated:** `bug1_fixed.py` through `bug6_fixed.c`  
**Date:** 2026-11-11  
**Environment:** Python 3.13.5, Node.js 22.16.0, GCC 14.2.0 (C11)

Each corrected file corresponds to an original in `../bug_snippets/`. The original snippets are preserved unchanged. The fixes follow the AI diagnoses recorded in `../bug_snippets/ai_debug_log.md`. I ran each corrected program, then checked additional inputs using assertions, Node.js test expressions, or a small temporary C test harness. For C, I compiled using `-std=c11 -Wall -Wextra -Werror -pedantic` so warnings would count as failures.

## Bug 1 — `bug1_fixed.py` (Python)

**Root cause:** `items[-n + 1:]` had an off-by-one error and behaved incorrectly when `n == 0`.  
**Fix:** Return `[]` for `n == 0`; otherwise use `items[-n:]`. Preserve checks for negative and oversized `n`.

| Test input | Expected | Actual | Status |
|---|---|---|---|
| `last_n([10,20,30,40,50], 2)` | `[40,50]` | `[40,50]` | PASS |
| `last_n([10,20,30,40,50], 0)` | `[]` | `[]` | PASS |
| `last_n([10,20,30,40,50], 5)` | `[10,20,30,40,50]` | `[10,20,30,40,50]` | PASS |
| `last_n([10,20,30,40,50], 8)` | `[10,20,30,40,50]` | `[10,20,30,40,50]` | PASS |
| `last_n([1,2], -1)` | `ValueError` | `ValueError` | PASS |

**Run command:** `python3 bug1_fixed.py`  
**Sample output:** `Last 2: [40, 50]`; `Last 0: []`.  
**Additional checks:** Imported the function and compared each return value or exception to the expected result.  
**Manual tweaks beyond AI suggestion:** None.

## Bug 2 — `bug2_fixed.py` (Python)

**Root cause:** Unconditional `order["price"]` raised `KeyError` for entries with no price.  
**Fix:** Only add a price when the key exists.

| Test input | Expected | Actual | Status |
|---|---|---|---|
| Prices `[12,3,missing,5]` | `20` | `20` | PASS |
| One order with no price | `0` | `0` | PASS |
| Empty order list `[]` | `0` | `0` | PASS |
| Prices `[0,7]` | `7` | `7` | PASS |

**Run command:** `python3 bug2_fixed.py`  
**Sample output:** `Order total: 20`.  
**Additional checks:** Called `calculate_total()` on the extra lists and compared returned totals.  
**Manual tweaks beyond AI suggestion:** None.

## Bug 3 — `bug3_fixed.js` (JavaScript)

**Root cause:** Missing closing parenthesis in `console.log("Average:", average;`.  
**Fix:** Close the function call with `);`.

| Test input | Expected | Actual | Status |
|---|---|---|---|
| `calculateAverage([70,80,90])` | `80` | `80` | PASS |
| `calculateAverage([])` | `0` | `0` | PASS |
| `calculateAverage([10,20])` | `15` | `15` | PASS |
| Run sample program | `Average: 80` | `Average: 80` | PASS |

**Run command:** `node bug3_fixed.js`  
**Additional checks:** Evaluated the script in a Node.js `vm` context and asserted function results.  
**Manual tweaks beyond AI suggestion:** None.

## Bug 4 — `bug4_fixed.js` (JavaScript)

**Root cause:** `price * discountRate` gave the discount amount rather than the price after discount.  
**Fix:** Use `price * (1 - discountRate)` and preserve the existing range check.

| Test input | Expected | Actual | Status |
|---|---|---|---|
| `applyDiscount(100, 0.10)` | `90` | `90` | PASS |
| `applyDiscount(40, 0.25)` | `30` | `30` | PASS |
| `applyDiscount(100, 0)` | `100` | `100` | PASS |
| `applyDiscount(100, 1)` | `0` | `0` | PASS |
| `applyDiscount(100, -0.1)` | Throws error | Throws error | PASS |
| `applyDiscount(100, 1.1)` | Throws error | Throws error | PASS |
| Run sample program | `$90.00`, `$30.00` | `$90.00`, `$30.00` | PASS |

**Run command:** `node bug4_fixed.js`  
**Sample output:** `Keyboard: $90.00`; `Mouse: $30.00`.  
**Additional checks:** Evaluated the functions in a Node.js `vm` context and checked results and thrown errors.  
**Manual tweaks beyond AI suggestion:** None.

## Bug 5 — `bug5_fixed.c` (C)

**Root cause:** `sizeof(numbers)` inside a function measures the pointer parameter, not the caller's array length.  
**Fix:** Pass `size_t count` to `sum_array()` from `main()` using `sizeof(values) / sizeof(values[0])`. Use `<stddef.h>` for `size_t`.

| Test input | Expected | Actual | Status |
|---|---|---|---|
| Values `{1,2,3,4,5}`, count `5` | `15` | `15` | PASS |
| Values `{2,4,6}`, count `3` | `12` | `12` | PASS |
| Values `{2,4,6}`, count `0` | `0` | `0` | PASS |
| Values `{2,4,6}`, count `1` | `2` | `2` | PASS |
| GCC with strict warnings | No warnings/errors | No warnings/errors | PASS |

**Build and run:** `gcc -std=c11 -Wall -Wextra -Werror -pedantic bug5_fixed.c -o bug5_fixed && ./bug5_fixed`  
**Sample output:** `Sum: 15`.  
**Additional checks:** Compiled a temporary C harness that called `sum_array()` with counts 3, 0, and 1.  
**Manual tweaks beyond AI suggestion:** None.

## Bug 6 — `bug6_fixed.c` (C)

**Root cause:** `username == "admin"` compares pointer addresses, not C-string contents.  
**Fix:** Include `<string.h>` and compare with `strcmp(username, "admin") == 0`.

| Test input | Expected | Actual | Status |
|---|---|---|---|
| `is_admin("admin")` | `1` | `1` | PASS |
| `is_admin("guest")` | `0` | `0` | PASS |
| `is_admin("ADMIN")` | `0` | `0` | PASS |
| Run sample program | `Administrator recognized` | `Administrator recognized` | PASS |
| GCC with strict warnings | No warnings/errors | No warnings/errors | PASS |

**Build and run:** `gcc -std=c11 -Wall -Wextra -Werror -pedantic bug6_fixed.c -o bug6_fixed && ./bug6_fixed`  
**Additional checks:** Compiled a temporary C harness to test `admin`, `guest`, and uppercase `ADMIN`.  
**Manual tweaks beyond AI suggestion:** None.

## Final Summary

| Fixed file | Validation checks | Result |
|---|---:|---|
| `bug1_fixed.py` | 5 | PASS |
| `bug2_fixed.py` | 4 | PASS |
| `bug3_fixed.js` | 4 | PASS |
| `bug4_fixed.js` | 7 | PASS |
| `bug5_fixed.c` | 3 checks + 3 additional cases | PASS |
| `bug6_fixed.c` | 3 checks + 3 additional cases | PASS |

**Total:** 26 validation checks passed out of 26 (the C extra-case groups each count as one harness check, but include three assertions apiece). All six fixed programs execute with the expected sample output. No manual corrections beyond the AI-suggested fixes were necessary. The original buggy files were left untouched.
