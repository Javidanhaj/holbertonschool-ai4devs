# Pull Request: Add Task Filtering by Status, Due Date, and Search

## PR Title
Add validated, composable task filters to project board

## Summary
Adds a small Python task-filtering feature for a project-management board. Users can filter tasks by workflow status, an inclusive due-date range, and case-insensitive title search, with all selected filters applied together.

## Context and Motivation
A task board becomes difficult to use as the number of tasks grows. Filtering helps users locate overdue, upcoming, or in-progress work without manually scanning the entire board. This feature is deliberately implemented as a standalone pure function so it can be reviewed, tested, and reused without an API or database dependency.

Related issue: none (self-contained assignment feature).

## Changes
- **`task_filter.py`**: implements `filter_tasks()` with optional `status`, `due_before`, `due_after`, and `search` parameters.
- Validates task records, statuses, dates, and contradictory date ranges; provides clear `TaskValidationError` messages.
- Uses inclusive date boundaries and excludes undated tasks when a date filter is supplied.
- Preserves input order and returns copied task dictionaries rather than mutating the original records.
- **`tests/test_task_filter.py`**: adds 14 `unittest` cases for basic behavior, combined filters, edge cases, invalid inputs, and non-mutation.

## Usage

```python
from task_filter import filter_tasks

tasks = [
    {"id": 1, "title": "Write report", "status": "todo", "due_date": "2026-11-15"},
    {"id": 2, "title": "Deploy app", "status": "done", "due_date": None},
]

upcoming = filter_tasks(tasks, status="todo", due_before="2026-11-16")
assert len(upcoming) == 1
```

## Acceptance Criteria
- Filter by valid statuses `todo`, `in_progress`, and `done`.
- Filter by inclusive `YYYY-MM-DD` due dates and by partial, case-insensitive titles.
- Support combined filters; reject invalid parameters with explicit errors.
- Keep the original input data unchanged.
- All new tests pass; no third-party dependencies required.

## Test Plan
From the `ai_code_review_simulator` directory:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v
```

Tested locally with Python's standard-library `unittest` runner: 14 tests passed.

## Scope and Limitations
This PR implements an in-memory filtering utility, **not** an HTTP endpoint or a deployed web interface. Date values must be ISO dates. The new feature is approximately 70 lines of implementation plus tests, around 140 lines of Python in total. Integration with an existing task storage layer can be added in a later PR.
