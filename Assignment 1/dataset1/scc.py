import matplotlib.pyplot as plt
from networkx import nx
import pandas as pd


df = pd.read_csv("wiki-Vote.csv")
G = nx.from_pandas_edgelist(df,'src','dst',edge_attr=None,create_using=nx.DiGraph())

for c in nx.strongly_connected_components(G):
 print(c)


p= nx.number_strongly_connected_components(G)
print(p)
