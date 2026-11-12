"""Reference tests 11-12."""
from common import (unittest, json, subprocess, sys, REFERENCE_DIR, analyze, parse_line, entry, expected, path)

class LogAnalyzerTests(unittest.TestCase):
    def test_11_invalid_status_formats(self):
        self.assertEqual(analyze([entry(status=s) for s in ["99", "600", "099", "2O0", "200.0", "+200", "²00"]]), expected(malformed=7))


    def test_12_method_case_sensitive(self):
        records = [entry(method=m) for m in ["get", "HEAD", "OPTIONS", "POST", "PUT", "DELETE"]]
        self.assertEqual(analyze(records), expected(3, 1, {"200": 3}, 0, 0.0, [path("/home", 3)], 3))


