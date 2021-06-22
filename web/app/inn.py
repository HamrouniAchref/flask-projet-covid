from textblob_fr import PatternTagger, PatternAnalyzer
from textblob.classifiers import PositiveNaiveBayesClassifier
from textblob.classifiers import NaiveBayesClassifier

from flask import Flask, url_for, jsonify , request,json
import string
from langdetect import detect
from langdetect import detect_langs
from textblob import TextBlob  
from textblob_ar import TextBlob as TextBlobAr 
from textblob.classifiers import NaiveBayesClassifier
from datetime import datetime
from app_key import require_appkey
from difflib import SequenceMatcher
import nltk
from nltk.corpus import stopwords
import csv
import os
import random
import linecache


train=[]
for root, dirs, files in os.walk("pos"): 
        for i in files: 
            l=[]
            f = open(os.path.join(root, i), "r")
            l.append(f.read().replace("\n", '').replace(",", '').replace("'", '').strip())
            l.append('pos')
            train.append(l)
 
for root, dirs, files in os.walk("neg"): 

        for i in files: 
            l=[]
           # fichier.append(os.path.join(root, i))
            f = open(os.path.join(root, i), "r")
            l.append(f.read().replace("\n", '').replace(",", '').replace("'", '').strip())
            l.append('neg')
            train.append(l)
global cl = NaiveBayesClassifier(train)