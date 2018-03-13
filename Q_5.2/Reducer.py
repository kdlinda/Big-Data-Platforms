#!/usr/bin/python

import sys

current_node = None
lines = []

damping = 0.85

# Take list of lines for the same node
def node_processor(ls):

    page_rank = 0
    adj_list = []
    node = None
    for i in l:

        n, value = i.split('\t', 1)

        typ, value = value.split(' ', 1)
        
        if type == 'node':
            adj_list = value
            node = n
        
        elif type == 'score':
            page_rank += float(value)
            
        else:
            raise Exception('Type is unknown')

    page_rank = (1.0 - damping) + (damping * page_rank)

    # If node = none, no adjacency list for this node
    if node == None:
        pass
    else:
        print('%s\t%s %s' % (node, str(page_rank), adj_list))


for line in sys.stdin:

    line = line.strip()
    node = line.split('\t', 1)[0][:-1] # Skip the last char which is used for sorting

    # If 1st node, set the current node
    if current_node == None:
        current_node = node

    # Process node if info is complete
    if current_node != node:

        # Process the node
        node_processor(lines)

        # Update 
        current_node = node
        lines = [line]

    # Append line
    else:
        lines.append(line)

if current_node != None:
    node_processor(lines)

