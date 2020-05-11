import matplotlib.pyplot as plt
import networkx as nx

G= nx.read_edgelist('/home/sahil/Downloads/2nd sem/assignments/wsc/Assignment 4/dataset2/p2p-Gnutella04.txt')
d=nx.closeness_centrality(G) 
print(d)
