#!/usr/bin/env python2.7

import sys

data = []
for line in sys.stdin:

    line = line.strip()
    node, value = line.split('\t',1)
    page_rank = float(value.split(' ',1)[0])
    data.append((node, page_rank))

for i in sorted(data, key=lambda x: x[1], reverse=True)[:20]:
    print(i)

