#!/usr/bin/env python3
import sys


def print_banner():
    banner = """
    \033[36m___               _          ______ ____
   /   |  ___  ____ _(_)____    / ____//  _/
  / /| | / _ \\/ __ `/ / ___/___/ /     / /
 / ___ |/  __/ /_/ / (__  )___/ /___ _/ /
/_/  |_|\\___/\\__, /_/____/    \\____//___/
            /____/
    \033[0m
    \033[1;32m[+] Aegis-CI Security System Active\033[0m
    \033[36m   By Marshall Christ\033[0m
    """
    print(banner)

if __name__ == "__main__":
    print_banner()
    sys.exit(0)
