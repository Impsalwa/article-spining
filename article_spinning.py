# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 18:34:06 2021

@author: Salwa
"""
import nltk
import random 
import numpy as np 

from bs4 import BeautifulSoup

#open and read the data 
positive_reviews = BeautifulSoup(open(r'C:\Users\Salwa\Documents\NLP udemy formation\article_spinning\positive.review').read())
positive_reviews = positive_reviews.findAll('review_text')
#print(positive_reviews)

#create a dict for the trigrams
trigrams = {}
for review in positive_reviews:
    s = review.text.lower()
    tokens = nltk.tokenize.word_tokenize(s)
    for i in range(len(tokens) -2):
        k = (tokens[i], tokens[i+2])
        if k not in trigrams:
            trigrams[k] = []
        trigrams[k].append(tokens[i+1])
#print(trigrams)

#convert trigrams to pobabilities
trigrams_probabilities = {}
for k, words in trigrams.items():
    if len(set(words)) > 1:
        d = {}
        n = 0
        for w in words:
            if w not in d:
                d[w] =0
            d[w] += 1
            n += 1
        for w,c in d.items():
            d[w] = float(c) / n
        trigrams_probabilities[k] = d
#print(trigrams_probabilities)

#create a function to randomly sample from the trigrams probabilities dict 
def random_sample(d):
    r = random.random()
    cumulative = 0
    for w, p in d.items():
        cumulative += p
        if r < cumulative:
            return w
        
#to test the spinner 
#randomly choose a review and try to spinner 
def test_spinner():
    review = random.choice(positive_reviews)
    s = review.text.lower()
    print("Original", s)
    tokens = nltk.tokenize.word_tokenize(s)
    for i in range(len(tokens) -2):
        if random.random() < 2:
            k = (tokens[i], tokens[i+2])
            if k in trigrams_probabilities:
                w = random_sample(trigrams_probabilities[k])
                tokens[i+1]= w
    print("Spun:")
    print(" ".join(tokens).replace(" .", ".").replace(" '", "'").replace(" ,", ",").replace("$ ", "$").replace(" !", "!"))

print(test_spinner())

                         