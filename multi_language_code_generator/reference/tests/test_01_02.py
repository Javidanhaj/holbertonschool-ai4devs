"""Reference tests 01-02."""
from common import (unittest, json, subprocess, sys, REFERENCE_DIR, analyze, parse_line, entry, expected, path)

class LogAnalyzerTests(unittest.TestCase):
    def test_01_spec_normal(self):
        data = "\n".join([
            entry("192.0.2.10", "GET", "/home", "200"),
            entry("192.0.2.20", "GET", "/missing", "404", "2026-11-12T10:01:00Z"),
            entry("192.0.2.10", "GET", "/home", "200", "2026-11-12T10:02:00Z"),
            entry("192.0.2.20", "POST", "/upload", "500", "2026-11-12T10:03:00Z"),
        ])
        self.assertEqual(analyze(data.splitlines()), expected(4, 2, {"200": 2, "404": 1, "500": 1}, 2, 50.0, [path("/home", 2), path("/missing", 1), path("/upload", 1)]))


    def test_02_spec_empty(self):
        self.assertEqual(analyze([]), expected())


