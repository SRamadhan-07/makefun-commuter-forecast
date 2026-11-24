#!/usr/bin/env python3
"""Charm the Commuter: Forecast a City That Isn't — entry program.

Writes one line to /output/entry.txt: a weather forecast for New
Boredom, a city that does not exist, where the lows are measured in
eye contact and small talk is expected on the 8:15. One line of
UTF-8 text inside the gate of 1 to 140 characters, with no trailing
newline.
"""

import os
from pathlib import Path

FORECAST = (
    "New Boredom: highs of 21°, lows of eye contact. Expect scattered "
    "small talk on the 8:15, easing by the office."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    entry_file = out_dir / "entry.txt"
    # No trailing newline is appended, so the forecast's characters
    # are the whole file the sealed scorer measures.
    entry_file.write_text(FORECAST, encoding="utf-8")


if __name__ == "__main__":
    main()
