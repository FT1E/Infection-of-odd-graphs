# more structured way like this with main.py
# so other files just contain functions and classes/methods for doing stuff

# usage:
# python3 main.py <k> [<test_count>] [<starting_min>]
# in place of <k> write a number, which is taken as a k value for the odd graph k
# don't pass a number higher than 10, will take too much time
# <test_count> is 3rd optional arg to set how many times the program should try to test
# <starting_min> is an optional arg, specifying a starting upper bound number for how many initial infected vertices there should be
# the script will then try to infect the graph with 1 less, and 1 less, as long as the whole graph is infected at the end
# if not given it will start with (2k-2 choose k-2), number of all vertices containing the element 1

import random
import odd_graph_generator as odd_gen
import graph_infection_simulator as i_sim
import sys
import csv


if len(sys.argv) > 1:
    k = int(sys.argv[1])
else:
    sys.exit(1)    

# names of the columns in the .csv file
csv_fields = ['min_vertex_count', 'json_init_infection_list']

test_count = 10
if len(sys.argv) > 2:
    test_count = int(sys.argv[2])



odd_graph = odd_gen.OddGraph(k)
subsets_containing_1 = odd_gen.get_all_subsets_containing_x(1, odd_graph.vertex_set)
minimum = len(subsets_containing_1)

if len(sys.argv) > 3:
    minimum = int(sys.argv[3])

# to save which vertex subset (initially only them infected) infected the rest of the graph
vertex_subset = []


min_found = minimum
# read the csv file to see if there is a minimum found
# not bothering with locks here since it's just reading
with open(f"data/odd{k}.csv", 'r') as read_file:
    csv_reader = csv.DictReader(read_file)
    for row in csv_reader:
        min_found = int(row['min_vertex_count'])

for _ in range(test_count):
    random.shuffle(subsets_containing_1)

    for initial_infection_cnt in range(minimum, 0, -1):
        i_graph = i_sim.InfectedGraph(odd_graph.vertex_set, odd_graph.edge_list)
        i_graph.set_infected_vertices(subsets_containing_1[:initial_infection_cnt])
        i_graph.simulate_infection()

        result = i_graph.is_graph_infected()

        if result:
            minimum = initial_infection_cnt
            vertex_subset = subsets_containing_1[:initial_infection_cnt]
        else:
            # only when it hits false
            # try to write to the file
            # with results from last iteration
            # it's too many writes if I put this in the if above
            # break out of loop after

            # write result to file
            with open(f"data/odd{k}.csv.lock", 'r') as lock:
                # got lock on file
                # first read to see if maybe another process got a better result
                with open(f"data/odd{k}.csv", 'r') as read_file:
                    csv_reader = csv.DictReader(read_file)
                    keep_trying = False
                    for row in csv_reader:
                        if int(row['min_vertex_count']) <= minimum:
                            keep_trying = True
                    if keep_trying:
                        continue
                # else if this process has better result then write it
                with open(f"data/odd{k}.csv", 'w') as write_file:
                    csv_writer = csv.writer(write_file)
                    csv_writer.writerow(csv_fields)
                    csv_writer.writerow([minimum, vertex_subset])
                    
            break

