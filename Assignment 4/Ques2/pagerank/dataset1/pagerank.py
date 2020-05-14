import networkx as nx 
G= nx.read_edgelist('/home/sahil/Downloads/2nd sem/assignments/wsc/Assignment 4/Ques2/pagerank/dataset1/wiki-Vote.txt') 
pr=nx.pagerank(G,0.4) 
print(pr)
temp = min(pr.values()) 
res = [key for key in pr if pr[key] == temp] 
  
# printing result  
print("Keys with minimum values are : " + str(res)) 
 
temp2 = max(pr.values()) 
res2 = [key2 for key2 in pr if pr[key2] == temp2] 
  
# printing result  
print("Keys with maximum values are : " + str(res2)) 
