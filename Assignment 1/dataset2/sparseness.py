import networkx as nx
import matplotlib.pyplot as plt

G= nx.read_edgelist('/home/sahil/Downloads/2nd sem/assignments/wsc/dataset2/p2p-Gnutella04.txt')

print (nx.density(G))
