"""Reference tests 07-08."""
from common import (unittest, json, subprocess, sys, REFERENCE_DIR, analyze, parse_line, entry, expected, path)

class LogAnalyzerTests(unittest.TestCase):
    def test_07_only_blank_lines(self):
        self.assertEqual(analyze(["", "  ", "\t", "\r\n"]), expected())


    def test_08_invalid_field_counts(self):
        self.assertEqual(analyze(["a|b|c|d", "a|b|c|d|e|f", "broken"]), expected(malformed=3))


