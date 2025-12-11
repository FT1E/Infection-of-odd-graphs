
def print_binary_represent_single(num, max_bits=19):
    print(format(num, 'b').zfill(max_bits))

def print_binary_represent_multi(list, max_bits=19):
    for elt in list:
        print_binary_represent_single(elt, max_bits=max_bits)

def get_k_elt_subsets(k, set, set_size=-1, extra_elts=[]):
    if set_size == -1:
        set_size = len(set)

    if k == set_size:
        return [[i for i in range(k)] + extra_elts]
    elif k == 2:
        res = []
        for i in range(set_size):
            for j in range(i+1, set_size):
                res.append([i, j] + extra_elts)
        return res
    else:
        # split recursively into
        #   1 - subsets including last elt
        #   2 - subsets not including last elt
        part_1 = get_k_elt_subsets(k - 1, set, set_size - 1, [set_size - 1] + extra_elts)
        part_2 = get_k_elt_subsets(k, set, set_size - 1, extra_elts)
        return part_1 + part_2


# subset = [263, 23, 45, 141, 75, 401, 147, 329]
#
# print_binary_represent_multi(sorted(subset), 9)