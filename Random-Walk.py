# Drunkard's walk
# Crawlers take random walk on websites and ranks the websites
# Ranks nodes based on visits
# Google is mainly based on Page Rank System
# Page rank needs directed graph

import networkx as nx
import random
import matplotlib.pyplot as plt
import operator

G  = nx.gnp_random_graph(10, 0.5, directed=True)
# nx.draw(G, with_labels=True)
# plt.show()

x = random.choice(list(G.nodes()))
# x is the random source node

dict_counter = {}
for i in range(G.number_of_nodes()) :
    dict_counter[i] = 0

dict_counter[x] = dict_counter[x] + 1
# increase counter of source node

for i in range(5000000) :
    list_n = list(G.neighbors(x))
    if(len(list_n) == 0):
        # if x is a sink
        x = random.choice(list(G.nodes()))
        dict_counter[x] = dict_counter[x] + 1
        # increment visit value
        i -= 1
    else :
        x = random.choice(list_n)
        # choose new source node randomly
        dict_counter[x] = dict_counter[x] + 1

p = nx.pagerank(G)
sorted_p = sorted(p.items(), key=operator.itemgetter(1), reverse=True)
# 1 = sort by value, 0 = sort by keys
sorted_dict = sorted(dict_counter.items(), key=operator.itemgetter(1), reverse=True)

print([node for node, visits in sorted_p])
print([node for node, visits in sorted_dict])
