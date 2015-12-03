#dijkstra for 1000 nodes in  graph lab
import graphlab

print "-----Nodes: 1000-----"
g = graphlab.load_graph('../dataset/pr_1000.txt', format='snap')
sp = graphlab.shortest_path.create(g, source_vid=1)
sp_sframe = sp['distance']
sp_sframe
print "---------------------"
sp_sframe
sp_sframe.print_rows(100,3)
print "----above are the first 100 computed vertices-----"
