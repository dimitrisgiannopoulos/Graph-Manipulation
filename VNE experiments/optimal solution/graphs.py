# A simple program for finding the shortest path between two nodes of the GRnet network
# The GRnet graph in gml format can be found in http://www.topology-zoo.org/files/Grnet.gml
# GRnet's topology can be seen in http://www.topology-zoo.org/maps/Grnet.jpg

import networkx as nx   # For Graph manipulation and algorithm execution
import pylab            # For Graph plotting


# Define global parameters (nodes and links-per-node)
n = 50
m = 5

# Create a barabasi-albert-graph
G = nx.barabasi_albert_graph(n, m, seed=None, initial_graph=None)

# Show graph
pos=nx.spring_layout(G)
nx.draw(G,pos)
pylab.show()
