# Copilot Productivity Sprint — Benchmark Tasks

## Benchmark Overview

These three independent, beginner-friendly Python tasks are designed to take approximately **15–30 minutes each**. They cover API development, data transformation, and debugging/testing so that different AI coding-assistant capabilities can be evaluated. Use the same requirements and acceptance criteria when completing a task with and without AI assistance.

Record time taken, acceptance criteria passed, number of AI prompts, and any manual corrections for each attempt. The implementation and testing results are **not** part of this task-definition document.

## Task 1 — Create a User Registration Endpoint (API Development)

**Estimated time:** 20–30 minutes  
**Objective:** Implement a minimal REST endpoint with input validation.

**Requirements:**
- Use Python and Flask to implement `POST /users`.
- Accept a JSON request containing `name` and `email` strings.
- Reject missing fields, blank names, and invalid email formats.
- Store valid users in an in-memory list and assign each a unique integer ID, starting at 1.
- Return JSON responses with appropriate HTTP status codes. No database is required.

**Inputs:**
- Valid example: `{"name": "Alex", "email": "alex@example.com"}`
- Invalid example: `{"name": "Alex", "email": "not-an-email"}`

**Outputs:**
- Success (HTTP 201): `{"id": 1, "name": "Alex", "email": "alex@example.com"}`
- Invalid input (HTTP 400): `{"error": "Invalid email"}` (or an equally clear message).

**Acceptance Criteria:**
1. A valid JSON request returns HTTP 201 and the created user's ID, name, and email.
2. Missing/blank names and malformed email addresses return HTTP 400 with a meaningful JSON error.
3. Two valid registrations receive different integer IDs, and the server remains usable afterward.

## Task 2 — Summarize Expenses by Category (Data Processing)

**Estimated time:** 15–25 minutes  
**Objective:** Turn transaction data into a clean, deterministic summary.

**Requirements:**
- Write a Python function `summarize_expenses(transactions)`.
- Each transaction is a dictionary containing `category` (string) and `amount` (number).
- Sum amounts by category, including repeated categories.
- Reject negative amounts by raising `ValueError`.
- Return a dictionary with category names sorted alphabetically and totals rounded to two decimal places.
- Do not modify the input list or its dictionaries.

**Inputs:**
```python
[
    {"category": "Food", "amount": 12.50},
    {"category": "Transport", "amount": 3.00},
    {"category": "Food", "amount": 7.25}
]
```

**Outputs:**
```python
{"Food": 19.75, "Transport": 3.00}
```

**Acceptance Criteria:**
1. Repeated categories are combined correctly, with two-decimal totals and alphabetical key order.
2. An empty input list returns `{}`; negative amounts raise `ValueError`.
3. The original input data remains unchanged after the function runs.

## Task 3 — Debug a Word-Frequency Function (Debugging and Testing)

**Estimated time:** 15–25 minutes  
**Objective:** Fix incorrect counting and add automated tests.

**Requirements:**
- Start with the intentionally flawed function below.
- Make word counting case-insensitive and ignore punctuation.
- Count every occurrence, including the first occurrence of each word.
- Return a dictionary of words and their counts; empty or punctuation-only input returns `{}`.
- Add at least three `pytest` tests covering normal input, repeated mixed-case words, and empty/punctuation-only input.
- Use only Python's standard library for the function itself.

**Starting code (contains bugs):**
```python
def word_frequency(text):
    counts = {}
    for word in text.split():
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 0
    return counts
```

**Inputs:**
- `"Hello, hello world!"`
- `"Python PYTHON python."`
- `"..."`

**Outputs:**
- `{"hello": 2, "world": 1}`
- `{"python": 3}`
- `{}`

**Acceptance Criteria:**
1. The corrected function returns the expected dictionaries for all three example inputs.
2. It handles uppercase letters and punctuation without creating duplicate word entries.
3. At least three automated `pytest` tests pass, including an empty or punctuation-only case.

## Suggested Benchmark Recording Table

| Task | Time without AI (min) | Time with AI (min) | Criteria passed (out of 3) | AI prompts | Manual corrections |
|---|---:|---:|---:|---:|---:|
| 1 — Registration API | — | — | — | — | — |
| 2 — Expense summary | — | — | — | — | — |
| 3 — Word frequency | — | — | — | — | — |

> Fill in this table only after performing the benchmark; do not invent execution results.
