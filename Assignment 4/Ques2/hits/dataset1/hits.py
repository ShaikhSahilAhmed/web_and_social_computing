# importing modules 
import networkx as nx 
import matplotlib.pyplot as plt 
  
G= nx.read_edgelist('/home/sahil/Downloads/2nd sem/assignments/wsc/Assignment 4/Ques2/hits/dataset1/wiki-Vote.txt')
  
hubs, authorities = nx.hits(G, max_iter = 50, normalized = True) 
  
print("Hub Scores: ", hubs) 
print("Authority Scores: ", authorities) 

temp = min(hubs.values()) 
res = [key for key in hubs if hubs[key] == temp] 
  
# printing result  
print("Min hub : " + str(res)) 
 
temp2 = max(hubs.values()) 
res2 = [key2 for key2 in hubs if hubs[key2] == temp2] 
  
# printing result  
print("Max hub : " + str(res2))

temp3 = min(authorities.values()) 
res3 = [key3 for key3 in authorities if authorities[key3] == temp3] 
  
# printing result  
print("Min authority : " + str(res3))

temp4 = max(authorities.values()) 
res4 = [key4 for key4 in authorities if authorities[key4] == temp4] 
  
# printing result  
print("Max authority : " + str(res4))
