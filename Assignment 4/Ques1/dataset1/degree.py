import matplotlib.pyplot as plt
import networkx as nx

G= nx.read_edgelist('/home/sahil/Downloads/2nd sem/assignments/wsc/dataset1/wiki-Vote.txt')
d=nx.degree_centrality(G) 
print(d)
