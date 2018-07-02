#! /usr/bin/python2

""" Author: Oliver Tarrant
	Plot a snapshot of a food web graph/network.
	
	Needs: Adjacency list of who eats whom (consumer name/id in 1st 
	column, resource name/id in 2nd column), and list of species 
	names/ids and properties such as biomass (node abundance) or 
	average body mass.
	
""" 

import networkx as nx
import scipy as sc
import matplotlib.pyplot as plt
import matplotlib.animation as ani # for animation

def GenRdmAdjList(N = 2, C = 0.5):
	"""Generate random adjacency list given N nodes with connectance 
		probability C
	"""
	Ids = range(N)
	Alst = []
	for i in Ids:
		if sc.random.uniform(0,1,1) < C:
			Lnk = sc.random.choice(Ids,2).tolist() #generates a random sample of 2 elements from Ids and turns them to a list
			if Lnk[0] != Lnk[1]: # avoid self loops
				Alst.append(Lnk)
	return Alst
	
## Assign body mass range
SizRan = ([-10,10]) # use log scale

## Assign number of species (MaxN) and connectance (C)
MaxN = 30
C = 0.75

## Generate adjacency list:
AdjL = sc.array(GenRdmAdjList(MaxN,C))

## Generate species (node) data:
Sps = sc.unique(AdjL) # get species ids
Sizs = sc.random.uniform(SizRan[0], SizRan[1], MaxN) # Generate body sizes (log10 scale)


##### The Plotting #####
plt.close('all')

## Plot usign networkx:

## Calculate coordinates for circular configuration:
## (See networkx.layout for inbuilt functions to compute other types of node
# coords)
pos = nx.circular_layout(Sps)

G = nx.Graph()
G.add_nodes_from(Sps)
G.add_edges_from(tuple(AdjL))
NodSizs = 10**-32 + (Sizs - min(Sizs))/(max(Sizs)-min(Sizs)) # node sizes in proportion to body sizes
nx.draw(G, pos, nod_size = NodSizs*1000)
plt.show()
