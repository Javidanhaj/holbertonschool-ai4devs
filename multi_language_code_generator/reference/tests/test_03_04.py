"""Reference tests 03-04."""
from common import (unittest, json, subprocess, sys, REFERENCE_DIR, analyze, parse_line, entry, expected, path)

class LogAnalyzerTests(unittest.TestCase):
    def test_03_spec_malformed(self):
        data = "\n".join([
            entry("192.0.2.1", "GET", "/ok", "200"),
            "this is not a log record",
            "",
            entry("999.0.2.1", "POST", "/bad", "201", "2026-11-12T10:01:00Z"),
            entry("192.0.2.2", "GET", "/missing", "404", "2026-11-12T10:02:00Z"),
        ])
        self.assertEqual(analyze(data.splitlines()), expected(2, 2, {"200": 1, "404": 1}, 1, 50.0, [path("/missing", 1), path("/ok", 1)], 2))


    def test_04_spec_duplicates(self):
        one = entry("203.0.113.7", "GET", "/a", "200")
        two = entry("203.0.113.7", "GET", "/b", "302", "2026-11-12T10:01:00Z")
        self.assertEqual(analyze([one, one, two]), expected(3, 1, {"200": 2, "302": 1}, 0, 0.0, [path("/a", 2), path("/b", 1)]))


