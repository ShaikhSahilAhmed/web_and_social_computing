import matplotlib.pyplot as plt
import networkx as nx

G=nx.read_edgelist('/home/sahil/Downloads/2nd sem/assignments/wsc/dataset2/p2p-Gnutella04.txt')
print(nx.shortest_path_length(G,source='20',target='796'))        #(graph, source_node, dest_node)

G=nx.path_graph('/home/sahil/Downloads/2nd sem/assignments/wsc/dataset2/p2p-Gnutella04.txt')
print('Average shortest path length:')
print(nx.average_shortest_path_length(G))

