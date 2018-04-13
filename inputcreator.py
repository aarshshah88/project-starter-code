import sys
import networkx as nx
import numpy as np


#takes in a graph and edge between u and v with weight x
def edgeAdder(G, u, v, x):
	edgeUtoVweightX = (u, v, x)
	G.add_edge(u, v, weight= x)
	return G

#adding a node called,u , with conquesting cost, v, and edge degree, x. 
def nodeAdder(G, u, v, x):
	G.add_node(u, conquesting_cost = v, edge_degree = x)


def adjaceny_matrix_creator(G):
	return (nx.to_numpy_matrix(G)).tolist()

# def addxtoAL(AL, list_of_edges):
# 	for x in list_of_edges:
# 		start, end = x
# 		print(AL[start][end])
# 		AL[start][end] =  AL[start][end] - 10000
# 		AL[end][start] =  AL[end][start] - 10000

# 	for y in AL:
# 		for p in y:
# 			if AL[y][p] == 0:
# 				AL[y][p] = 'x'

# 	for x in list_of_edges:
# 		start, end = x
# 		AL[start][end] += 10000
# 		AL[end][start] += 10000

#adding x's
def ALcreator(G):
	AL = (nx.to_numpy_matrix(G)).tolist()
	print(AL)

	list_of_data = G.nodes.data("conquesting_cost")

	for n in G:
		AL[n][n] = list_of_data[n]

	for x in range(len(AL)):
		for y in range(len(AL)):
			if AL[x][y] == 0:
				AL[x][y] = 'x'

	return AL

#takes in a graph and writes it to a file
def write_to_file(G):
	f = open("Inputs","w")
	adjacency_list_formatted =  []
	temp = ALcreator(G)
	print(temp)
	# for item in f:

	return temp

G = nx.Graph()
list_of_edges = []
nodeAdder(G, 0, 3, 3)
nodeAdder(G, 1, 4, 4)
nodeAdder(G, 2, 5, 5)
nodeAdder(G, 3, 6, 6)
edgeAdder(G, 0, 1, 2)
edgeAdder(G, 1, 2, 6)
edgeAdder(G, 2, 3, 7)

temp = write_to_file(G)









