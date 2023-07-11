import nltk
import math
from collections import defaultdict
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import treetaggerwrapper
import statistics
import json

target = "corpus/human/to_graph"
target_file = "pun.txt"

source = open(f"{target}/{target_file}", "r")
dump = []

while source:
    line = source.readline()
    if line == "":
        break
    dump.append(float(line))
source.close()

ecarttype = statistics.pstdev(dump)
variance = statistics.variance(dump)
print(f"Ecartype: {ecarttype}")
print(f"Variance: {variance}")
for item in statistics.quantiles(dump, n=10):
    print(item)