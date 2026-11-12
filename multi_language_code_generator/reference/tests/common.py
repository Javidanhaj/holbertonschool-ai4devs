"""Common fixtures for reference analyzer tests."""
import json
from pathlib import Path
import subprocess
import sys
import unittest
REFERENCE_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REFERENCE_DIR))
from log_analyzer import analyze, parse_line
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
