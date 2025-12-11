
# testing function to get all possible k-elt subsets of a set
# written in util

import utils
import odd_graph_generator as odd_gen

k = 5
odd_graph = odd_gen.OddGraph(k)

# # lis == largest_independent subset
# lis = odd_gen.get_all_subsets_containing_x(1, odd_graph.vertex_set)
# # wanna get all k elt subsets of above list
# k_elt_subsets_of_lis = utils.get_k_elt_subsets(k, lis);

# print("Largest independent subset:")
# print(lis, sep="\n\n")
# print(f"All {k}-elt subsets of largest independent subset (size {len(lis)})")
# print(f"There are {len(k_elt_subsets_of_lis)} in total {k}-elt subsets of the largest independent subset")
# for subset in k_elt_subsets_of_lis:
#     print(subset)

set_size = 6
subset_size = 4
test_set = [i for i in range(set_size)]
subsets = utils.get_k_elt_subsets(subset_size, test_set)
print(f"All {subset_size} elt subsets of {set_size} elt set {str(test_set)}, in total {len(subsets)}")
for s in subsets:
    print(s)