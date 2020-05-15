# Web_and_Social_Computing(IT752)
## Assignment 1  
It contains various datasets of a graph as shown:  
    1. wiki-Vote  
    2. p2p-Gnutella04  
    3. p2p-Gnutella06  

Under each dataset, there are files which describes the properties of a graph as given:  
    1. Degree Distribution  
    2. Diameter  
    3. Geodesic path length  
    4. Clustering Coefficient   
    5. Strongly Connected Components  
    6. Sparseness  
    7. k-connectedness  
    8. SCC properties
   
#### Requirements
1. networkx  
2. matplotlib.pyplot  
3. pandas  

#### Executing files 
1. Locate the path of given dataset.  
2. Execute files in terminal using python command.  
Example:  
Name of file is name.py  
Go to terminal > python name.py  
Press Enter.

## Assignment 2  
It contains various datasets of a graph as shown:  
    1. wiki-Vote  
    2. p2p-Gnutella04  
    3. p2p-Gnutella06  

Under each dataset, there are files which describes the properties of graph using three models:  
1. Erdos Renyi  
2. Watts Strogatz  
3. Barabasi Albert  

#### Requirements
1. networkx  
2. matplotlib.pyplot  

#### Executing files 
1. Input for 3 models are already considered in code according to the nodes and edges given in dataset. 
2. Visit https://colab.research.google.com/ and upload the files.  
3. Execute the code.  


## Assignment 3
The basic web crawler is uploaded under crawler directory. The main.py file contains the crawler program where it is crawling the website URL: 'http://infotech.nitk.ac.in/'.

#### Requirements
1. icrawler  
2. spider 

#### Executing files 
1. python main.py for basic crawler  
2. For single and multithreaded crawler upload the Crawler_Thread.ipynb and execute it.
3. For bfs and dfs enter {python bfs_dfs.py 'number of seeds' <dfs/bfs>}
4. Data structure used for indexing is mentioned in the Assignment three report.

## Assignment 4
Datasets used are same as Assignment 1.
### Ques 1
Measurements are:
1. Degree centrality
2. Closeness centrality
3. Betweenness centrality
4. Eigenvector centrality

#### Executing files 
1. python filename.py

For every dataset, it contains 'results' directory which contains all 4 types of centrality for every node.

### Ques 2
This directory contains two subdirectories as "hits" and "pagerank".

#### PageRank
It contains 3 sub directories for each dataset. In each of the dataset it contains python file for PageRank Score calculation  for each of the nodes and the nodes which are having min and max score. It also contains the python file to plot the graph for Score vs node-id.

#### HITS
It contains 3 sub directories for each dataset. In each of the dataset it contains python file for HITS Hub and Authority Score calculation for each of the nodes and the nodes which are having min and max score. It also contains the python file to plot the graph for Score vs node-id.

##### Executing files
1. python filename.py

For every dataset, it contains 'results' directory which contains their score values with respect to their node-id.
