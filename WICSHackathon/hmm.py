# Import the toolkit and tags
import nltk
import csv
import numpy
import random
from nltk.tag import hmm
from nltk import corpus
from nltk import model

reader = csv.reader(open('quotes.csv', 'r'), delimiter= "\n")

rng = random.random()

train_data = []
for i, line in enumerate(reader):
    tokens = nltk.word_tokenize(line[0])
    train_data.append(nltk.pos_tag(tokens))

# model.build_vocabulary(train_data)
#
# content_model = model.ngram.MLENgramModel(train_data)

trainer = hmm.HiddenMarkovModelTrainer()
modelHMM = trainer.train(train_data)
print modelHMM.random_sample(random,random.randrange(10, 20))
#
# print tagger
