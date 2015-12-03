#pagerank for 36000 nodes in  graph lab
import graphlab
print "-----Nodes: 36692 Edges: 367662-----"
g = graphlab.load_graph('http://snap.stanford.edu/data/email-Enron.txt.gz', format='snap')
pr = graphlab.pagerank.create(g)
pr_out = pr['pagerank']
print "---------------------"
pr_out
pr_out.print_rows(100,3)
print "----above are the first 100 computed vertices-----"
