# used for analysis on the computation results
# trying to find some pattern or something


import csv
import json
import utils as u

data = {}
with open(f"summary.json", 'r') as f:
    data = json.loads(f.read())

# data['9'] = None
# data['10'] = None
# print(data['3']['json_init_infection_list'][0])
for k in data:
    if data[k] is None:
        continue
    data[k]['json_init_infection_list'] = sorted(json.loads(data[k]['json_init_infection_list']))
    print(f"Odd graph {k}")
    print(f"Minimum initial infection count == {data[k]['min_vertex_count']}")
    print("XOR done on the initial infection subset:")
    print(format(u.listXOR(data[k]['json_init_infection_list']), 'b').zfill(2*int(k) - 1))
    # print("Initial infected vertex subset in binary form:")
    # u.print_binary_represent_multi(data[k]['json_init_infection_list'], 2*int(k) - 1)
    print('\n')