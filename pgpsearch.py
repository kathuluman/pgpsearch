#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup
from rich.console import Console
from rich.table import Table
import argparse
import concurrent.futures
import re

console = Console()

def fetch_emails(domain, proxy):
    url = f'https://keyserver.ubuntu.com/pks/lookup?search={domain}&fingerprint=on&op=index'
    proxies = {'http': proxy, 'https': proxy} if proxy else None

    try:
        response = requests.get(url, proxies=proxies)
        response.raise_for_status()
    except requests.RequestException as e:
        console.print(f'[bold red]Error: {e}')
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    email_spans = soup.find_all('span', class_='uid')

    matches = [span.get_text() for span in email_spans]
    return matches

def create_table(emails):
    table = Table()
    table.add_column("Name", justify="left", style="cyan")
    table.add_column("Email", justify="left", style="magenta")

    formatted_output = ""
    for email in emails:
        name, email_address = email.split('<')
        formatted_name = f"<{name.strip()}> {email_address.strip('>')}"
        table.add_row(formatted_name, email_address.strip('>'))
        formatted_output += f"{formatted_name}\n"

    return table, formatted_output

def save_emails_to_file(emails, output_file, format_option):
    with open(output_file, 'w') as f:
        if format_option == 'default':
            table, formatted_output = create_table(emails)
            console.print(table)
            f.write(formatted_output)
        elif format_option == 'email':
            table = create_table(emails)[0]
            console.print(table)
            for email in emails:
                _, email_address = email.split('<')
                f.write(f"{email_address.strip('>')}\n")

def main():
    parser = argparse.ArgumentParser(description='PGP Search')
    parser.add_argument('-d', '--domain', type=str, required=True, help='Specify the domain')
    parser.add_argument('-t', '--threads', type=int, default=1, help='Number of threads')
    parser.add_argument('--proxy', type=str, help='Specify proxy in format socks5://127.0.0.1:9050')
    parser.add_argument('-o', '--output', type=str, help='Specify output file')
    parser.add_argument('-f', '--format', choices=['default', 'email'], default='default',
                        help='Specify output format (default or email)')

    args = parser.parse_args()

    domain = args.domain
    threads = args.threads
    proxy = args.proxy

    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        emails = list(executor.map(fetch_emails, [domain] * threads, [proxy] * threads))

    # Flatten the list of lists
    emails = [item for sublist in emails for item in sublist]

    if args.output:
        save_emails_to_file(emails, args.output, args.format)
    else:
        table, _ = create_table(emails)
        console.print(table)

if __name__ == "__main__":
    main()
