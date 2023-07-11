#!/usr/bin/python

import os
import time
import numpy as np

with open(f"gpt/themes.txt", 'r') as themes:
    data = themes.read()
    data = data.split("\n")
    chunked = np.array_split(data, 50)
    for chunk in chunked:
        for theme in chunk:
            os.system(f'sudo python3.9 askgpt.py {theme} &')
            print(f"Asked {theme}")
        time.sleep(90)