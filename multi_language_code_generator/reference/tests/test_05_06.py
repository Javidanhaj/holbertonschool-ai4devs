"""Reference tests 05-06."""
from common import (unittest, json, subprocess, sys, REFERENCE_DIR, analyze, parse_line, entry, expected, path)

class LogAnalyzerTests(unittest.TestCase):
    def test_05_spec_all_errors_tied(self):
        data = [
            entry("198.51.100.1", "GET", "/z", "500"),
            entry("198.51.100.2", "GET", "/a", "404", "2026-11-12T10:01:00Z"),
            entry("198.51.100.3", "POST", "/m", "403", "2026-11-12T10:02:00Z"),
            entry("198.51.100.4", "GET", "/x", "503", "2026-11-12T10:03:00Z"),
        ]
        self.assertEqual(analyze(data), expected(4, 4, {"403": 1, "404": 1, "500": 1, "503": 1}, 4, 100.0, [path("/a", 1), path("/m", 1), path("/x", 1)]))


    def test_06_spec_validation(self):
        data = [
            " 2026-11-12T10:00:00Z | 192.0.2.3 | PATCH | /profile | 204 ",
            entry("192.0.2.3", "GET", "/bad-date", "200", "2026-02-30T10:00:00Z"),
            entry("192.0.2.03", "GET", "/bad-ip", "200", "2026-11-12T10:01:00Z"),
            entry("192.0.2.3", "get", "/bad-method", "200", "2026-11-12T10:02:00Z"),
            entry("192.0.2.3", "GET", "/bad-status", "600", "2026-11-12T10:03:00Z"),
        ]
        self.assertEqual(analyze(data), expected(1, 1, {"204": 1}, 0, 0.0, [path("/profile", 1)], 4))


