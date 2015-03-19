import numpy as np
import random

# DICTIONARY MAPPING numbers to bases.
NUM_TO_BASE = {
	0: 'A',
	1: 'C',
	2: 'G',
	3: 'T'
}

MUTATION_HELPER = {
	0: [1, 2, 3],
	1: [0, 2, 3],
	2: [0, 1, 3],
	3: [0, 1, 2],
}

# Dictionary encoding mutation rates. We can do this later. I think the probability of
# transitioning between A <-> T vs C <-> G should be different.
MUTATION_MATRIX = {} # Not used for now.

def fn_deletion(p_del, mean, var, del_min, del_max):
	""" with probability p_del, we will delete X characters.
	    X ~ gaussian(mean, del_var) that is restrict to be in [del_min, del_max]

	    returns a number that represents number of deletions.
	"""
	pass

def mutate(node, p_mutation):
	result = []
	for i in node:
		if random.random < p_mutation:
			result.append(random.choice(MUTATION_HELPER[i]))
		else:
			result.append(i)
	return result

def make_children(tag1, tag2, node, p_mutation, del_fn):
	# node is a list
	# output is two lists
	c1 = mutate(node, p_mutation)
	c2 = mutate(node, p_mutation)

	n_del_c1 = del_fn()
	n_del_c2 = del_fn()
	c1_index_end = len(c1) - n_del_c1
	c2_index_end = len(c2) - n_del_c2

	c1_result = c1[:c1_index_end] + tag1
	c2_result = c2[:c2_index_end] + tag2
	return c1_result, c2_result


def stringify(node):
	# convert list of numbers to characters.
	result = ''
	for i in node:
		result += NUM_TO_BASE[i]

def print_tree(tree):
	depth = len(tree)
	for i in range(depth):
		print 'printing depth %s' %(i)
		spaces = ' '*i
		for node in tree[i]:
			print '%s %s'%(spaces, stringify(node))

def generate_tree(depth, p_mutation=mutation_matrix, del_fn=fn_deletion):
	tree = []
	parent_tag = [3, 1, 3, 2, 0, 2] # == 'TATGAG'
	tree.append(parent_tag)
	for i in range(depth):
		print 'depth: %s' %(i)
		for node in tree[i]:
			lst = []
			tree.append(lst)
			# create the two children, append to the list at i + 1.
			c1, c2 = make_children(tag1, tag2, list(node), p_mutation, del_fn)
			lst.append(c1)
			lst.append(c2)
		
	print_tree(tree)



def main():
	# Experiment with sampling.



if __name__ == '__main__':
	main()