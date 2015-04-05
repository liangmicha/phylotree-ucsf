import gen_tree
import cPickle

from optparse import OptionParser

def main():
    parser = OptionParser()
    parser.add_option('-f', dest='fname', help='name of pkl file', default='test_tree.pkl')
    (options, args) = parser.parse_args()


    f = open(options.fname, 'rb')
    tree = cPickle.load(f)
    f.close()
    gen_tree.print_tree(tree)

if __name__ == '__main__':
	main()