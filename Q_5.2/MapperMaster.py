#!/usr/bin/python

import sys

adjacency_list = []
current_node = None

page_rank = 1.0

for line in sys.stdin:

    if line[0] == '#' or line.strip() == "":
        continue

    node1, node2 = line.split('\t')
    node1 = node1.strip()
    node2 = node2.strip()

    # append node (still the first one)
    if current_node == node1:
        adjacency_list.append(node2)

    # on a different node
    else:
        if current_node != None:
            print('%s\t%s %s' % (current_node, str(page_rank), ' '.join(adjacency_list)))

        current_node = node1
        adjacency_list = [node2]

if current_node != None:
    print('%s\t%s %s' % (current_node, str(page_rank), ' '.join(adjacency_list)))

