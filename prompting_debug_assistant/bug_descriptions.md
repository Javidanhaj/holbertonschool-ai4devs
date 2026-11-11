# Bug Descriptions

These six intentionally flawed snippets are for practicing AI-assisted debugging. Each sample is between 10 and 40 lines. The expected behavior is stated so that the actual output can be compared against the goal. The code files are intentionally **not corrected**.

## Bug 1 – `bug_snippets/bug1.py`
- **Language:** Python
- **Intended Behavior:** Return the last `n` elements of a list, preserving order. Return an empty list when `n` is zero and the whole list when `n` is greater than its length.
- **Issue Type:** Off-by-one / slicing logic.
- **Notes:** Check the output for `n = 2` and `n = 0` against the expected results shown in the program.

## Bug 2 – `bug_snippets/bug2.py`
- **Language:** Python
- **Intended Behavior:** Calculate the sum of numeric prices in a list of order dictionaries. Orders without a `price` should be skipped.
- **Issue Type:** Runtime exception / missing dictionary key.
- **Notes:** One sample order does not include a `price`. The expected sum is 20.

## Bug 3 – `bug_snippets/bug3.js`
- **Language:** JavaScript
- **Intended Behavior:** Calculate the arithmetic average of an array of scores and print the result. Return zero for an empty array.
- **Issue Type:** Syntax error.
- **Notes:** The sample scores are 70, 80, and 90, so the expected average is 80. The program fails before it can run.

## Bug 4 – `bug_snippets/bug4.js`
- **Language:** JavaScript
- **Intended Behavior:** Calculate the final price of an item after applying a percentage discount. For example, a 10% discount on $100 should result in $90.
- **Issue Type:** Logical / arithmetic error.
- **Notes:** The program executes, but the final prices do not match the expected $90 and $30.

## Bug 5 – `bug_snippets/bug5.c`
- **Language:** C
- **Intended Behavior:** Sum all numbers in a provided integer array. For `{1, 2, 3, 4, 5}`, the result should be 15.
- **Issue Type:** Misuse of `sizeof` on an array parameter.
- **Notes:** The array parameter behaves as a pointer inside the function; the compiler may warn about `sizeof`. The program may compute an incomplete sum, depending on the platform.

## Bug 6 – `bug_snippets/bug6.c`
- **Language:** C
- **Intended Behavior:** Detect whether the supplied username has the text `admin` and print "Administrator recognized".
- **Issue Type:** Data type misuse / string comparison.
- **Notes:** The input is a character array containing `admin`, yet the program checks the wrong kind of equality and prints "Regular user".
