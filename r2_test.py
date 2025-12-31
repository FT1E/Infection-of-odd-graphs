# tests infection by infecting all vertices at distance 2 from the vertex {1, 2, ... k-1} (vertex is arbitrarilly chosen, could be any vertex since it's distance regular)


# usage python3.py <k>  
# in place of <k> write a number, which is taken as a k value for the odd graph k
# don't pass a number higher than 10, will take too much time

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

# t1_subset_find = datetime.now()
# subsets_containing_1 = odd_gen.get_all_subsets_containing_x(1, odd_graph['vertex_set'])
# t2_subset_find = datetime.now()

# minimum = len(subsets_containing_1)

# min_found = minimum
# # read the csv file to see if there is a minimum found
# # not bothering with locks here since it's just reading
# with open(f"/home/studenti/famnit/89231028//graph_theory_project/git/data/odd{k}.csv", 'r') as read_file:
#     csv_reader = csv.DictReader(read_file)
#     for row in csv_reader:
#         min_found = int(row['min_vertex_count'])

# expected_minimum = min_found
# if len(sys.argv) > 2:
#     expected_minimum = int(sys.argv[2])

t1_main = datetime.now()

# to save which vertex subset (initially only them infected) infected the rest of the graph
vertex = odd_gen.get_vertex_number([i+1 for i in range(k-1)])
vertex_r1_neighbours = odd_gen.get_vertex_neighbours(k, vertex, exclude_vertex=vertex)
vertex_r2_neighbours = []
for neighbour in vertex_r1_neighbours:
    vertex_r2_neighbours += odd_gen.get_vertex_neighbours(k, neighbour, exclude_vertex=vertex)

# 
initial_infection_subset = vertex_r2_neighbours

i_graph = i_sim.InfectedGraph(odd_graph['vertex_set'], odd_graph['edge_list'])
i_graph.set_infected_vertices(initial_infection_subset)
i_graph.simulate_infection()
result = i_graph.is_graph_infected()

t2_main = datetime.now()

print(f"Whole graph infected == {result}")
print(f"Initial infection list == {initial_infection_subset}")

if result:

    minimum = len(initial_infection_subset)
    vertex_subset = initial_infection_subset

    # get out since all subsets are of the same size   
    print(f"Found infection with {minimum} infeceted vertices on odd graph {k}")
    print(f"Initial infected vertex set: {initial_infection_subset}")

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

        if not keep_trying:
            # else if this process has better result then write it
            with open(f"/home/studenti/famnit/89231028//graph_theory_project/git/data/odd{k}.csv", 'w') as write_file:
                csv_writer = csv.writer(write_file)
                csv_writer.writerow(csv_fields)
                csv_writer.writerow([minimum, vertex_subset])

print(f"Time it took == {str(t2_main - t1_main)}")