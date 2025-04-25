#!/usr/bin/env python3

import socket
import threading
from queue import Queue
import os

# ┌────────────────────────────────────────────┐
# │               MidnightOps v1.0             │
# │       Subdomain Enumerator by You™️        │
# └────────────────────────────────────────────┘

# Configuration
THREADS = 10
WORDLIST_FILE = "wordlists/subdomains.txt"
OUTPUT_FILE = "output/found_subdomains.txt"
q = Queue()
found_subdomains = []

def banner():
    print(r"""
       .---.
       |---|
       |---|
       |---|
   .---^ - ^---.
   :___________:
      |  |//|
      |  |//|
      |  |//|
      |  |//|
      |  |//|
      |  |//|
      |  |.-|
      |.-'**|
       \***/
        \*/
         V

        '
         ^'
        (_)

    ┌────────────────────────────────────────────┐
    │               MidnightOps v1.0             │
    │       Subdomain Enumerator by devlin™️     │
    └────────────────────────────────────────────┘
    """)

def load_wordlist(domain, wordlist_path):
    try:
        with open(wordlist_path, 'r') as f:
            for line in f:
                sub = line.strip()
                if sub:
                    q.put(f"{sub}.{domain}")
    except FileNotFoundError:
        print(f"[!] Wordlist not found: {wordlist_path}")
        exit(1)

def resolve():
    while not q.empty():
        subdomain = q.get()
        try:
            ip = socket.gethostbyname(subdomain)
            print(f"[+] {subdomain} -> {ip}")
            found_subdomains.append((subdomain, ip))
        except socket.gaierror:
            pass
        q.task_done()

def save_results(path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        for sub, ip in found_subdomains:
            f.write(f"{sub} -> {ip}\n")
    print(f"\n[✓] Results saved to {path}")

def main():
    banner()
    domain = input("[?] Enter target domain (e.g. example.com): ").strip()

    load_wordlist(domain, WORDLIST_FILE)

    print(f"[*] Enumerating subdomains for: {domain}")
    threads = []
    for _ in range(THREADS):
        t = threading.Thread(target=resolve)
        t.start()
        threads.append(t)

    q.join()

    save_results(OUTPUT_FILE)
    print(f"[+] Done. {len(found_subdomains)} subdomains found.")

if __name__ == "__main__":
    main()
