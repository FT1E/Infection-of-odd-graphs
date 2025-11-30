
def print_binary_represent_single(num, max_bits=19):
    print(format(num, 'b').zfill(max_bits))

def print_binary_represent_multi(list, max_bits=19):
    for elt in list:
        print_binary_represent_single(elt, max_bits=max_bits)

subset = [263, 23, 45, 141, 75, 401, 147, 329]

print_binary_represent_multi(sorted(subset), 9)