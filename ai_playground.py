import pdb

import gen_tree
import ai


def construct_counts_dict(counts_dict, lst):
	pass
def count_values_within_half(counts_dict, epsilon=0.1):
	num_within_half = 0
	char1 = None
	char2 = None
	for key, prob in counts_dict.iteritems():
		if abs(0.5 - prob) <= epsilon:
			num_within_half += 1
			if char1 == None:
				char1 = key
			elif char2 == None:
				char2 = key
	return char1, char2, num_within_half


def infer_parent(leaves):
	confidence, _, min_length, counts_all = ai.entropy_leaves(leaves, True)
	
	parent = []
	split_index = None
	for i in range(min_length):
		# normalize counts_all
		for key, prob in counts_all[i].iteritems():
			counts_all[i][key] *= 1.0/len(leaves)

		print i, confidence[i], counts_all[i]
		char1, char2, num_near_half = count_values_within_half(counts_all[i])
		if num_near_half == 2:
			print 'found split point.'
			split_index = i
			break
		else:
			best_character = None
			prob_max = 0.0
			for key, prob in counts_all[i].iteritems():
				if prob > prob_max:
					prob_max = prob
					best_character = key
			parent.append(best_character)
	return parent, split_index, char1, char2

def main():
	depth = 5 # depth of tree
	mean_ins = 6 # mean length of insertions
	var_ins = 4 # variance for length of insertions
	p_mutation = 0.001 # prob of a mutation (per base)
	p_del = 0.20 # prob of deletion
	mean_del = 4 # mean length of deletion
	var_del = 2 #variance for length of deletion

	tree = gen_tree.generate_tree(depth, mean_ins, var_ins, p_mutation, p_del, mean_del, var_del)
	leaves = tree[-1]

	parent, split_index, char1, char2 = infer_parent(leaves)

	actual_parent = gen_tree.stringify(tree[0][0])
	guessed_parent = gen_tree.stringify(parent)
	print 'actual parent: %s' %(actual_parent)
	print 'guessed parent: %s' %(guessed_parent)
	
	if guessed_parent.startswith(actual_parent):
		print 'yay :)'

	# Now that we've done the parent, let's split the rest of the strings, and
	# cluster them.
 
 	# simple binning method
 	bin1 = []
 	bin2 = []
 	other = [] #weird case.
 	for leaf in leaves:
 		if leaf[split_index] == char1:
 			bin1.append(leaf[split_index:])
 		elif leaf[split_index] == char2:
 			bin2.append(leaf[split_index:])
 		else:
 			other.append(leaf[split_index:])
 	print char1, char2
 	print len(bin1), len(bin2), len(other)


 	print 'bin1  : %s\n' %(bin1[0])
 	print 'bin2  : %s\n' %(bin2[0])
 	print 'other :\n'
 	for o in other:
 		print '        %s\n'%(other[0])

 	gen_tree.print_tree(tree)


		




if __name__ == '__main__':
	main()