"""Reference tests 09-10."""
from common import (unittest, json, subprocess, sys, REFERENCE_DIR, analyze, parse_line, entry, expected, path)

class LogAnalyzerTests(unittest.TestCase):
    def test_09_invalid_ipv4_values(self):
        bad = ["256.0.0.1", "192.0.2.01", "1.2.3", "1.2.3.4.5", "-1.0.0.1", "１２７.0.0.1"]
        self.assertEqual(analyze([entry(ip=value) for value in bad]), expected(malformed=len(bad)))


    def test_10_calendar_validation_and_leap_day(self):
        records = [
            entry(timestamp="2024-02-29T23:59:59Z"),
            entry(timestamp="2025-02-29T10:00:00Z"),
            entry(timestamp="2024-13-01T00:00:00Z"),
            entry(timestamp="2024-12-01T24:00:00Z"),
            entry(timestamp="2024-12-01T00:00:60Z"),
        ]
        self.assertEqual(analyze(records), expected(1, 1, {"200": 1}, 0, 0.0, [path("/home", 1)], 4))


