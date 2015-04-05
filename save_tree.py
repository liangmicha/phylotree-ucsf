import gen_tree
import cPickle

from optparse import OptionParser

def main():
    # should be able to cPickle this.

    depth = 5 # depth of tree
    mean_ins = 6 # mean length of insertions
    var_ins = 2 # variance for length of insertions
    p_mutation = 0.0 # prob of a mutation (per base)
    p_del = 0.0 # prob of deletion
    mean_del = 4 # mean length of deletion
    var_del = 2 #variance for length of deletion

    parser = OptionParser()
    parser.add_option('-f', dest='fname', help='name of pkl file')
    (options, args) = parser.parse_args()


    tree = gen_tree.generate_tree(depth, mean_ins, var_ins, p_mutation, p_del, mean_del, var_del)
    f = open(options.fname, 'wb')
    

    cPickle.dump( tree, f )
    f.close()

if __name__ == '__main__':
	main()