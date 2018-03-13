#!/usr/bin/python
#coding: utf-8

import sys
import os
import csv
from math import log10
from collections import defaultdict

words = []
w_last_txtid = None
df_dict = defaultdict(lambda: set())
txtid_list = set()

#--- Input comes from STDIN ---
for line in sys.stdin:
	#Removing leading and trailing whitespace
	line = line.strip()

	#Parse the input received from mapper.py
	key, w_count, w_count_txt, df = line.split('\t')
	
	w_count = int(w_count)
	df = int(df)
	word,txtid = key.split(",")
	txtid = int(txtid)
	w_txtid = (word,txtid)

	#--- WordCount ---
	if w_last_txtid is None:					
		w_last_txtid = w_txtid
		last_w_count = 0
		last_w_count_per_txt = w_count_txt
		last_df = df
	if w_txtid == w_last_txtid:
		last_w_count += w_count
	else:
		words.append([w_last_txtid,last_w_count,last_w_count_per_txt,last_df])
		
		# set new values
		w_last_txtid = w_txtid
		last_w_count = w_count
		last_w_count_per_txt = w_count_txt
		last_df = df
	
	#--- df Calculation --- 
	dict_v = df_dict[word]
	dict_v.add(txtid)
	df_dict[word] = dict_v
	
	txtid_list.add(txtid)

words.append([w_last_txtid,last_w_count,last_w_count_per_txt,last_df])
N = len(txtid_list)

for item in words:
	word,txtid,w_count,w_count_txt,df = item[0][0],int(item[0][1]),int(item[1]),int(item[2]),int(item[3])
	df = len(df_dict[word])

	#--- Calculating Tf-idf score ---
	item.append(w_count * w_count_txt * log10(N/df))

#--- Output: Top20 Words per Text ---
for txtid in txtid_list:
	top20_words = sorted([item for item in words if item[0][1] == txtid], key=lambda x: x[4], reverse=True)[:20]
	print(top20_words)

