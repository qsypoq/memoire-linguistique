import re
from textblob import TextBlob
from textblob_fr import PatternTagger, PatternAnalyzer
import nltk
import math
from collections import defaultdict
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import treetaggerwrapper
from os import listdir
from os.path import isfile, join

def nlp_pipeline(text):
    text = text.lower()
    text = text.replace('\n', ' ').replace('\r', '')
    text = ' '.join(text.split())
    text = re.sub(r"[A-Za-z\.]*[0-9]+[A-Za-z%°\.]*", "", text)
    text = re.sub(r"(\s\-\s|-$)", "", text)
    text = re.sub(r"[,\!\?\%\(\)\/\"]", "", text)
    text = re.sub(r"\&\S*\s", "", text)
    text = re.sub(r"\&", "", text)
    text = re.sub(r"\+", "", text)
    text = re.sub(r"\#", "", text)
    text = re.sub(r"\$", "", text)
    text = re.sub(r"\£", "", text)
    text = re.sub(r"\%", "", text)
    text = re.sub(r"\:", "", text)
    text = re.sub(r"\@", "", text)
    text = re.sub(r"\-", "", text)
    return text

polarity = []


target = "corpus/gpt/txt"
files = [f for f in listdir(target) if isfile(join(target, f))]

for file in files:
    with open (f"{target}/{file}", "r") as text:
        raw_text = text.read()
        corpus_clean = nlp_pipeline(raw_text)
        polarity.append(TextBlob(corpus_clean,pos_tagger=PatternTagger(),analyzer=PatternAnalyzer()).sentiment[0])

print(polarity)