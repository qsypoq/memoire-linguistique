import nltk
import math
from collections import defaultdict
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import treetaggerwrapper
from os import listdir
from os.path import isfile, join
import re
def tag_tokens(tokenized_words):
    return nltk.pos_tag(tokenized_words)

def count_tokens(tokenized_sentences):
    tokenized_text = nltk.word_tokenize(tokenized_sentences, language="french")
    return math.ceil(len(tokenized_text))

def average_words_sentences(tokenized_sentences):
    count = []
    for sentence in tokenized_sentences:
        count.append(count_tokens(sentence))
    total = 0
    for item in count:
        total = total + item
    return math.ceil(total/len(tokenized_sentences))

def get_diversity(text):
    return len(set(text))/len(text)

def get_tagstats(text):
    tagger = treetaggerwrapper.TreeTagger(TAGLANG='fr', TAGDIR="treetagger")
    tags = tagger.tag_text(text)
    tags2 = treetaggerwrapper.make_tags(tags)
    count = defaultdict(dict)
    for item in tags2:
        try:
            count[item[1]] = count[item[1]] + 1
        except:
            try:
                count[item[1]] = 1
            except:
                pass
    total = [(k,v) for k,v in count.items()]
    return total

def addtolist(item, target):
    with open(f"{target}", 'a+') as outfile:
            outfile.write(f"{item}\n")

target = "corpus/presse/"
files = [f for f in listdir(target) if isfile(join(target, f))]

for file in files:
    with open (f"{target}/{file}", "r") as text:
        raw_text = text.read()
        tokenized_sentences = nltk.sent_tokenize(raw_text, language="french")
        tokenized_words = nltk.word_tokenize(raw_text, language="french")

        average_words_by_sentence = average_words_sentences(tokenized_sentences)
        diversity = get_diversity(tokenized_words)
        density = get_tagstats(raw_text)

        addtolist(average_words_by_sentence, f"{target}/average_words_by_sentence.txt")
        addtolist(diversity, f"{target}/diversity.txt")
        addtolist(density, f"{target}/density.txt")
