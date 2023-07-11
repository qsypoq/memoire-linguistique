import nltk 
from os import listdir
from os.path import isfile, join
nltk.download('punkt')

files = [f for f in listdir("gpt/txt") if isfile(join("gpt/txt", f))]

def addtolist(item):
    with open(f"gpt/count.txt", 'a+') as outfile:
            outfile.write(f"{item}\n")

for file in files:
    with open (f"gpt/txt/{file}", "r") as string:
        data=string.read()
        words= nltk.word_tokenize(data)
        addtolist(len(words))