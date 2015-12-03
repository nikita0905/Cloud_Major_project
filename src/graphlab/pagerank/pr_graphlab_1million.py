#pagerank for 1 million nodes in  graph lab
import graphlab
print "-----Youtube Dataset-----"
print "-----Nodes: 1134890 Edges: 2987624-----"
g = graphlab.load_graph('http://snap.stanford.edu/data/bigdata/communities/com-youtube.ungraph.txt.gz', format='snap')
pr = graphlab.pagerank.create(g)
pr_out = pr['pagerank']
print "---------------------"
pr_out
pr_out.print_rows(100,3)
print "----above are the first 100 computed vertices-----"