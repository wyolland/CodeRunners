# Import the toolkit and tags
import csv
import random
import nltk
import language_check
from nltk import tokenize
from nltk.tag import hmm

tool = language_check.LanguageTool('en-US')

QUOTES_TO_GEN = 100
UPPER_QUOTE = 20
LOWER_QUOTE = 7

rng = random.random()

reader = csv.reader(open('quotes.csv', 'r'), delimiter= "\n")

words_only = tokenize.RegexpTokenizer('([A-Za-z]\w+)')

train_data = []
for i, line in enumerate(reader):
    tokens = words_only.tokenize(line[0])
    train_data.append(nltk.pos_tag(tokens))

reader = csv.reader(open('quotes2.csv', 'r'), delimiter="\n")

for i, line in enumerate(reader):
    if line:
        tokens = words_only.tokenize(line[0])
        train_data.append(nltk.pos_tag(tokens))

trainer = hmm.HiddenMarkovModelTrainer()
modelHMM = trainer.train(train_data)

f = open("input.txt", 'w')

for i in range(QUOTES_TO_GEN):
    quote_list = modelHMM.random_sample(random,random.randrange(LOWER_QUOTE, UPPER_QUOTE))
    LENGTH = len(quote_list)
    quote_str = ""
    for j in range(0, LENGTH):
        quote_str = (quote_str + quote_list[j][0] + " ") if j+1 < len(quote_list) else (quote_str + quote_list[j][0] + ".\n")
    matches = tool.check(quote_str)
    quote_str = language_check.correct(quote_str, matches)
    f.write(quote_str)

f.close()
