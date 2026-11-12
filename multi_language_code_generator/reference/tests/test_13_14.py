"""Reference tests 13-14."""
from common import (unittest, json, subprocess, sys, REFERENCE_DIR, analyze, parse_line, entry, expected, path)

class LogAnalyzerTests(unittest.TestCase):
    def test_13_path_validation_and_case(self):
        records = [entry(path=p) for p in ["/home", "/Home", "home", "/has space", "/tab\there"]]
        self.assertEqual(analyze(records), expected(2, 1, {"200": 2}, 0, 0.0, [path("/Home", 1), path("/home", 1)], 3))


    def test_14_query_strings_distinct(self):
        records = [entry(path="/search?q=a"), entry(path="/search?q=b"), entry(path="/search?q=a")]
        self.assertEqual(analyze(records), expected(3, 1, {"200": 3}, 0, 0.0, [path("/search?q=a", 2), path("/search?q=b", 1)]))


