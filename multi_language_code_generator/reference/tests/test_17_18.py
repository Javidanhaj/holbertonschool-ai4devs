"""Reference tests 17-18."""
from common import (unittest, json, subprocess, sys, REFERENCE_DIR, analyze, parse_line, entry, expected, path)

class LogAnalyzerTests(unittest.TestCase):
    def test_17_multiple_paths_top_three(self):
        records = [entry(path=p) for p in ["/z", "/b", "/a", "/z", "/b", "/a", "/q"]]
        self.assertEqual(analyze(records)["top_paths"], [path("/a", 2), path("/b", 2), path("/z", 2)])


    def test_18_crlf_no_final_newline(self):
        text = entry(path="/first") + "\r\n" + entry(path="/second")
        self.assertEqual(analyze(text.splitlines(keepends=True))["total_requests"], 2)


