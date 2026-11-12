"""Reference tests 15-16."""
from common import (unittest, json, subprocess, sys, REFERENCE_DIR, analyze, parse_line, entry, expected, path)

class LogAnalyzerTests(unittest.TestCase):
    def test_15_status_boundary_values(self):
        records = [entry(status=s) for s in ["100", "399", "400", "599"]]
        self.assertEqual(analyze(records), expected(4, 1, {"100": 1, "399": 1, "400": 1, "599": 1}, 2, 50.0, [path("/home", 4)]))


    def test_16_round_half_up(self):
        records = [entry(status="400")] * 1 + [entry(status="200")] * 31
        self.assertEqual(analyze(records)["error_rate_percent"], 3.13)


