# Python Reference Implementation — HTTP Log Analyzer

Implements the simplified pipe-delimited format in `../cross_language_spec.md` (not full Apache logs). Uses only the Python standard library; Python 3.9+ recommended.

## Run

From the repository root:

```bash
python3 multi_language_code_generator/reference/log_analyzer.py logs.txt
# Or read standard input:
cat logs.txt | python3 multi_language_code_generator/reference/log_analyzer.py
```

Output is one JSON object containing all seven required metrics.

## Test

```bash
python3 -m unittest discover -s multi_language_code_generator/reference/tests -v
```

The 20 automated tests include exact outputs for the six cases in the task 0 specification, plus validation, edge cases, rounding, tie breaking, Windows newlines, and CLI behavior.

## Implementation notes

- Invalid nonblank records count toward `malformed_lines` only.
- Invalid IPs, nonexistent calendar dates, invalid statuses, methods and paths are rejected.
- Rounding uses `decimal.ROUND_HALF_UP` rather than default float rounding.
- No network access, third-party packages, or configuration required.
