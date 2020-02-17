
import networkx as nx
import matplotlib.pyplot as plt

cam_net= nx.read_edgelist('/home/sahil/Downloads/2nd sem/assignments/wsc/dataset3/p2p-Gnutella06.txt')

for i in nx.clustering(cam_net).items():
  print (i)
print ("average clustering coefficient:")
print (nx.average_clustering(cam_net))



