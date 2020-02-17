import matplotlib.pyplot as plt
from networkx import nx

G = nx.read_edgelist('/home/sahil/Downloads/2nd sem/assignments/wsc/dataset1/wiki-Vote.txt')

#c = nx.k_components(G, flow_func=None)
c = nx.number_connected_components(G)
print(c)
