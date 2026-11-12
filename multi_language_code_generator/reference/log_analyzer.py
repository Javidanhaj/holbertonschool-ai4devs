"""Reference implementation of the simplified HTTP access-log specification.

Each nonblank record is TIMESTAMP|IP|METHOD|PATH|STATUS.
Run: python3 reference/log_analyzer.py path/to/log.txt
Or:  cat log.txt | python3 reference/log_analyzer.py
"""

from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime
from decimal import Decimal, ROUND_HALF_UP
import ipaddress
import json
import re
import sys
from typing import Iterable


_TIMESTAMP_PATTERN = re.compile(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z\Z", re.ASCII)
_IP_PATTERN = re.compile(r"(?:0|[1-9][0-9]{0,2})(?:\.(?:0|[1-9][0-9]{0,2})){3}\Z", re.ASCII)
_STATUS_PATTERN = re.compile(r"[0-9]{3}\Z", re.ASCII)
_METHODS = frozenset({"GET", "POST", "PUT", "PATCH", "DELETE"})


def parse_line(line: str) -> dict[str, str | int]:
    """Parse one record, raising ValueError if any field is invalid."""
    parts = [field.strip() for field in line.split("|")]
    if len(parts) != 5:
        raise ValueError("expected exactly five pipe-separated fields")
    timestamp, ip, method, path, raw_status = parts

    if not _TIMESTAMP_PATTERN.fullmatch(timestamp):
        raise ValueError("invalid timestamp format")
    try:
        datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%SZ")
    except ValueError as exc:
        raise ValueError("invalid UTC date or time") from exc

    if not _IP_PATTERN.fullmatch(ip):
        raise ValueError("invalid IPv4 syntax")
    try:
        ipaddress.IPv4Address(ip)
    except ipaddress.AddressValueError as exc:
        raise ValueError("IPv4 octet out of range") from exc

    if method not in _METHODS:
        raise ValueError("unsupported HTTP method")
    if not path.startswith("/") or any(char.isspace() for char in path) or "|" in path:
        raise ValueError("invalid request path")
    if not _STATUS_PATTERN.fullmatch(raw_status):
        raise ValueError("invalid HTTP status syntax")
    status = int(raw_status)
    if not 100 <= status <= 599:
        raise ValueError("HTTP status out of range")

    return {"timestamp": timestamp, "ip": ip, "method": method, "path": path, "status": status}


def analyze(lines: Iterable[str]) -> dict:
    """Analyze log records and return the seven documented JSON-compatible fields."""
    total_requests = 0
    visitors: set[str] = set()
    statuses: Counter[int] = Counter()
    paths: Counter[str] = Counter()
    error_requests = 0
    malformed_lines = 0

    for line in lines:
        if not line.strip():
            continue
        try:
            record = parse_line(line)
        except ValueError:
            malformed_lines += 1
            continue

        total_requests += 1
        visitors.add(record["ip"])
        statuses[record["status"]] += 1
        paths[record["path"]] += 1
        if 400 <= record["status"] <= 599:
            error_requests += 1

    rate = (
        float((Decimal(error_requests) * 100 / Decimal(total_requests)).quantize(
            Decimal("0.01"), rounding=ROUND_HALF_UP
        ))
        if total_requests
        else 0.0
    )
    return {
        "total_requests": total_requests,
        "unique_visitors": len(visitors),
        "status_counts": {str(code): statuses[code] for code in sorted(statuses)},
        "error_requests": error_requests,
        "error_rate_percent": rate,
        "top_paths": [
            {"path": path, "count": count}
            for path, count in sorted(paths.items(), key=lambda item: (-item[1], item[0]))[:3]
        ],
        "malformed_lines": malformed_lines,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Analyze simplified HTTP access logs")
    parser.add_argument("file", nargs="?", help="UTF-8 log file; omit to read stdin")
    args = parser.parse_args(argv)
    try:
        if args.file:
            with open(args.file, "r", encoding="utf-8", newline=None) as input_file:
                result = analyze(input_file)
        else:
            result = analyze(sys.stdin)
    except (OSError, UnicodeError) as exc:
        print(f"Could not read log input: {exc}", file=sys.stderr)
        return 1

    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
