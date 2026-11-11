# Fix Validation — AI-Assisted Debugging

**Validation date:** 2026-11-11  
**Test environment:** Python 3.13.5; Node.js 22.16.0; GCC 14.2.0 (C11)  
**Scope:** Six corrected programs in `bug_fixes/`; original flawed snippets in `../bug_snippets/` remain unchanged.

## Exact test procedure

Run from the repository root:

```bash
python3 prompting_debug_assistant/bug_fixes/validate_fixes.py
```

The included `validate_fixes.py` executes the actual corrected programs, calls Python/JavaScript functions with additional inputs, and compiles and executes C programs and temporary C harnesses. For C it uses `gcc -std=c11 -Wall -Wextra -Werror -pedantic`, so a compiler warning makes the test fail. Each case compares an **actual computed result** against an explicit **expected result**, rather than merely printing an expected value. The result below is from executing this test runner.

## Bug 1 — `bug1_fixed.py`

**Original failure (reproduced):** `bug1.py` used `items[-n + 1:]`, so `n=2` returned `[50]` instead of `[40, 50]` and `n=0` returned most of the list.  
**Fix applied:** Special-case `n==0`; otherwise return `items[-n:]`.  
**How tested:** Python function input-output comparisons, including invalid input.

| Test case | Input / command | Expected output | Actual output | Result |
|---|---|---|---|---|
| normal | `last_n([10, 20, 30, 40, 50], 2)` | `[40, 50]` | `[40, 50]` | **PASS** |
| zero | `last_n([10, 20, 30, 40, 50], 0)` | `[]` | `[]` | **PASS** |
| full length | `last_n([10, 20, 30, 40, 50], 5)` | `[10, 20, 30, 40, 50]` | `[10, 20, 30, 40, 50]` | **PASS** |
| too large | `last_n([10, 20, 30, 40, 50], 8)` | `[10, 20, 30, 40, 50]` | `[10, 20, 30, 40, 50]` | **PASS** |
| negative n | `last_n([1,2], -1)` | `ValueError` | `ValueError` | **PASS** |

**Fix confirmation:** **PASS (5/5 tests)** — all observed outputs matched expectations.  
**Manual changes beyond the AI fix:** None.

## Bug 2 — `bug2_fixed.py`

**Original failure (reproduced):** `bug2.py` raised `KeyError: 'price'` when an order lacked that key.  
**Fix applied:** Only add `order["price"]` when `"price" in order`.  
**How tested:** Python function input-output comparisons for missing and empty orders.

| Test case | Input / command | Expected output | Actual output | Result |
|---|---|---|---|---|
| mixed | `calculate_total([{'price': 12}, {'price': 3}, {'item': 'sample'}, {'price': 5}])` | `20` | `20` | **PASS** |
| missing price | `calculate_total([{'item': 'sample'}])` | `0` | `0` | **PASS** |
| empty | `calculate_total([])` | `0` | `0` | **PASS** |
| zero price | `calculate_total([{'price': 0}, {'price': 7}])` | `7` | `7` | **PASS** |

**Fix confirmation:** **PASS (4/4 tests)** — all observed outputs matched expectations.  
**Manual changes beyond the AI fix:** None.

## Bug 3 — `bug3_fixed.js`

**Original failure (reproduced):** **Confirmed syntax error:** original `bug3.js` contained `console.log("Average:", average;` (missing closing `)`). `node --check` reported `SyntaxError: missing ) after argument list`.  
**Fix applied:** Change the line to `console.log("Average:", average);`.  
**How tested:** Node.js function checks plus executed sample program.

| Test case | Input / command | Expected output | Actual output | Result |
|---|---|---|---|---|
| sample | `calculateAverage([70,80,90])` | `80` | `80` | **PASS** |
| empty | `calculateAverage([])` | `0` | `0` | **PASS** |
| two values | `calculateAverage([10,20])` | `15` | `15` | **PASS** |
| main output | `node bug3_fixed.js` | `Average: 80<br>Expected average: 80` | `Average: 80<br>Expected average: 80` | **PASS** |

**Fix confirmation:** **PASS (4/4 tests)** — all observed outputs matched expectations.  
**Manual changes beyond the AI fix:** None.

## Bug 4 — `bug4_fixed.js`

**Original failure (reproduced):** `bug4.js` returned `price * discountRate` (discount *amount*) instead of the discounted price; it printed `$10.00` for both sample items.  
**Fix applied:** Return `price * (1 - discountRate)`; keep rate validation.  
**How tested:** Node.js function checks, invalid rates, and sample output.

| Test case | Input / command | Expected output | Actual output | Result |
|---|---|---|---|---|
| 10% discount | `applyDiscount(100, 0.1)` | `90` | `90` | **PASS** |
| 25% discount | `applyDiscount(40, 0.25)` | `30` | `30` | **PASS** |
| 0% discount | `applyDiscount(100, 0)` | `100` | `100` | **PASS** |
| 100% discount | `applyDiscount(100, 1)` | `0` | `0` | **PASS** |
| negative rate | `applyDiscount(100, -0.1)` | `Error` | `Error` | **PASS** |
| too large rate | `applyDiscount(100, 1.1)` | `Error` | `Error` | **PASS** |
| main output | `node bug4_fixed.js` | `Keyboard: $90.00<br>Mouse: $30.00<br>Expected final prices: $90.00 and $30.00` | `Keyboard: $90.00<br>Mouse: $30.00<br>Expected final prices: $90.00 and $30.00` | **PASS** |

**Fix confirmation:** **PASS (7/7 tests)** — all observed outputs matched expectations.  
**Manual changes beyond the AI fix:** None.

## Bug 5 — `bug5_fixed.c`

**Original failure (reproduced):** Original `bug5.c` used `sizeof(numbers)` on an array parameter (actually a pointer inside the function). GCC warned and the original program printed `Sum: 3`, not `15`.  
**Fix applied:** Pass element count explicitly as `size_t count`; iterate `i < count`.  
**How tested:** GCC strict compilation, actual sample execution, and a temporary C function-call harness.

| Test case | Input / command | Expected output | Actual output | Result |
|---|---|---|---|---|
| main output (strict build) | `gcc -Werror && execute` | `Sum: 15<br>Expected sum: 15` | `Sum: 15<br>Expected sum: 15` | **PASS** |
| three values | `{2,4,6}, count=3` | `12` | `12` | **PASS** |
| zero count | `{2,4,6}, count=0` | `0` | `0` | **PASS** |
| one value | `{2,4,6}, count=1` | `2` | `2` | **PASS** |

**Fix confirmation:** **PASS (4/4 tests)** — all observed outputs matched expectations.  
**Manual changes beyond the AI fix:** None.

## Bug 6 — `bug6_fixed.c`

**Original failure (reproduced):** Original `bug6.c` compared strings with `==` (pointer addresses), printed `Regular user`, and triggered a GCC warning.  
**Fix applied:** Use `strcmp(username, "admin") == 0` and include `<string.h>`.  
**How tested:** GCC strict compilation, sample execution, and a temporary C function-call harness.

| Test case | Input / command | Expected output | Actual output | Result |
|---|---|---|---|---|
| main output (strict build) | `gcc -Werror && execute` | `Administrator recognized<br>Expected: Administrator recognized` | `Administrator recognized<br>Expected: Administrator recognized` | **PASS** |
| correct username | `"admin"` | `1` | `1` | **PASS** |
| other username | `"guest"` | `0` | `0` | **PASS** |
| case-sensitive | `"ADMIN"` | `0` | `0` | **PASS** |

**Fix confirmation:** **PASS (4/4 tests)** — all observed outputs matched expectations.  
**Manual changes beyond the AI fix:** None.

## Overall Results

| Fixed file | Test cases | Passed | Failed |
|---|---:|---:|---:|
| `bug1_fixed.py` | 5 | 5 | 0 |
| `bug2_fixed.py` | 4 | 4 | 0 |
| `bug3_fixed.js` | 4 | 4 | 0 |
| `bug4_fixed.js` | 7 | 7 | 0 |
| `bug5_fixed.c` | 4 | 4 | 0 |
| `bug6_fixed.c` | 4 | 4 | 0 |

**Total: 28/28 PASS; 0 failures.** All six fixed files execute successfully. No alternative fixes were proposed for this task; no extra manual code changes were needed.

The original `bug3.js` is intentionally syntactically invalid, but the corrected `bug3_fixed.js` runs without syntax errors. This difference is confirmed by `node --check` on the original and by executing the corrected script.
