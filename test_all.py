# tests for odd graph k, all possible vertex subsets (of the largest independent subset) of size j
# stops once it finds one valid solution which it infects the whole graph
# no point in running further, since all the test cases have an initial infected subset of the same size
# if no value for j is given, the default value is (previous_minimum_found - 1)


# usage python3 test_all.py <k> [<j>] 
# in place of <k> write a number, which is taken as a k value for the odd graph k
# don't pass a number higher than 10, will take too much time
# j = expected minimum size of initial vertex subset to be infected

import random
import odd_graph_generator as odd_gen
import graph_infection_simulator as i_sim
import sys
import csv
import json
from datetime import datetime
import utils
from itertools import combinations


if len(sys.argv) > 1:
    k = int(sys.argv[1])
else:
    sys.exit(1)    

program_start_time = datetime.now()

# names of the columns in the .csv file
csv_fields = ['min_vertex_count', 'json_init_infection_list']




t1_gen = datetime.now()
if k < 8:
    odd_graph = odd_gen.OddGraph(k)
    odd_graph = {'vertex_set': odd_graph.vertex_set, 'edge_list': odd_graph.edge_list}
else:
    with open(f"/home/studenti/famnit/89231028//graph_theory_project/git/json_graphs/odd{k}.json", 'r') as rfile:
        odd_graph = json.loads(rfile.read())
t2_gen = datetime.now()

t1_subset_find = datetime.now()
subsets_containing_1 = odd_gen.get_all_subsets_containing_x(1, odd_graph['vertex_set'])
t2_subset_find = datetime.now()

minimum = len(subsets_containing_1)

min_found = minimum
# read the csv file to see if there is a minimum found
# not bothering with locks here since it's just reading
with open(f"/home/studenti/famnit/89231028//graph_theory_project/git/data/odd{k}.csv", 'r') as read_file:
    csv_reader = csv.DictReader(read_file)
    for row in csv_reader:
        min_found = int(row['min_vertex_count'])

expected_minimum = min_found

t1_main = datetime.now()
if len(sys.argv) > 2:
    expected_minimum = int(sys.argv[2])

# to save which vertex subset (initially only them infected) infected the rest of the graph
vertex_subset = []



# test all subsets of largest independent subset (all vertex/subsets which contain 1) of size expected_minimum
# subset_indexes = utils.get_k_elt_subsets(expected_minimum, subsets_containing_1)
# print(f"Total number of subsets being tested: {len(subset_indexes)}")

count = 0

print('Tested in crontab, run once - output saved in nohup.out')


t1_s = datetime.now()
for vertex_subset in combinations(subsets_containing_1, (expected_minimum)):
    # print(vertex_subset)
    # continue
    
    i_graph = i_sim.InfectedGraph(odd_graph['vertex_set'], odd_graph['edge_list'])
    
    # print(f"Simulating infection with {str(vertex_subset)}")
    for vertex in vertex_subset:
        i_graph.set_infected_vertex(vertex)
    i_graph.simulate_infection()
    
    result = i_graph.is_graph_infected()
    
    if result:
        count += 1

        minimum = expected_minimum
        # vertex_subset = [subsets_containing_1[index] for index in subset_index]
        
        # get out since all subsets are of the same size   
        print(f"Found infection with {expected_minimum} infeceted vertices on odd graph {k}")
        print(f"Initial infected vertex set: {vertex_subset}")

        # write result to file
        # then stop, since all subsets are of the same size here
        with open(f"/home/studenti/famnit/89231028//graph_theory_project/git/data/odd{k}.csv.lock", 'r') as lock:
            # got lock on file
            # first read to see if maybe another process got a better result
            with open(f"/home/studenti/famnit/89231028//graph_theory_project/git/data/odd{k}.csv", 'r') as read_file:
                csv_reader = csv.DictReader(read_file)
                keep_trying = False
                for row in csv_reader:
                    if int(row['min_vertex_count']) <= minimum:
                        keep_trying = True
                if keep_trying:
                    break
            # else if this process has better result then write it
            with open(f"/home/studenti/famnit/89231028//graph_theory_project/git/data/odd{k}.csv", 'w') as write_file:
                csv_writer = csv.writer(write_file)
                csv_writer.writerow(csv_fields)
                csv_writer.writerow([minimum, vertex_subset])
        break
        
t2_s = datetime.now()

print(f"Time it took to go through all combinations without printing or at least until a viable solution was found: {str(t2_s - t1_s)}")