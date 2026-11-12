"""Automated reference tests, including all six cross_language_spec.md fixtures."""

import json
from pathlib import Path
import subprocess
import sys
import unittest

REFERENCE_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REFERENCE_DIR))
from log_analyzer import analyze, parse_line  # noqa: E402

T = "2026-11-12T10:00:00Z"

def entry(ip="192.0.2.1", method="GET", path="/home", status="200", timestamp=T):
    return f"{timestamp}|{ip}|{method}|{path}|{status}"


def expected(total=0, visitors=0, status_counts=None, errors=0, rate=0.0, paths=None, malformed=0):
    return {
        "total_requests": total,
        "unique_visitors": visitors,
        "status_counts": status_counts if status_counts is not None else {},
        "error_requests": errors,
        "error_rate_percent": rate,
        "top_paths": paths if paths is not None else [],
        "malformed_lines": malformed,
    }


def path(name, count):
    return {"path": name, "count": count}


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

    def test_07_only_blank_lines(self):
        self.assertEqual(analyze(["", "  ", "\t", "\r\n"]), expected())

    def test_08_invalid_field_counts(self):
        self.assertEqual(analyze(["a|b|c|d", "a|b|c|d|e|f", "broken"]), expected(malformed=3))

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

    def test_11_invalid_status_formats(self):
        self.assertEqual(analyze([entry(status=s) for s in ["99", "600", "099", "2O0", "200.0", "+200", "²00"]]), expected(malformed=7))

    def test_12_method_case_sensitive(self):
        records = [entry(method=m) for m in ["get", "HEAD", "OPTIONS", "POST", "PUT", "DELETE"]]
        self.assertEqual(analyze(records), expected(3, 1, {"200": 3}, 0, 0.0, [path("/home", 3)], 3))

    def test_13_path_validation_and_case(self):
        records = [entry(path=p) for p in ["/home", "/Home", "home", "/has space", "/tab\there"]]
        self.assertEqual(analyze(records), expected(2, 1, {"200": 2}, 0, 0.0, [path("/Home", 1), path("/home", 1)], 3))

    def test_14_query_strings_distinct(self):
        records = [entry(path="/search?q=a"), entry(path="/search?q=b"), entry(path="/search?q=a")]
        self.assertEqual(analyze(records), expected(3, 1, {"200": 3}, 0, 0.0, [path("/search?q=a", 2), path("/search?q=b", 1)]))

    def test_15_status_boundary_values(self):
        records = [entry(status=s) for s in ["100", "399", "400", "599"]]
        self.assertEqual(analyze(records), expected(4, 1, {"100": 1, "399": 1, "400": 1, "599": 1}, 2, 50.0, [path("/home", 4)]))

    def test_16_round_half_up(self):
        records = [entry(status="400")] * 1 + [entry(status="200")] * 31
        self.assertEqual(analyze(records)["error_rate_percent"], 3.13)

    def test_17_multiple_paths_top_three(self):
        records = [entry(path=p) for p in ["/z", "/b", "/a", "/z", "/b", "/a", "/q"]]
        self.assertEqual(analyze(records)["top_paths"], [path("/a", 2), path("/b", 2), path("/z", 2)])

    def test_18_crlf_no_final_newline(self):
        text = entry(path="/first") + "\r\n" + entry(path="/second")
        self.assertEqual(analyze(text.splitlines(keepends=True))["total_requests"], 2)

    def test_19_parse_line_raises(self):
        with self.assertRaises(ValueError):
            parse_line("not|a|valid|record")

    def test_20_cli_reads_stdin_and_returns_json(self):
        run = subprocess.run(
            [sys.executable, str(REFERENCE_DIR / "log_analyzer.py")],
            input=entry(), capture_output=True, text=True, check=True,
        )
        self.assertEqual(json.loads(run.stdout), expected(1, 1, {"200": 1}, 0, 0.0, [path("/home", 1)]))


if __name__ == "__main__":
    unittest.main()
