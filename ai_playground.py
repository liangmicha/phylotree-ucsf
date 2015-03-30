import pdb
import Queue

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
    # calculates list of entropies, returns count objects at each base position.
    confidence, _, min_length, counts_all = ai.entropy_leaves(leaves, True)
    
    parent = []
    split_index = None
    for i in range(min_length):
        # normalize counts_all
        for key, prob in counts_all[i].iteritems():
            counts_all[i][key] *= 1.0/len(leaves)

        print i, gen_tree.stringify([leaves[0][i]]), confidence[i], counts_all[i]
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
    # should be able to cPickle this.

    depth = 5 # depth of tree
    mean_ins = 6 # mean length of insertions
    var_ins = 4 # variance for length of insertions
    p_mutation = 0.0 # prob of a mutation (per base)
    p_del = 0.0 # prob of deletion
    mean_del = 4 # mean length of deletion
    var_del = 2 #variance for length of deletion

    tree = gen_tree.generate_tree(depth, mean_ins, var_ins, p_mutation, p_del, mean_del, var_del)

    # tree is a list of lists.
    # tree[0] is nodes at depth 0.
    # tree[1] is nodes at depth 1.
    # ...
    # tree[-1] is nodes at depth of the leaves.
    leaves = tree[-1]

    q = Queue.Queue()
    q.put(leaves)

    labels = [[] for _ in range(len(tree))]
    depth = 0

    # basically what I am doing is have a queue for "breadth first search".
    # each time I dequeue, a list of "leaves" will come out".
    # if number of leaves is more than 2, then I will need to split.
    # if number of leaves is equal to 2, then that is the pair.
    # 
    # I dequeue EVERYTHING from the queue every time (taking care of each node at depth)
    # which is why I have two while not q.empty() loops.
    while not q.empty():
        new_q = Queue.Queue()
        print 'depth: %s' %(depth)
        while not q.empty():
            ls = q.get() # get the leaves
            if len(ls) == 2:
                # This is the base case.
                labels[depth].append(ls)
            parent, split_index, char1, char2 = infer_parent(ls)
            guessed_parent = gen_tree.stringify(parent)
            print 'leaves: \n'
            for l in ls:
                print '  %s' %(gen_tree.stringify(l))
            print 'end leaves\n'
            print '     parent: %s\n     split_index: %s\n     char1: %s\n     char2: %s\n' %(
                    guessed_parent, split_index, char1, char2)
            labels[depth].append(guessed_parent)

            # Now that we've done the parent, let's split the rest of the strings, and
            # cluster them.
         
            # simple binning method
            bin1 = []
            bin2 = []
            other = [] #weird case.
            for leaf in ls:
                if leaf[split_index] == char1:
                    bin1.append(leaf[split_index:])
                elif leaf[split_index] == char2:
                    bin2.append(leaf[split_index:])
                else:
                    other.append(leaf[split_index:])
            print char1, char2
            print len(bin1), len(bin2), len(other)
            if len(bin1) == len(bin2) and len(other) == 0:
                # let's recursively do the rest now.
                new_q.put(bin1)
                new_q.put(bin2)

            else:
                print 'something wrong, not able to split into two relatively equal bins, WHY?'
                print 'bin1  : %s\n' %(bin1[0])
                print 'bin2  : %s\n' %(bin2[0])
                print 'other :\n'
                for o in other:
                    print '        %s\n'%(other[0])
                return None
            print '------\n'
        q = new_q
        depth += 1
    gen_tree.print_tree(tree)
    gen_tree.print_tree(labels)


        




if __name__ == '__main__':
    main()