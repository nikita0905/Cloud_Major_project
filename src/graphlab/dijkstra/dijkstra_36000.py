#dijkstra for 36000 nodes in  graph lab
import graphlab

print "-----Nodes: 36692 Edges: 367662-----"
g = graphlab.load_graph('http://snap.stanford.edu/data/email-Enron.txt.gz', format='snap')
sp = graphlab.shortest_path.create(g, source_vid=1)
sp_sframe = sp['distance']
sp_sframe
print "---------------------"
sp_sframe
sp_sframe.print_rows(100,3)
print "----above are the first 100 computed vertices-----"
