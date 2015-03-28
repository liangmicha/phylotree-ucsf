
import matplotlib.pyplot as plt

import ai
import gen_tree
# Exploratory Data Analysis





def main():
	depth = 3 # depth of tree
	mean_ins = 6 # mean length of insertions
	var_ins = 4 # variance for length of insertions
	p_mutation = 0.001 # prob of a mutation (per base)
	p_del = 0.05 # prob of deletion
	mean_del = 4 # mean length of deletion
	var_del = 2 #variance for length of deletion
	#tree = gen_tree.generate_tree(depth, mean_ins, var_ins, p_mutation, p_del, mean_del, var_del)
	#leaves = tree[-1]
	#ai.entropy_leaves(leaves)
	# for leaf in leaves:
	# 	print gen_tree.stringify(leaf)
	# gen_tree.print_tree(tree)

	# try to generate multiple trees and figure out the mean/var of the entropies at each position.
	N = 100 # generate 100 trees.
	entropies = [[] for i in range(100)]
	max_length = 0
	for i in range(N):
		print 'generating tree %s/%s' %(i, N)
		tree = gen_tree.generate_tree(depth, mean_ins, var_ins, p_mutation, p_del, mean_del, var_del)
		_, entropy, length, _ = ai.entropy_leaves(tree[-1])
		for base_position in range(length):
			entropies[base_position].append(entropy[base_position])
		max_length = max(max_length, length)
	# print len(entropies), max_length
	# plt.boxplot(entropies[:max_length], 0, 'rs', 1)
	# plt.show()






if __name__ == '__main__':
	main()


