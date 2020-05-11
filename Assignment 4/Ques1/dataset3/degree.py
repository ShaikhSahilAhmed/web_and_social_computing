import matplotlib.pyplot as plt
import networkx as nx

G= nx.read_edgelist('/home/sahil/Downloads/2nd sem/assignments/wsc/Assignment 4/dataset3/p2p-Gnutella06.txt')
d=nx.degree_centrality(G) 
print(d)
