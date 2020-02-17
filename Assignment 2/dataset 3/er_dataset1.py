import networkx as nx
import matplotlib.pyplot as plt
n=8717
m=31525
def plot_deg_dist(G):
	all_degree=dict(nx.degree(G)).values()
	
	unique_degree=list(set(all_degree))
	
	count_degree=[]
	all_degree=list(all_degree)
	
	for i in unique_degree:
		x=all_degree.count(i)
		count_degree.append(x)
	
	
	
	plt.plot(unique_degree,count_degree,'yo-')
	plt.xlabel('Degrees')
	plt.ylabel('No of nodes ')
	plt.title('Degree distribution of network')
	plt.show()

G = nx.gnm_random_graph(n, m)
print("Shortest path ")
for C in (G.subgraph(c).copy() for c in nx.connected_components(G)):
  print(nx.average_shortest_path_length(C))
print(nx.average_clustering(G))
plot_deg_dist(G)
