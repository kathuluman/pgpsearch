# pgpsearch
PGPSearch is a Python-based command-line tool for fetching and listing PGP email addresses associated with a specific domain. It queries the Ubuntu keyserver and extracts email information, making it easy to view and save the results.

![pgpseaerch](https://img.shields.io/github/license/kathuluman/pgpsearch?color=blue&style=for-the-badge) 
![Version](https://img.shields.io/github/v/tag/kathuluman/pgpsearch?color=blue&style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)
![Version](https://img.shields.io/badge/version-1.5.0-green?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green)
![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-orange)

## Features

- Fetch PGP emails associated with a domain.
- Supports multi-threaded execution for faster processing.
- Output in both human-readable and email-only formats.
- Proxy support for enhanced privacy.

## Requirements

- Python 3.7+
- Required Python packages listed in [requirements.txt](#installation).

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/kathuluman/pgpsearch.git
   cd pgpsearch
   ```

2. Install the dependencies
   ```bash
   pip install -r requirements.txt
   ```

## Usage

   ```bash
   python3 pgpsearch.py -d <domain> [-t <threads>] [--proxy <proxy>] [-o <output_file>] [-f <format>]
   ```

## Arguments
- `-d, --domain` (required): The domain to search for PGP emails.
- `-t, --threads`: Number of threads to use (default: 1).
- `--proxy`: Proxy server to use (e.g., socks5://127.0.0.1:9050).
- `-o, --output`: Output file to save the results.
- `-f, --format`: Output format (default or email).

## Example
Fetch emails associated with example.com using 5 threads and save them to `emails.txt` in email-only format:
   ```bash
   python3 pgpsearch.py -d example.com -t 5 -o emails.txt -f email
   ```
## Output Formats

  - default: Outputs the PGP emails with names in a tabular format.
  - email: Outputs only the email addresses.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue to discuss changes.

