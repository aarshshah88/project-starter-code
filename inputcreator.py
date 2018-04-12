import sys
import networkx as nx
import numpy as np


#takes in a graph and edge between u and v with weight x
def edgeAdder(G, u, v, x):
	G.add_edge(u, v, weight= x)

#adding a node called,u , with conquesting cost, v, and edge degree, x. 
def nodeAdder(G, u, v):
	G.add_node(u, conquesting_cost = v)


#takes in a graph and writes it to a file
def write_to_file(G):
	f = open("Inputs","w")
	AL = nx.to_numpy_matrix(G)
	print(AL)
	list_of_data = G.nodes.data("conquesting_cost")
	AL = AL.tolist()
	print(type(AL))
	count = 0
	for n in G:
		AL[n][n] = list_of_data[n]
	print(AL)


G = nx.Graph()
nodeAdder(G, 0, 20)
nodeAdder(G, 1, 5)
nodeAdder(G, 2, 30)
nodeAdder(G, 3, 30)
nodeAdder(G, 4, 30)
edgeAdder(G, 0, 1, 20)
edgeAdder(G, 0, 3, 5)
edgeAdder(G, 1, 3, 10)
edgeAdder(G, 1, 2, 10)
edgeAdder(G, 1, 4, 10)
edgeAdder(G, 2, 3, 10)
edgeAdder(G, 3, 4, 10)

write_to_file(G)


