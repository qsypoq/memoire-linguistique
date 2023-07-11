from operator import contains
import matplotlib.pyplot as plt
import seaborn as sns
import json
import pandas as pd
import math

def combine(dict1, dict2):
    """Updates dict1 to contain dict2"""
    for key in dict2:
        if key in dict1:
            dict1[key] = dict1[key] + dict2[key]
        else: # Creates the values that doesn't exist.
            dict1[key] = dict2[key]
    return dict1

source = open (f"corpus/gpt/to_graph/pun.txt", "r")

to_graph = []
while source:
    line = source.readline()
    if line == "":
        break
    to_graph.append(float(line[0:5]))

ax = sns.histplot(data=to_graph, kde=True, stat="percent")

ax.set(xlabel='Ponctuation - GPT-3.5', ylabel='percent')

plt.savefig('fig.png')