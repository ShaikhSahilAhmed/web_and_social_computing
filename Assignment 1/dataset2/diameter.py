
import networkx as nx
import matplotlib.pyplot as plt

cam_net= nx.read_edgelist('/home/sahil/Downloads/2nd sem/assignments/wsc/dataset2/p2p-Gnutella04.txt')

print (nx.diameter(cam_net))





