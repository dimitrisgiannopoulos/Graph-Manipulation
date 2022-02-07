# A simple program for finding the shortest path between two nodes of the GRnet network
# The GRnet graph in gml format can be found in http://www.topology-zoo.org/files/Grnet.gml
# GRnet's topology can be seen in http://www.topology-zoo.org/maps/Grnet.jpg

import networkx as nx   # For Graph manipulation and algorithm execution
import pylab            # For Graph plotting


# Copy the gml topology from the URL into G.gml and place it into the local directory
G = nx.read_gml("G.gml") 
pos=nx.spring_layout(G)
nx.draw(G,pos)
pylab.show()
print([p for p in nx.all_shortest_paths(G, source='Karditsa', target='Ioannina')])