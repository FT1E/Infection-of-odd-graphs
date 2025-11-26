
from graph_visualizor import GraphVisualization as GV



def get_odd_graph_k_vertices(k):
    set_size = 2*k - 1
    subset_size = k - 1
    one_bit_1 = []
    for i in range(set_size):
        one_bit_1.append(1 << i)
    # k_bits_1 now holds all numbers with 1 bit set 1
    k_bits_1 = one_bit_1
    k_plus_1_bits_1 = []

    for m in range(subset_size - 1):
        for i in range(len(k_bits_1)):
            for j in range(len(one_bit_1)):
                if one_bit_1[j] > k_bits_1[i] and (k_bits_1[i] & one_bit_1[j]) == 0:
                    k_plus_1_bits_1.append(k_bits_1[i] | one_bit_1[j])
        k_bits_1 = k_plus_1_bits_1
        k_plus_1_bits_1 = []
        # print("With " + str(m+2) + " bits set to 1:\n - edge count = " + str(len(k_bits_1)))
        # for num in k_bits_1:
        #     print(format(num, '09b'))
        # print("END\n")
    return k_bits_1

get_odd_graph_k_vertices(5)

def get_edge_list(vertex_list):
    edge_list = []
    for i in range(len(vertex_list)):
        for j in range(i+1, len(vertex_list)):
            if (vertex_list[i] & vertex_list[j]) == 0:
                edge_list.append([vertex_list[i], vertex_list[j]])

    return edge_list

class OddGraph:
    def __init__(self, k):
        self.k = k
        self.vertex_set = get_odd_graph_k_vertices(k)
#         each vertex as binary integer represents a k-1 elt subset of 2k-1 elt sets
#         the bits of each number correspond to which elements are in the subset (bit 1 is, bit 0 isn't)
#         so basically all numbers with k-1 bits set to 1 up to 2k-1 max bits
#         bits > (2k-1) are set to 0
        self.edge_list = get_edge_list(self.vertex_set)


# odd_graph_5 = OddGraph(3)
# example_vis_graph = GV()
# example_vis_graph.set_edge_list(odd_graph_5.edge_list)
# example_vis_graph.visualize()