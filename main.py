#!/usr/bin/env python3
"""The Painfully Honest Out-of-Office.

Writes a single brutally honest but still polite out-of-office
auto-reply to /output/entry.txt. Deterministic: the same bytes
every run. No dependencies, no network access.
"""

import os

ENTRY = (
    "I'm away until Monday, and honestly your email joins the 214 "
    "messages I've been avoiding since Tuesday, so please resend it "
    "then, because I plan to return pretending this inbox never existed."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
