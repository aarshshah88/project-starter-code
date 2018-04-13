import sys
import networkx as nx
import numpy as np
import random
<<<<<<< HEAD
=======

>>>>>>> 2bd1c756f982e0586b94919e732bb6fc209c8aca

#takes in a graph and edge between u and v with weight x
def edgeAdder(G, u, v, x):
	G.add_edge(u, v, weight= x)
<<<<<<< HEAD
=======

#adding a node called,u , with conquesting cost, v
def nodeAdder(G, u, v):
	G.add_node(u, conquesting_cost = v)


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
>>>>>>> 2bd1c756f982e0586b94919e732bb6fc209c8aca

#adding a node called,u , with conquesting cost, v
def nodeAdder(G, u, v):
	G.add_node(u, conquesting_cost = v)


#takes in a graph and writes it to a file
def write_to_file(G):
	f = open("Inputs","w")
<<<<<<< HEAD
	AL = nx.to_numpy_matrix(G)
	list_of_data = G.nodes.data("conquesting_cost")
	print(AL)
	AL = AL.tolist()
	count = 0
	for n in G:
		AL[n][n] = list_of_data[n]
	print(AL)
=======
	adjacency_list_formatted =  []
	temp = ALcreator(G)
	print(temp)
	# for item in f:

	return temp

def graphGenerator(n, k):
	G = nx.Graph()
	for i in np.arange(n):
		r = random.randint(10, 100)
		nodeAdder(G, i, r)

	for j in np.arange(k):
		v = random.randint(0, n)
		u = random.randint(0, n)
		r = random.randint(10, 100)
		if u != v:
			edgeAdder(G, u, v, r)

	AL = nx.to_numpy_matrix(G)
	nx.draw_networkx(G)
	return G

#takes in a graph G and numbers n,k and creates a random graph around G with n vertices and k edges. Returns new graph H
#def graphGenerator(G, n, k):
	#H = G

# G = nx.Graph()
# nodeAdder(G, 0, 20)
# nodeAdder(G, 1, 5)
# nodeAdder(G, 2, 30)
# nodeAdder(G, 3, 30)
# nodeAdder(G, 4, 30)
# edgeAdder(G, 0, 1, 20)
# edgeAdder(G, 0, 3, 5)
# edgeAdder(G, 1, 3, 10)
# edgeAdder(G, 1, 2, 10)
# edgeAdder(G, 1, 4, 10)
# edgeAdder(G, 2, 3, 10)
# edgeAdder(G, 3, 4, 10)

# write_to_file(G)

G=graphGenerator(50, 300)
nx.write_graphml(G, 'testInputs')



>>>>>>> 2bd1c756f982e0586b94919e732bb6fc209c8aca

#takes in numbers n,k and creates a random graph with n vertices and k edges. Returns graph G
def graphGenerator(n, k):
	G = nx.Graph()
	for i in np.arange(n):
		r = random.randint(10, 100)
		nodeAdder(G, i, r)

	for j in np.arange(k):
		v = random.randint(0, n)
		u = random.randint(0, n)
		r = random.randint(10, 100)
		if u != v:
			edgeAdder(G, u, v, r)

	AL = nx.to_numpy_matrix(G)
	nx.draw_networkx(G)
	return G

#takes in a graph G and numbers n,k and creates a random graph around G with n vertices and k edges. Returns new graph H
#def graphGenerator(G, n, k):
	#H = G

# G = nx.Graph()
# nodeAdder(G, 0, 20)
# nodeAdder(G, 1, 5)
# nodeAdder(G, 2, 30)
# nodeAdder(G, 3, 30)
# nodeAdder(G, 4, 30)
# edgeAdder(G, 0, 1, 20)
# edgeAdder(G, 0, 3, 5)
# edgeAdder(G, 1, 3, 10)
# edgeAdder(G, 1, 2, 10)
# edgeAdder(G, 1, 4, 10)
# edgeAdder(G, 2, 3, 10)
# edgeAdder(G, 3, 4, 10)

# write_to_file(G)

G=graphGenerator(50, 300)
nx.write_graphml(G, 'testInputs')


