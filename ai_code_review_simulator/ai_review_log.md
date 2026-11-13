# AI Review Log — Task Filtering Pull Request

## Review scope and method

- **PR title:** Add Task Filtering by Status, Due Date, and Search
- **Files reviewed:** `task_filter.py`, `tests/test_task_filter.py`, and `pr_description.md` from Task 0.
- **Review approach:** AI-assisted local source review using three personas: security/correctness, performance, and maintainability. These are proposed review comments for the pull request, **not comments actually posted by a GitHub bot**.
- **Review date:** 2026-11-13.
- **Baseline validation:** `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v` — **14 tests passed** locally. Two additional manual probes confirmed that an unhashable `status` value can raise `TypeError` instead of `TaskValidationError`.

## Inline comments

### Comment 1 — Incorrect exception for invalid filter types
- **Location:** `task_filter.py:57`
- **Persona:** Security / input validation
- **Severity:** Medium
- **Finding:** `status not in VALID_STATUSES` attempts set membership without first checking its type. `filter_tasks([], status=[])` raises `TypeError: unhashable type: 'list'`, not the documented `TaskValidationError`.
- **Suggestion:** Validate `isinstance(status, str)` (and allow `None`) before membership testing. Add a regression test for list, dict, and numeric values.

### Comment 2 — Same unchecked hashability in task validation
- **Location:** `task_filter.py:36`
- **Persona:** Security / input validation
- **Severity:** Medium
- **Finding:** The task-level `status` check also raises `TypeError` for unhashable values such as `[]`, bypassing the intended validation error contract.
- **Suggestion:** Reject non-string status values with `TaskValidationError` before checking `VALID_STATUSES`.

### Comment 3 — Invalid iterable type is not rejected clearly
- **Location:** `task_filter.py:67`
- **Persona:** Maintainability
- **Severity:** Low
- **Finding:** `tasks=None` fails with a raw `TypeError` when iteration starts. A dictionary passed as `tasks` iterates over its keys, producing an error message about individual tasks rather than the collection.
- **Suggestion:** Document accepted iterable types and optionally validate the outer argument to produce a consistent, actionable error.

### Comment 4 — Partial validation of lazy inputs
- **Location:** `task_filter.py:67-81`
- **Persona:** Security / correctness
- **Severity:** Medium
- **Finding:** An iterator that raises halfway through processing causes the whole call to fail after earlier work. This is expected for streaming iterables, but behavior is not documented and may surprise callers expecting full input validation up front.
- **Suggestion:** Clarify that evaluation consumes iterables, including generators; consider accepting a concrete sequence if repeatability is required. Add a generator-input test.

### Comment 5 — Case folding performed for every task
- **Location:** `task_filter.py:71`
- **Persona:** Performance
- **Severity:** Low
- **Finding:** `search.casefold()` is calculated on every iteration even though `search` is constant across the request.
- **Suggestion:** Compute `normalized_search = search.casefold()` once before looping. Keep `task['title'].casefold()` per task.

### Comment 6 — Date parsed twice for matched tasks
- **Location:** `task_filter.py:38-40` and `task_filter.py:73-76`
- **Persona:** Performance
- **Severity:** Low
- **Finding:** When date filters are present, `_validated_task` validates a due date and the filtering loop parses the same date again.
- **Suggestion:** Return a parsed date from validation, or validate and filter in one pass; preserve the current non-mutation behavior.

### Comment 7 — Shallow copy may not meet future immutability expectations
- **Location:** `task_filter.py:81`
- **Persona:** Maintainability
- **Severity:** Low
- **Finding:** `task.copy()` protects the top-level dictionary, but nested mutable fields introduced later (e.g. `metadata` or `tags`) would remain shared with the original.
- **Suggestion:** Explicitly document shallow-copy semantics; use deep-copy only if the public contract requires isolation of nested objects.

### Comment 8 — No handling for whitespace-only search terms
- **Location:** `task_filter.py:59-60,71`
- **Persona:** Maintainability / UX
- **Severity:** Low
- **Finding:** `search='   '` is technically valid but likely returns no results even when the user intended an empty search. `search=''` instead matches every title.
- **Suggestion:** Decide whether search terms should be stripped, rejected, or preserved literally, then document the chosen behavior and add tests.

### Comment 9 — Identifier validation accepts negative integers
- **Location:** `task_filter.py:32-33`
- **Persona:** Security / data correctness
- **Severity:** Low
- **Finding:** Any non-boolean integer is accepted as `id`, including negative values. This may be fine for the current in-memory utility, but it could violate a task-board data model using positive identifiers.
- **Suggestion:** Confirm the domain requirement before adding positive-only validation; add a corresponding test if positivity is required.

### Comment 10 — Error path lacks invalid-type regression cases
- **Location:** `tests/test_task_filter.py:47-61`
- **Persona:** Security / testing
- **Severity:** Medium
- **Finding:** Tests cover unknown status strings and invalid dates but not unhashable status inputs, malformed outer collections, or non-string titles. The first two comments expose a real gap.
- **Suggestion:** Add parameterized/subtests for wrong-type inputs and assert that callers receive `TaskValidationError` consistently where specified.

### Comment 11 — No direct test for original order after combined filtering
- **Location:** `tests/test_task_filter.py:38-39`
- **Persona:** Maintainability / testing
- **Severity:** Low
- **Finding:** Existing tests establish ordering with no filters, but do not specifically assert order preservation on a multi-match combined-filter result.
- **Suggestion:** Add a test with several matching tasks in deliberately non-sorted input order.

### Comment 12 — Consider a defined bound for large collections
- **Location:** `task_filter.py:66-82`
- **Persona:** Performance
- **Severity:** Low
- **Finding:** The function scans all tasks in memory and creates a result list. This is appropriate for an MVP but could be costly if used to filter very large back-end datasets.
- **Suggestion:** Keep the simple approach for the current scope; if integrated with a database later, push predicates into the database query and paginate results. This is a scaling consideration, not a current bug.

## Global review suggestions

1. **Security/correctness — fix consistent error handling first.** Ensure invalid status types always raise `TaskValidationError`; verify both filter parameters and task records. This is the most concrete defect discovered.
2. **Performance — avoid unnecessary repeated operations.** Precompute the normalized search text and prevent double date parsing; profile before attempting larger optimizations.
3. **Maintainability — document interface contracts.** Explicitly define accepted task collections, shallow-copy semantics, literal/trimmed search behavior, inclusive date limits, and what happens with undated tasks.
4. **Testing — expand negative and boundary coverage.** Add wrong-type tests, empty/whitespace searches, generator input, nested mutable values, and order preservation for multiple matches.
5. **Architecture — maintain current scope.** A pure in-memory utility with no third-party dependencies is suitable for this PR; avoid introducing a database, endpoint, or additional framework just to satisfy speculative future needs.

## Suggested review decision

**Request changes (minor):** Fix comments 1 and 2 and add regression tests before merge. Other comments are non-blocking improvements or documented trade-offs.

## Reproduction and baseline commands

Run from `ai_code_review_simulator/`:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v
python3 - <<'PY'
from task_filter import filter_tasks
try:
    filter_tasks([], status=[])
except Exception as error:
    print(type(error).__name__, str(error))
PY
```

**Observed locally:** 14 tests pass; the second command prints `TypeError unhashable type: 'list'`. This review did not post comments on GitHub, and it did not modify the feature implementation.
