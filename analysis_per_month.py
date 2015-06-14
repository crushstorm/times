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
internet_related = ['4G','LTE','INTERNET','MOBILE','IP','ADDRESS','DOMAIN','WEB','SITES','PAGES','BANDWIDTH','PROVIDER','MOBIL','CARRIER','3G','DATA','TERMINAL','DEVICES','E-COMMERCE','ONLINE','BROADBAND'];


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
		text = tokenizer.tokenize(data['title'].upper())

		#print int(data['date'][5:7])
		#making frequency table
		#for w in text:
		#	if freq.has_key(w):
		#		freq[w] = freq[w]+1
		#		max1 = max(max1,freq[w])
		#	else:
		#		freq[w] = 1

		for w  in text:
			#if (w = '')
				#break
			if (w in (internet_related[:1]+internet_related[2:])):
				#print data['date'],'\t',data['city'].upper(),'\t\t\t',data['title'].encode('UTF-8')
				#if (town_freq.has_key(data['city'].upper())):
				#	town_freq[data['city'].upper()] = town_freq[data['city'].upper()]+1
				#else:
				#	town_freq[data['city'].upper()] = 1

				if freq.has_key(w):
					freq[w] = freq[w]+1
					#max1 = max(max1,freq[w])
				else:
					freq[w] = 1	
		#print nltk.pos_tag(text)

		#print (data)
		#if (data['date'] == temp):
		#	print town_freq
#print town_freq
#print freq
#print max1