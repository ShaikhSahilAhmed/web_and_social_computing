import matplotlib.pyplot as plt
import networkx as nx

G=nx.read_edgelist('/home/sahil/Downloads/2nd sem/assignments/wsc/dataset1/wiki-Vote.txt')
print(nx.shortest_path_length(G,source='7092',target='3'))        #(graph, source_node, dest_node)

G=nx.path_graph('/home/sahil/Downloads/2nd sem/assignments/wsc/dataset1/wiki-Vote.txt')
print('Average shortest path length:')
print(nx.average_shortest_path_length(G))

