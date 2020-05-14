# importing modules 
import networkx as nx 
import matplotlib.pyplot as plt 
  
G= nx.read_edgelist('/home/sahil/Downloads/2nd sem/assignments/wsc/Assignment 4/Ques2/hits/dataset3/p2p-Gnutella06.txt')
 
hubs, authorities = nx.hits(G, max_iter = 50, normalized = True) 
  
import numpy as np
lists = sorted(hubs.items()) # sorted by key, return a list of tuples

x, y = zip(*lists) # unpack a list of pairs into two tuples
plt.figure(figsize=(12,7))
plt.xlabel('Node id')
plt.ylabel('Scores')
plt.plot(x, y)
plt.xticks(np.arange(0,9500, 500))
plt.legend()
