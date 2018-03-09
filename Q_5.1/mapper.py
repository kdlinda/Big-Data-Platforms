#!/usr/bin/python
#coding: utf-8

import sys
import re
from nltk.corpus import stopwords

words = []
txt_id=0
line_nr=1
w_count=1
w_count_txt=0
df=1

#--- get all lines from stdin ---
for line in sys.stdin:
	#--- Cleaning: remove leading and trailing whitespace ---
	line = line.strip()

	#--- Associate input documents ---
	if line_nr == 1:
		if line == '1903':
			txt_id=2
			line_nr=0
		else:
			txt_id=1
			line_nr=0

	#--- Tokenization: split the line into words ---
	w_line = line.split()

	#--- Pre-processing ---
	# Converting to lower_case
	w_line = [word.lower() for word in w_line]
	
	#--- Deleting punctuation and numerical characters ---
	w_line = [re.sub(r'[^\w]','',word) for word in w_line]

	#--- Removing stop_words ---
	stop_words = ('a','able','about','across','after','all','almost','also','am','among','an','and','any','are','as','at','be','because','been','but','by',
            	     'can','cannot','could','dear','did','do','does','either','else','ever','every','for','from','get','got','had','has','have','he','her','hers',
                     'him','his','how','however','i','if','in','into','is','it','its','just','least','let','like','likely','may','me','might','most','must','my',
                     'neither','no','nor','not','of','off','often','on','only','or','other','our','own','rather','said','say','says','she','should','since','so',
                     'some','than','that','the','their','them','then','there','these','they','this','tis','to','too','twas','us','wants','was','we','were','what',
                     'when','where','which','while','who','whom','why','will','with','would','yet','you','your')
	
	w_line = [word for word in w_line if word not in stop_words]

	#--- Removing words with less than 3 characters ---
	w_line = [word for word in w_line if len(word)>2]

	#--- Concatenating lists ---
	words += w_line
	w_count_txt += len(w_line)

#--- Output Tuples: [word,1] in tab-delimited format ---
for word in words:
	print('%s,%i\t%i\t%i\t%i' % (word, txt_id, w_count, w_count_txt, df))

