Open the files to read how to use them. 
Usage is described at the top of the file in comments
Core files:
- odd_graph_generator.py - for generating odd graph with value k, or rather the vertex set and the edge set for that graph
- graph_infection_simulator.py - for simulating the infection, passing as arguments a list of vertices, and a list of edges (list of 2-lenght lists/pairs, not matrix or adjacency list)
- main.py - testing a certain amount of random test cases - basically random subsets of the largest independence subset (of the vertices) of size equal or smaller to the previous minimum found
- r2_test.py - testing infection of a graph by infecting all vertices at distance 2 from the vertex {1, 2, ..., k-1} (can be any arbitrary vertex, since it's distance regular)
- test_all.py - to test every possible subset of largest independence subset of size equal to the argument passed, or if ommited size is (previous_minimum_found - 1)
