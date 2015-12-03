#pagerank for 1 million nodes in  graph lab
import graphlab
print "-----1000 node Dataset-----"
g = graphlab.load_graph('../dataset/pr_1000.txt', format='snap')
pr = graphlab.pagerank.create(g)
pr_out = pr['pagerank']
print "---------------------"
pr_out
pr_out.print_rows(100,3)
print "----above are the first 100 computed vertices-----"
