import matplotlib.pyplot as plt
import networkx as nx

def plot_degree_dist(G):
    degrees = [G.degree(n) for n in G.nodes()]
    plt.hist(degrees)
    plt.show()

plot_degree_dist(nx.read_edgelist('/home/sahil/Downloads/2nd sem/assignments/wsc/dataset3/p2p-Gnutella06.txt'))
G= nx.read_edgelist('/home/sahil/Downloads/2nd sem/assignments/wsc/dataset3/p2p-Gnutella06.txt')
degrees=nx.degree(G)
all_degrees=list(dict(degrees).values())
#print all_degrees
unique_degrees=list(set(all_degrees))
#print unique_degrees
count_degrees = []
for i in unique_degrees:
  count=all_degrees.count(i)
  count_degrees.append(count)
plt.xlabel("Degree")
plt.ylabel("Number of nodes")
plt.title("Degree distribution of p2p-Gnutella06  ")
plt.plot(unique_degrees,count_degrees)
plt.show()
