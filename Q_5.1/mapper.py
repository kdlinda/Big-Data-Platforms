#!/usr/bin/env python
#coding: utf-8

import sys
import re

#--- get all lines from stdin ---
for line in sys.stdin:
    #--- remove leading and trailing whitespace---
    line = line.strip()

    #--- Tokenization - split the line into words ---
    words = line.split()

    #---output tuples [word, 1] in tab-delimited format ---
    for word in words:
        print '%s\t%s' % (word, "1")
