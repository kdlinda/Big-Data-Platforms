#!/usr/bin/python
#coding: utf-8

import sys
import os
import csv
from math import log10
from collections import defaultdict


words = []
w_last_txt_id = None
df_dict = defaultdict(lambda: set())
txt_id_list = set()

#--- Input comes from STDIN ---
for line in sys.stdin:
	#Removing leading and trailing whitespace
	line = line.strip()

	#Parse the input received from mapper.py
	key, w_count, w_count_txt, df = line.split('\t')
	
	w_count = int(w_count)
	df = int(df)
	word,txt_id = key.split(",")
	txt_id = int(txt_id)
	w_txt_id = (word,txt_id)

	#--- WordCount ---
	if w_last_txt_id is None:					
		w_last_txt_id = w_txt_id
		last_w_count = 0
		last_w_count_per_txt = w_count_txt
		last_df = df
	if w_txt_id == w_last_txt_id:
		last_w_count += w_count
	else:
		words.append([w_last_txt_id,last_w_count,last_w_count_per_txt,last_df])
		
		# set new values
		w_last_txt_id = w_txt_id
		last_w_count = w_count
		last_w_count_per_txt = w_count_txt
		last_df = df
	
	#--- df Calculation --- 
	dict_v = df_dict[word]
	dict_v.add(txt_id)
	df_dict[word] = dict_v
	
	txt_id_list.add(txt_id)

words.append([w_last_txt_id,last_w_count,last_w_count_per_txt,last_df])
N = len(txt_id_list)

for w_block in words:
	word,txt_id,w_count,w_count_txt,df = w_block[0][0],int(w_block[0][1]),int(w_block[1]),int(w_block[2]),int(w_block[3])
	df = len(df_dict[word])

	#--- Calculating Tf-idf score ---
	w_block.append(w_count * w_count_txt * log10(N/df))
	tfidf = w_block[4]

	#--- Collecting Data Pairs (word, doc_ID, Tf-idf) ---
	formatted_k = '{0:_<30}\n'.format("%s,%i" % (word,txt_id))
	print("%s\t%i\t%i\t%i\t%.*f" % (formatted_k,w_count,w_count_txt,df,5,tfidf))

#--- Output: Top20 Words per Text ---
for txt_id in txt_id_list:
	top20_words = sorted([w_block for w_block in words if w_block[0][1] == txt_id], key=lambda x: x[4], reverse=True)[:20]
	print(top20_words)
