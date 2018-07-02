#! usr/bin/python3
""" Author: Oliver Tarrant

A python version of Nets.R , Takes the QMEE CDT data and returns a 
visualisation of the network of connections coloured and sized by
the type of institution and the number of Phd students connected to it
"""

import networkx as nx
import scipy as sc
import csv
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.cm as cmx
import matplotlib.lines as lines

### edges file for the graph
edgs = csv.reader(open('../Data/QMEE_Net_Mat_edges.csv', 'rt'), delimiter=",")
edgs = list(edgs)
### nodes file for graph
nods = csv.reader(open('../Data/QMEE_Net_Mat_nodes.csv','rt'), delimiter = ",")
nods = list(nods)
### 
edges=sc.array(edgs[1:]).astype("float") # remove headers from the array
places=list(sc.array(edgs[0]))
G=nx.from_numpy_matrix(edges) # defines network from array


#relable the nodes
#first need dictionary of old nodes to new
k = list(range(len(G.nodes))) #define keys
v = list(places) # define the new node names
mapping=dict(zip(k,v)) # generate the dictionary
G=nx.relabel_nodes(G,mapping) #apply the relabling


###### add type to nodes######
Types = list()
for i in range(1,len(nods)):
	Type = nods[i][1]
	Types.append(Type)
#Create a dictionary from nodes to Types
TypeMap=dict(zip(v,Types))
for nod in G.nodes:        #Assign the types to the nodes
	G.node[nod]['Type']=TypeMap[nod]

####Set color_map for types#####
color_map={'University':'green','Hosting Partner' : 'red','Non-Hosting Partners':'blue'} #set colours
for n in G.nodes():
	T = nx.get_node_attributes(G,'Type')
	G.node[n]['color']=color_map[T[n]] # assign colours to the nodes by lookign at the types
	
##### add Pis to nodes ######
Pis = list()
for i in range(1,len(nods)):
	P = nods[i][2]
	Pis.append(P)
#Create a dictionary from nodes to Pis
PisMap=dict(zip(v,Pis))
for nod in G.nodes:        #Assign the types to the nodes
	G.node[nod]['Pis']=float(PisMap[nod])*20

# Create a dictionary from nodes to colors
Col=list()
for i in range(1, len(nods)):
	c = color_map[nods[i][1]]
	Col.append(c)
ColMap = dict(zip(v,Col))





plt.close('all')

pos=nx.spring_layout(G)


nx.draw(G, pos=pos,with_labels=True, node_color=[G.node[node]['color'] for node in G], node_size=[G.node[node]['Pis']*1.5 for node in G] ) # draws the graph
nx.draw_networkx_edges(G, pos=pos,width=[(G.edges[edge]['weight']+1)/10 for edge in G.edges], arrows=True)
# plot includes colouring by type and sized by Pis value

### Create a legend
linelst=[] #create blank list of points for the legend
Types=list(color_map) #Create a list of types to be added to the legend
for i in range(0,len(color_map)):
	line = lines.Line2D(range(1), range(1),color=color_map[Types[i]], marker ='o', markerfacecolor=color_map[Types[i]])
	linelst.append(line)
	
plt.legend((linelst),(Types),numpoints=1, loc=2)

plt.savefig('../Results/QMEENet_py.svg')
