"""Reference tests 19-20."""
from common import (unittest, json, subprocess, sys, REFERENCE_DIR, analyze, parse_line, entry, expected, path)

class LogAnalyzerTests(unittest.TestCase):
    def test_19_parse_line_raises(self):
        with self.assertRaises(ValueError):
            parse_line("not|a|valid|record")


    def test_20_cli_reads_stdin_and_returns_json(self):
        run = subprocess.run(
            [sys.executable, str(REFERENCE_DIR / "log_analyzer.py")],
            input=entry(), capture_output=True, text=True, check=True,
        )
        self.assertEqual(json.loads(run.stdout), expected(1, 1, {"200": 1}, 0, 0.0, [path("/home", 1)]))


