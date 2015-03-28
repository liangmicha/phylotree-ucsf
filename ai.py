""" Algorithms for choosing best tree. 
Split into parts.
"""

import collections
import math
import matplotlib.pyplot as plt

def optimal_length_of_parent(leaves):
	"""
	Takes a list of lists of integers (list of leaves)
	Returns a list of integers representing the common ancestor among the leaves.
	"""

	pass

	
def entropy_leaves(leaves, save_fig=False):
	# leaves is a list of lists of integers in [0, 3].
	# returns list of floats representing entropy.

	# get min_length of leaves, we don't care about the rest for now.
	min_length = float('inf')
	for leaf in leaves:
		min_length = min(min_length, len(leaf))
	num_leaves = len(leaves)

	entropy = []
	confidence = []
	counts_all = []
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
		counts_all.append(counts.copy())

	positions = list(xrange(min_length))
	if save_fig:
		plt.scatter(positions, confidence)
		plt.savefig('figures/plot_confidence.png', format='png')
		plt.clf()

		plt.scatter(positions, entropy)
		plt.savefig('figures/plot_entropy.png', format='png')
		plt.clf()

	
	return confidence, entropy, min_length, counts_all