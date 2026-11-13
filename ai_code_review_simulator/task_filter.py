"""Task filtering utilities for a lightweight project board.

All functions are pure: input task dictionaries are never changed.
Dates use the ISO YYYY-MM-DD format and status is a known task state.
"""

from datetime import date
from typing import Any, Iterable

VALID_STATUSES = frozenset({"todo", "in_progress", "done"})


class TaskValidationError(ValueError):
    """Raised when a task or filter has invalid input."""


def _date(value: str, field_name: str) -> date:
    if not isinstance(value, str):
        raise TaskValidationError(f"{field_name} must be a YYYY-MM-DD string")
    try:
        parsed = date.fromisoformat(value)
    except ValueError as error:
        raise TaskValidationError(f"{field_name} must be a valid YYYY-MM-DD date") from error
    if parsed.isoformat() != value:
        raise TaskValidationError(f"{field_name} must use YYYY-MM-DD format")
    return parsed


def _validated_task(task: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(task, dict):
        raise TaskValidationError("each task must be a dictionary")
    if not isinstance(task.get("id"), int) or isinstance(task["id"], bool):
        raise TaskValidationError("task id must be an integer")
    if not isinstance(task.get("title"), str) or not task["title"].strip():
        raise TaskValidationError("task title must be non-empty")
    if task.get("status") not in VALID_STATUSES:
        raise TaskValidationError("task status must be todo, in_progress, or done")
    due = task.get("due_date")
    if due is not None:
        _date(due, "due_date")
    return task


def filter_tasks(
    tasks: Iterable[dict[str, Any]],
    *,
    status: str | None = None,
    due_before: str | None = None,
    due_after: str | None = None,
    search: str | None = None,
) -> list[dict[str, Any]]:
    """Return tasks matching all supplied filters, retaining input order.

    Date boundaries are inclusive. Tasks without a due date are omitted
    whenever either due-date filter is supplied. Search is case-insensitive.
    """
    if status is not None and status not in VALID_STATUSES:
        raise TaskValidationError("invalid status filter")
    if search is not None and not isinstance(search, str):
        raise TaskValidationError("search must be a string")
    before = _date(due_before, "due_before") if due_before is not None else None
    after = _date(due_after, "due_after") if due_after is not None else None
    if before is not None and after is not None and after > before:
        raise TaskValidationError("due_after cannot be later than due_before")

    matches = []
    for task in tasks:
        _validated_task(task)
        if status is not None and task["status"] != status:
            continue
        if search is not None and search.casefold() not in task["title"].casefold():
            continue
        if before is not None or after is not None:
            if task.get("due_date") is None:
                continue
            due = _date(task["due_date"], "due_date")
            if before is not None and due > before:
                continue
            if after is not None and due < after:
                continue
        matches.append(task.copy())
    return matches
