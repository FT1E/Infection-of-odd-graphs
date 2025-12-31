# usage
# import odd_graph_generator as odd_gen


# # for generating an odd graph k, in place of k below, give some positive integer
# odd_graph = odd_gen.OddGraph(k)

# # accessing vertex list and edge lists
# print(odd_graph.vertex_list) 
# print(odd_graph.edge_list)
# # note that edge list is just an unordered list of all edges

def get_odd_graph_k_vertices(k):
    set_size = 2*k - 1
    subset_size = k - 1
    # one_bit_1 == one_elt_subsets  # past variable name
    one_elt_subsets = []
    for i in range(set_size):
        one_elt_subsets.append(1 << i)

    # k_bits_1 == k_elt_subsets # past variable name
    k_elt_subsets = one_elt_subsets

    # k_plus_1_bits_1 == k_plus_1_elt_subsets
    k_plus_1_elt_subsets = []

    for m in range(subset_size - 1):
        for i in range(len(k_elt_subsets)):
            for j in range(len(one_elt_subsets)):
                #  and (k_bits_1[i] & one_bit_1[j]) == 0
                # past version had above but it's unnecessary
                if one_elt_subsets[j] > k_elt_subsets[i]:
                    k_plus_1_elt_subsets.append(k_elt_subsets[i] | one_elt_subsets[j])
        k_elt_subsets = k_plus_1_elt_subsets
        k_plus_1_elt_subsets = []

        # # Debugging below
        # print("With " + str(m+2) + " bits set to 1:\n - vertex count = " + str(len(k_elt_subsets)))
        # for num in k_elt_subsets:
        #     print(format(num, f"0{set_size}b"))
        # print("END\n")
    return k_elt_subsets


def get_edge_list(vertex_list):
    edge_list = []
    for i in range(len(vertex_list)):
        for j in range(i+1, len(vertex_list)):
            if (vertex_list[i] & vertex_list[j]) == 0:
                edge_list.append([vertex_list[i], vertex_list[j]])

    return edge_list

def get_vertex_number(subset_list):
    vertex_number = 0
    for number in subset_list:
        vertex_number += (1 << (number - 1))
    return vertex_number

def get_all_subsets_containing_x(x, vertex_list):
    bit = (1 << (x-1))
    subset_list = []
    for vertex in vertex_list:
        if vertex & bit != 0:
            subset_list.append(vertex)
    return subset_list

# get neighbours of a vertex in odd graph k
def get_vertex_neighbours(k, vertex, exclude_vertex=None, exclude_list=[]):
    # list of all elements not included in the vertex's subset
    complete_list = 0
    for i in range(2*k-1):
        complete_list = complete_list | (1 << i)
    exclusion_list = complete_list ^ vertex
    neighbour_list = []
    for i in range(2*k-1):
        if ((1 << i) & exclusion_list) != 0:
            neighbour = exclusion_list ^ (1 << i)
            if neighbour != exclude_vertex:
                neighbour_list.append(neighbour)
    return neighbour_list


class OddGraph:
    def __init__(self, k):
        self.k = k
        self.vertex_set = get_odd_graph_k_vertices(k)
#         each vertex as binary integer represents a k-1 elt subset of 2k-1 elt sets
#         the bits of each number correspond to which elements are in the subset (bit 1 is, bit 0 isn't)
#         so basically all numbers with k-1 bits set to 1 up to 2k-1 max bits
#         bits > (2k-1) are set to 0
        self.edge_list = get_edge_list(self.vertex_set)

