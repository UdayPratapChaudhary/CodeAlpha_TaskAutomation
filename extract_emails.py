"""Task Automation: Extract email addresses from a text file.

Usage:
    python extract_emails.py input.txt
The extracted addresses are saved to emails_found.txt.
"""

import re
import sys
from pathlib import Path

EMAIL_PATTERN = re.compile(
    r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
)


def main():
    if len(sys.argv) > 2:
        print("Usage: python extract_emails.py [input_file.txt]")
        raise SystemExit(1)

    input_path = Path(sys.argv[1]) if len(sys.argv) == 2 else Path("input.txt")
    output_path = Path("emails_found.txt")

    if not input_path.exists() or not input_path.is_file():
        print(f"Error: input file not found: {input_path}")
        print("Create input.txt or provide a path, for example:")
        print("python extract_emails.py input.txt")
        raise SystemExit(1)

    text = input_path.read_text(encoding="utf-8", errors="replace")
    emails = sorted(set(EMAIL_PATTERN.findall(text)), key=str.lower)
    output_path.write_text(
        "\n".join(emails) + ("\n" if emails else ""),
        encoding="utf-8"
    )

    print(f"Done! Found {len(emails)} unique email address(es).")
    print(f"Saved results to: {output_path.resolve()}")


if __name__ == "__main__":
    main()
