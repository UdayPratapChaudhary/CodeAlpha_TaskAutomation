# CodeAlpha Task Automation: Email Extractor

A small Python automation script that finds email addresses in a text file and saves unique results to a separate file.

## Concepts Used
- `re` for matching email-address patterns
- `pathlib` and file handling for reading/writing text files
- `sys` for accepting an optional input filename from the command line

## Files
- `extract_emails.py` — main script
- `input.txt` — sample input file
- `emails_found.txt` — generated output file (created when the script runs)

## Requirements
Python 3.8 or newer. No third-party packages are required.

## How to Run
Keep `extract_emails.py` and `input.txt` in the same folder, then run:

```bash
python extract_emails.py
```

Or specify another text file:

```bash
python extract_emails.py my_contacts.txt
```

The extracted unique email addresses are saved to `emails_found.txt`.

## Example Output
Using the included sample `input.txt`, the script reports three unique addresses and writes:

```text
alex@example.com
student123@gmail.com
support@codealpha.example
```

Note: `example.com` and `.example` addresses are sample placeholders, not real contact details.

## Author
Uday Pratap Chaudhary
