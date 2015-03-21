import numpy as np
import random

# NUM_ALPHABET
NUM_ALPHABET = [0, 1, 2, 3]
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

def fn_deletion(p_del, mean, var, del_min, del_max, max_iter=10):
	""" with probability p_del, we will delete X characters.
	    X ~ gaussian(mean, del_var) that is restrict to be in [del_min, del_max]

	    returns a number that represents number of deletions.
	"""
	if random.random() > p_del:
		return 0
	else:
		i = 0
		while i < max_iter:
			sample = int(round(np.random.normal()*var + mean))
			if sample >= del_min and sample <= del_max:
				return sample
		print 'weird... did not find a good sample within range [%s, %s]' %(del_min, del_max)
		return 0

def mutate(node, p_mutation):
	result = []
	for i in node:
		if random.random() < p_mutation:
			result.append(random.choice(MUTATION_HELPER[i]))
		else:
			result.append(i)
	return result

def make_children(tag1, tag2, node, p_mutation, p_del, mean_del, var_del, del_min, del_max):
	# node is a list
	# output is two lists
	c1 = mutate(node, p_mutation)
	c2 = mutate(node, p_mutation)

	n_del_c1 = fn_deletion(p_del, mean_del, var_del, del_min, del_max)
	n_del_c2 = fn_deletion(p_del, mean_del, var_del, del_min, del_max)
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
	return result

def print_tree(tree):
	depth = len(tree)
	for i in range(depth):
		print 'printing depth %s' %(i)
		spaces = ' '*i
		for node in tree[i]:
			print '%s %s'%(spaces, stringify(node))

def gen_tag(mean, var):
	# sample from a normal distribution
	# N(mean, var)
	length = np.random.normal()*var + mean
	values = []
	for _ in range(int(round(length))):
		values.append(random.choice(NUM_ALPHABET))
	return values



def generate_tree(depth, mean_ins, var_ins, p_mutation=0.05, p_del=0.05, mean_del=2, var_del=1):
	tree = []
	parent_tag = [3, 1, 3, 2, 0, 2] # == 'TATGAG'
	tree.append([parent_tag])
	del_min = 0
	for i in range(depth):
		print '  depth: %s' %(i)
		lst = []
		for node in tree[i]:
			# create the two children, append to the list at i + 1.
			tag1 = gen_tag(mean_ins, var_ins)
			tag2 = gen_tag(mean_ins, var_ins)
			# this should be max number of characters in the node.
			del_max = len(node)
			c1, c2 = make_children(tag1, tag2, list(node), p_mutation, p_del, mean_del, var_del, del_min, del_max)
			lst.append(c1)
			lst.append(c2)
		tree.append(list(lst))
		print tree
		print '  done printing depth'
	# printing tree
	print 'pritning tree now.'
	print_tree(tree)



def main():
	# Experiment with sampling.
	depth = 5
	mean_ins = 3
	var_ins = 0
	p_mutation = 0
	p_del = 0.05
	mean_del = 2
	var_del = 1
	generate_tree(depth, mean_ins, var_ins, p_mutation=0.05, p_del=0.05, mean_del=2, var_del=1)


if __name__ == '__main__':
	main()