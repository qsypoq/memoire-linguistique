from array import array
from webbrowser import get
from flask import Flask, request, render_template
import nltk
import math
import re
from textblob import TextBlob
from textblob_fr import PatternTagger, PatternAnalyzer
from threshold import *
import treetaggerwrapper
from collections import defaultdict
import json

# Flask constructor
app = Flask(__name__)  

@app.context_processor
def utility_processor():

    def clean_txt(text):
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

    def get_sentiment(text):
        return TextBlob(text,pos_tagger=PatternTagger(),analyzer=PatternAnalyzer()).sentiment[0]

    def get_stat(value, stat):
        value = float(value)
        stat_percent = array('i', [0,0])
        for item in stat:
            if value > stat[item]:
                stat_percent[0] = int(item)
            if stat_percent[0] > 50:
                stat_percent[1] = 100 - stat_percent[0]
            else:
                stat_percent[1] = stat_percent[0]
        return stat_percent

    def check_human(value_human, value_ia, sentiment=False, sentiment_value=0):
        if value_human[1] > value_ia[1]:
            return True
        elif value_human[1] == value_ia[1]:
            if value_human[0] < 20:
                if sentiment:
                    return True
                else:
                    return False
            elif value_human[0] > 80:
                if sentiment:
                    if sentiment_value >= 0.3:
                        return True
                    else:
                        return False
                return True
            else:
                return True
        else:
            return False

    def count_tokens(tokenized_sentences):
        tokenized_text = nltk.word_tokenize(tokenized_sentences, language="french")
        return math.ceil(len(tokenized_text))

    def pun(text):
        print(text)
        tagger = treetaggerwrapper.TreeTagger(TAGLANG='fr', TAGDIR="treetagger")
        tags = tagger.tag_text(text)
        tags2 = treetaggerwrapper.make_tags(tags)
        count = defaultdict(dict)
        for item in tags2:
            try:
                count[item[1][:3]] = count[item[1][:3]] + 1
            except:
                try:
                    count[item[1][:3]] = 1
                except:
                    pass
        load = [(k,v) for k,v in count.items()]
        total = 0
        pun = 0
        print(load)
        for sousitem in load:
            stred = str(sousitem)
            tokentype = stred[2:5]
            tokennumber = stred[-3:]
            tokennumber = tokennumber[:-1]
            print(f"{tokentype}:{tokennumber}")
            total = total + int(tokennumber)
            if tokentype == "PUN":
                pun = pun + int(tokennumber)
        percent = math.ceil(100 * float(pun)/float(total))
        print(f"Total: {total} | Percent: {percent}")
        return percent

    def diversity(text):
        return len(set(text))/len(text)

    def average_words_sentences(tokenized_sentences):
        count = []
        for sentence in tokenized_sentences:
            count.append(count_tokens(sentence))
        total = 0
        for item in count:
            total = total + item
        return math.ceil(total/len(tokenized_sentences))

    return dict(average_words_sentences=average_words_sentences, diversity=diversity,
                get_stat=get_stat, check_human=check_human, get_sentiment=get_sentiment, clean_txt=clean_txt, pun=pun)

@app.route('/', methods =["GET", "POST"])
def render():
    if request.method == "POST":
        user_text = request.form.get("user_text")
        tokenized_sentences = nltk.sent_tokenize(user_text, language="french")
        tokenized_words = nltk.word_tokenize(user_text, language="french")

        return render_template("results.html", user_text=user_text, tokenized_sentences=tokenized_sentences, 
                                tokenized_words=tokenized_words, diversity_gpt=diversity_gpt, diversity_humans=diversity_humans,
                                average_humans=average_humans, average_gpt=average_gpt, sentiment_humans=sentiment_humans, sentiment_gpt=sentiment_gpt,
                                pun_humans=pun_humans, pun_gpt=pun_gpt)
    return render_template("form.html")
 
if __name__=='__main__':
   app.run()