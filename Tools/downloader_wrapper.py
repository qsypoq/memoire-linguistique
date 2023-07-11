#!/usr/bin/python

import os
import time

printed = 0
with open(f"presse/url.txt", 'r') as links:
    for link in links:
        printed = printed +1
        print(f"Downloading item number {printed}: {link}")
        os.system(f'python3 downloader.py {link}')
        time.sleep(5)