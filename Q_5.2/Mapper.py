#!/usr/bin/env python2.7import sys

for line in sys.stdin:

    line = line.strip()
    
    node, value = line.split('\t', 1)
    page_rank, adj_list = val.split(' ', 1)
    page_rank = float(pr)
    adj_list = adj_list.split(' ')

    # Print score for node
    for out_node in adj_list:
        print('%s\tscore %s' % (out_node, str(page_rank/float(len(adj_list:)))))

    # Print adjacency list
    print('%s\tnode %s' % (node, ' '.join(adj_list:)))

