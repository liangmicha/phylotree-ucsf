import collections
import math
import matplotlib.pyplot as plt

import gen_tree
# Exploratory Data Analysis

def entropy_leaves(leaves):
	# leaves is a list of lists of integers in [0, 3].
	# returns list of floats representing entropy.

	# get min_length of leaves, we don't care about the rest for now.
	min_length = float('inf')
	for leaf in leaves:
		min_length = min(min_length, len(leaf))
	num_leaves = len(leaves)

	entropy = []
	confidence = []
	for i in range(min_length):
		counts = collections.Counter()
		# counts key = key.
		# counts value = count
		for leaf in leaves:
			counts[leaf[i]] += 1.0
		# Now let's calculate entropy.
		entropy_leaf = 0.0
		for _, count in counts.iteritems():
			prob = 1.0*count/num_leaves
			entropy_leaf -= prob*math.log(prob, 2)
		confidence.append(1.0*max(counts.values())/num_leaves)
		entropy.append(entropy_leaf)

	positions = list(xrange(min_length))
	
	plt.scatter(positions, confidence)
	plt.savefig('figures/plot_confidence.png', format='png')
	plt.clf()

	plt.scatter(positions, entropy)
	plt.savefig('figures/plot_entropy.png', format='png')
	plt.clf()



def main():
	depth = 10 # depth of tree
	mean_ins = 6 # mean length of insertions
	var_ins = 4 # variance for length of insertions
	p_mutation = 0.05 # prob of a mutation (per base)
	p_del = 0.05 # prob of deletion
	mean_del = 4 # mean length of deletion
	var_del = 2 #variance for length of deletion
	tree = gen_tree.generate_tree(depth, mean_ins, var_ins, p_mutation, p_del, mean_del, var_del)
	leaves = tree[-1]
	entropy_leaves(leaves)
	# for leaf in leaves:
	# 	print gen_tree.stringify(leaf)
	gen_tree.print_tree(tree)



if __name__ == '__main__':
	main()


