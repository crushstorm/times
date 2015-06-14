import csv
import os
import codecs
import csv
import nltk
import json
import pprint
from nltk import pos_tag, word_tokenize
from time import time
from collections import Counter
from nltk.tokenize import RegexpTokenizer

#India_Province = ['ANDHRA PRADESH','ASSAM','BIHAR','CHHATTISGARH','DELHI','GOA','GUJARAT','HARYANA','HIMACHAL PRADESH','JAMMU & KASHMIR','JHARKHAND','KARNAKATA','KERALA','MADHYA PRADESH','MAHARASHTRA','ORISSA','PONDICHERRY','PUNJAB','RAJASTHAN','TAMIL NADU','UTTAR PRADESH','UTTARANCHAL','WEST BENGAL']
internet_related = ['4G','LTE','INTERNET','MOBILE','IP','ADDRESS','DOMAIN','WEB','SITES','PAGES','BANDWIDTH','PROVIDER','MOBIL','CARRIER','3G','DATA','TERMINAL','DEVICES','E-COMMERCE','ONLINE','BROADBAND'];


freq  = {}
town_freq = {}
max1 = 0
tempdate = 1
t = 0
with codecs.open('all.txt') as file:
	for line in file:
		# get out at the end of line
		if (line == '\n'):
			break
		data = json.loads(line)
		# if the month is different from tempdate. Print out all the statistics information
		if (int(data['date'][5:7]) != tempdate):
			# replace the tempdate with the new values
			tempdate = int(data['date'][5:7])

			print "Frequency for month ",tempdate, " ", data['date'][0:4]
			if freq:
				# print out the statistics of words based on dictionary of words exist
				for key,value in freq.items() :
					print key,'\t',value
		
			freq = {}
		# tokenizing words
		tokenizer = RegexpTokenizer(r'\w+')
		text = tokenizer.tokenize(data['text'].upper())

		

		for w  in text:
			# check whether w is available in the list of words
			if (w in (internet_related[:1]+internet_related[2:])):
				
				if freq.has_key(w):
					freq[w] = freq[w]+1
				else:
					freq[w] = 1	
		