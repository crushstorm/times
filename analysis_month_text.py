import csv
import os
import codecs
import nltk
import json
import pprint
from nltk import pos_tag, word_tokenize
from time import time
from collections import Counter
from nltk.tokenize import RegexpTokenizer

India_Province = ['ANDHRA PRADESH','ASSAM','BIHAR','CHHATTISGARH','DELHI','GOA','GUJARAT','HARYANA','HIMACHAL PRADESH','JAMMU & KASHMIR','JHARKHAND','KARNAKATA','KERALA','MADHYA PRADESH','MAHARASHTRA','ORISSA','PONDICHERRY','PUNJAB','RAJASTHAN','TAMIL NADU','UTTAR PRADESH','UTTARANCHAL','WEST BENGAL']
internet_related = ['4G','LTE'];


freq  = {}
town_freq = {}
max1 = 0
temp = '2012-12-31'
tempdate = 1
with codecs.open('all.txt') as file:
	for line in file:
		
		if (line == '\n'):
			break
		data = json.loads(line)
		if (int(data['date'][5:7]) != tempdate):
			tempdate = int(data['date'][5:7])

			print "Frequency for month ",tempdate, " ", data['date'][0:4]
			print freq
			freq = {}
		tokenizer = RegexpTokenizer(r'\w+')
		text = tokenizer.tokenize(data['text'].upper())

		for w  in text:
			if (w in (internet_related[:1]+internet_related[2:])):
			
				if freq.has_key(w):
					freq[w] = freq[w]+1
					#max1 = max(max1,freq[w])
				else:
					freq[w] = 1	
		