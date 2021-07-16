#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# NISHI SINGH
# HOOMACL201900025
# MA COMPUTATIONAL LINGUISTICS


# This module is written to do a Resource Based Semantic analyasis using hindi sentiwordnet.
import pandas as pd
import codecs
from nltk.tokenize import word_tokenize
import sklearn.metrics
import re
fields = ['POS_TAG', 'ID', 'POS', 'NEG', 'LIST_OF_WORDS']
#Creating a dictionary which contain a tuple for every word. Tuple contains a list of synonyms,
# positive score and negative score for that word.
def sentiment(text):
    print(text)
    words = word_tokenize(text)
    votes = []
    pos_polarity = 0
    neg_polarity = 0
    #adverbs, nouns, adjective, verb are only used
    allowed_words = ['a','v','r','n']
    for word in words:

        if word in words_dict:
            #if word in dictionary, it picks up the positive and negative score of the word
            pos, neg = words_dict[word]
            print(word,pos, neg)
            if pos > neg:
                pos_polarity += pos
                votes.append(1)
            elif neg > pos:
                neg_polarity += neg
                votes.append(0)
    #calculating the no. of positive and negative words in total in a review to give class labels
    pos_votes = votes.count(1)
    neg_votes = votes.count(0)
    if pos_votes > neg_votes:
        return 1
    elif neg_votes > pos_votes:
        return -1
    else:
        if pos_polarity < neg_polarity:
            return 1
        elif neg_polarity>pos_polarity :
            return -1
        else:
            return 0
words_dict = {}
# This function determines sentiment of text.
data = pd.read_csv("HindiSentiWordnet.txt", delimiter=' ')
for i in data.index:
    # print (data[fields[0]][i], data[fields[1]][i], data[fields[2]][i], data[fields[3]][i], data[fields[4]][i])
    words = data[fields[4]][i].split(',')
    for word in words:
        words_dict[word] = (data[fields[2]][i], data[fields[3]][i])
        #print(word,data[fields[0]][i], data[fields[2]][i], data[fields[3]][i])
# for x in words_dict:
#     print(x)
#     for y in words_dict[x]:
#         print(y)
c='Y'
while c=='Y' or c=='y':
    text=input('Enter a Hindi news article: ')
    t=sentiment(text)
    if t==1:
        print("Positive")
    elif t==-1 :
        print("Negative")
    else:
        print("Neutral")
    c=input('To Continue press Y: ')
#print(len(actual_y))
#print(accuracy_score(actual_y, pred_y) * 100)
#print('F-measure:  ',f1_score(actual_y,pred_y))

