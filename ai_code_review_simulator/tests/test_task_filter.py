"""Unit tests for the task-filtering feature."""

import unittest

from task_filter import TaskValidationError, filter_tasks


class FilterTasksTests(unittest.TestCase):
    def setUp(self):
        self.tasks = [
            {"id": 1, "title": "Write report", "status": "todo", "due_date": "2026-11-15"},
            {"id": 2, "title": "Review report", "status": "in_progress", "due_date": "2026-11-16"},
            {"id": 3, "title": "Deploy app", "status": "done", "due_date": None},
            {"id": 4, "title": "Fix REPORT", "status": "todo", "due_date": "2026-11-20"},
        ]

    def ids(self, result):
        return [task["id"] for task in result]

    def test_no_filters_returns_all_in_order(self):
        self.assertEqual(self.ids(filter_tasks(self.tasks)), [1, 2, 3, 4])

    def test_filter_by_status(self):
        self.assertEqual(self.ids(filter_tasks(self.tasks, status="todo")), [1, 4])

    def test_filter_by_due_before_inclusive(self):
        self.assertEqual(self.ids(filter_tasks(self.tasks, due_before="2026-11-16")), [1, 2])

    def test_filter_by_due_after_inclusive(self):
        self.assertEqual(self.ids(filter_tasks(self.tasks, due_after="2026-11-16")), [2, 4])

    def test_date_range(self):
        self.assertEqual(self.ids(filter_tasks(self.tasks, due_after="2026-11-16", due_before="2026-11-20")), [2, 4])

    def test_search_is_case_insensitive(self):
        self.assertEqual(self.ids(filter_tasks(self.tasks, search="report")), [1, 2, 4])

    def test_combined_filters(self):
        self.assertEqual(self.ids(filter_tasks(self.tasks, status="todo", search="report", due_before="2026-11-15")), [1])

    def test_empty_tasks(self):
        self.assertEqual(filter_tasks([]), [])

    def test_undated_tasks_excluded_from_date_filter(self):
        self.assertNotIn(3, self.ids(filter_tasks(self.tasks, due_after="2026-11-01")))

    def test_rejects_bad_status(self):
        with self.assertRaises(TaskValidationError):
            filter_tasks(self.tasks, status="pending")

    def test_rejects_bad_date(self):
        with self.assertRaises(TaskValidationError):
            filter_tasks(self.tasks, due_before="2026-02-30")

    def test_rejects_inverted_range(self):
        with self.assertRaises(TaskValidationError):
            filter_tasks(self.tasks, due_after="2026-11-20", due_before="2026-11-15")

    def test_rejects_invalid_task(self):
        with self.assertRaises(TaskValidationError):
            filter_tasks([{"id": 1, "title": "Oops", "status": "unknown"}])

    def test_does_not_mutate_input(self):
        result = filter_tasks(self.tasks, status="todo")
        result[0]["title"] = "Changed"
        self.assertEqual(self.tasks[0]["title"], "Write report")


if __name__ == "__main__":
    unittest.main()
