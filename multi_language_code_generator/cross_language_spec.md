# Cross-Language Specification — HTTP Access Log Analyzer

## 1. Goal and Algorithm

Implement the same deterministic HTTP access-log analyzer in multiple programming languages. The analyzer reads UTF-8 text containing one request per line, validates each log record, and computes summary statistics. **Do not silently repair malformed records.** The specification is independent of any particular language or framework.

For every valid request, the analyzer must calculate:

1. `total_requests`: number of valid request records.
2. `unique_visitors`: number of distinct visitor IP addresses among valid records.
3. `status_counts`: counts of each HTTP status code found in valid records.
4. `error_requests`: number of valid records whose HTTP status is 400–599.
5. `error_rate_percent`: `error_requests / total_requests * 100`, rounded to **two decimal places**; use `0.0` if there are no valid requests.
6. `top_paths`: up to three request paths, sorted by request count (descending), then path lexicographically (ascending) to break ties.
7. `malformed_lines`: number of nonblank lines that fail parsing or validation.

Blank/whitespace-only lines are skipped and **not** counted as malformed. Invalid records do not contribute to any other metric.

## 2. Input Format

Input is a UTF-8 text file (or equivalent UTF-8 string) with one log record per line. For this exercise, use the **simplified log format** below, not the full Apache Combined Log Format:

```text
TIMESTAMP|IP|METHOD|PATH|STATUS
```

Example:

```text
2026-11-12T10:00:00Z|192.0.2.10|GET|/home|200
```

A record is valid only if all the following conditions hold:

- Exactly five pipe-delimited fields exist; trim surrounding whitespace from each field.
- `TIMESTAMP` matches `YYYY-MM-DDTHH:MM:SSZ`, represents a real UTC calendar date/time, and uses the literal `Z` suffix.
- `IP` is a syntactically valid IPv4 address: four decimal octets, each from 0 to 255, with no leading zeros except the single digit `0`.
- `METHOD` is exactly one of `GET`, `POST`, `PUT`, `PATCH`, `DELETE` (case-sensitive).
- `PATH` starts with `/`, contains no spaces or `|`, and is not empty. Query strings, if present, are considered part of the path for counting (e.g. `/search?q=a` differs from `/search?q=b`).
- `STATUS` is exactly a three-digit decimal integer in the inclusive range 100–599.

Do not impose a time filter. Each valid log line represents one request, even if two lines are identical. Both LF and CRLF newlines are supported. A missing final newline is allowed.

## 3. Output Format

Return exactly one JSON-compatible object with these keys and types:

```json
{
  "total_requests": 4,
  "unique_visitors": 2,
  "status_counts": {"200": 2, "404": 1, "500": 1},
  "error_requests": 2,
  "error_rate_percent": 50.0,
  "top_paths": [
    {"path": "/home", "count": 2},
    {"path": "/missing", "count": 1},
    {"path": "/upload", "count": 1}
  ],
  "malformed_lines": 0
}
```

`status_counts` keys are strings in the JSON representation; serialize them in ascending numeric status order for consistent snapshots. `top_paths` is a list, with zero to three objects, in the ordering defined above. Comparison of test outputs should treat JSON object key order as irrelevant. Numeric `error_rate_percent` is rounded to two decimal places using **round half up** (not language-default banker's rounding).

## 4. Processing Steps (Language-Neutral)

1. Initialize counters and empty sets/maps.
2. Read input line by line; skip blank lines.
3. Split each line on `|` and validate all five fields.
4. For an invalid nonblank line, increment `malformed_lines` and continue.
5. For a valid line, increment `total_requests`, add the IP to the visitor set, increment the corresponding status and path counts, and increment `error_requests` when `400 <= STATUS <= 599`.
6. Compute `unique_visitors`, `error_rate_percent`, and the first three sorted path-frequency pairs.
7. Return the output object as specified.

## 5. Edge Cases

- **Empty input or only blank lines:** all counters are zero, `status_counts` is `{}`, and `top_paths` is `[]`.
- **Malformed lines:** count them, but exclude them from all other metrics.
- **Duplicate requests:** count each line as a separate request; repeated IPs count as one visitor.
- **No errors:** error rate is `0.0`.
- **All errors:** error rate is `100.0`.
- **Tied path frequencies:** sort alphabetically by path.
- **Unexpected method, invalid IP/date/status, missing/extra fields:** mark the whole line malformed.
- **Status 300–399:** valid requests, but not counted as errors.
- **Leading/trailing whitespace around fields:** trimmed before validation.
- **Case-sensitive paths and methods:** `/Home` and `/home` are different paths; `get` is invalid.

## 6. Test Cases

Each input block represents the complete text of a separate test file. Expected JSON shown in compact form; object field order does not matter.

### Test 1 — Normal traffic with errors

**Input** (`log_normal.txt`):

```text
2026-11-12T10:00:00Z|192.0.2.10|GET|/home|200
2026-11-12T10:01:00Z|192.0.2.20|GET|/missing|404
2026-11-12T10:02:00Z|192.0.2.10|GET|/home|200
2026-11-12T10:03:00Z|192.0.2.20|POST|/upload|500
```

**Expected output:**

```json
{"total_requests":4,"unique_visitors":2,"status_counts":{"200":2,"404":1,"500":1},"error_requests":2,"error_rate_percent":50.0,"top_paths":[{"path":"/home","count":2},{"path":"/missing","count":1},{"path":"/upload","count":1}],"malformed_lines":0}
```

### Test 2 — Empty file

**Input** (`log_empty.txt`): empty text.

**Expected output:**

```json
{"total_requests":0,"unique_visitors":0,"status_counts":{},"error_requests":0,"error_rate_percent":0.0,"top_paths":[],"malformed_lines":0}
```

### Test 3 — Invalid records and blank lines

**Input** (`log_malformed.txt`):

```text
2026-11-12T10:00:00Z|192.0.2.1|GET|/ok|200
this is not a log record

2026-11-12T10:01:00Z|999.0.2.1|POST|/bad|201
2026-11-12T10:02:00Z|192.0.2.2|GET|/missing|404
```

**Expected output:**

```json
{"total_requests":2,"unique_visitors":2,"status_counts":{"200":1,"404":1},"error_requests":1,"error_rate_percent":50.0,"top_paths":[{"path":"/missing","count":1},{"path":"/ok","count":1}],"malformed_lines":2}
```

### Test 4 — Duplicate lines, repeated visitor, no errors

**Input** (`log_duplicates.txt`):

```text
2026-11-12T10:00:00Z|203.0.113.7|GET|/a|200
2026-11-12T10:00:00Z|203.0.113.7|GET|/a|200
2026-11-12T10:01:00Z|203.0.113.7|GET|/b|302
```

**Expected output:**

```json
{"total_requests":3,"unique_visitors":1,"status_counts":{"200":2,"302":1},"error_requests":0,"error_rate_percent":0.0,"top_paths":[{"path":"/a","count":2},{"path":"/b","count":1}],"malformed_lines":0}
```

### Test 5 — All errors, tied paths

**Input** (`log_all_errors.txt`):

```text
2026-11-12T10:00:00Z|198.51.100.1|GET|/z|500
2026-11-12T10:01:00Z|198.51.100.2|GET|/a|404
2026-11-12T10:02:00Z|198.51.100.3|POST|/m|403
2026-11-12T10:03:00Z|198.51.100.4|GET|/x|503
```

**Expected output:**

```json
{"total_requests":4,"unique_visitors":4,"status_counts":{"403":1,"404":1,"500":1,"503":1},"error_requests":4,"error_rate_percent":100.0,"top_paths":[{"path":"/a","count":1},{"path":"/m","count":1},{"path":"/x","count":1}],"malformed_lines":0}
```

### Test 6 — Validation and whitespace handling

**Input** (`log_validation.txt`):

```text
 2026-11-12T10:00:00Z | 192.0.2.3 | PATCH | /profile | 204 
2026-02-30T10:00:00Z|192.0.2.3|GET|/bad-date|200
2026-11-12T10:01:00Z|192.0.2.03|GET|/bad-ip|200
2026-11-12T10:02:00Z|192.0.2.3|get|/bad-method|200
2026-11-12T10:03:00Z|192.0.2.3|GET|/bad-status|600
```

**Expected output:**

```json
{"total_requests":1,"unique_visitors":1,"status_counts":{"204":1},"error_requests":0,"error_rate_percent":0.0,"top_paths":[{"path":"/profile","count":1}],"malformed_lines":4}
```

## 7. Acceptance Criteria

- Implementations in different languages accept identical input and produce logically identical output for all six tests.
- Parsing and validation follow the same rules regardless of the programming language.
- Output includes all seven required fields, with consistent types and sorting.
- Empty inputs and malformed records are handled without crashing.
- All supplied test cases pass; add automated tests where possible.
