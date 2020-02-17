import networkx as nx
import matplotlib.pyplot as plt

G= nx.read_edgelist('/home/sahil/Downloads/2nd sem/assignments/wsc/dataset1/wiki-Vote.txt')

print (nx.density(G))
