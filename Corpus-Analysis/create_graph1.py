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

source = open (f"corpus/gpt/to_graph/density.txt", "r")
output = {}
i = 0
while source:
    i = i + 1
    line = source.readline()
    if line == "":
        break
    test = json.loads(line)
    ouput = combine(output,test)
source.close()

for item in output:
    i = i + output[item]
    output[item] = output[item]/3305.36

new_data = {}
for key, value in output.items():
    if key[0:3] in new_data:
        new_data[key[0:3]] = new_data[key[0:3]] + math.floor(output[key])
    else:
        new_data[key[0:3]] = math.ceil(value)

ordered = dict(sorted(new_data.items(), key=lambda item: item[1], reverse=True))
print(ordered)
pdf = pd.DataFrame.from_dict(ordered, orient='index')
pdf['percent'] = pdf[0]

sns.set(font_scale=0.8)

ax = sns.histplot(data=pdf, kde=True, x=pdf.index, y="percent")
ax.set_ylim(0,30)

ax.set_ylabel("Pourcentage")
plt.savefig('fig.png')