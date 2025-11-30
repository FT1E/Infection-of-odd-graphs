import random

import odd_graph_generator as og

class InfectedGraph:

    def __init__(self, vertex_set, edge_list):
        self.vertex_set = vertex_set
        self.infected_vertices = dict()
        for vertex in self.vertex_set:
            self.infected_vertices[vertex] = False
#         by default no vertex is infected
        self.edge_list = edge_list

    def set_infected_vertex(self, vertex):
        self.infected_vertices[vertex] = True


    # TODO - Improve this algorithm a bit
    def simulate_infection(self):



        change=True
        while change:
            change = False
            infected_vertex_count = dict()
            for vertex in self.vertex_set:
                infected_vertex_count[vertex] = 0

            for edge in self.edge_list:
                if self.infected_vertices[edge[0]] == self.infected_vertices[edge[1]]:
                    continue
                elif self.infected_vertices[edge[1]]:
                    infected_vertex_count[edge[0]] += 1
                else:
                    infected_vertex_count[edge[1]] += 1

            for vertex in infected_vertex_count:
                if infected_vertex_count[vertex] >= 2:
                    self.infected_vertices[vertex] = True
                    change = True
                    # print('new infected vertex' + str(vertex))

    def is_graph_infected(self):
        for vertex in self.infected_vertices:
            if not self.infected_vertices[vertex]:
                return False
        return True


print("Infecting odd graph 10 by setting all vertices/subsets which contain 1 to be infected:")
odd_graph = og.OddGraph(5)

subsets_containing_1 = og.get_all_subsets_containing_x(1, odd_graph.vertex_set)
minimum = len(subsets_containing_1)
vertex_subset_winner = []

for gamble in range(100):
    random.shuffle(subsets_containing_1)
    for i in range(len(subsets_containing_1)):
        print("\tSimulating infection with " + str(len(subsets_containing_1) - i) + " initial infected vertices")

        i_graph = InfectedGraph(odd_graph.vertex_set, odd_graph.edge_list)
        current_infection_count = len(subsets_containing_1) - i
        for j in range(current_infection_count):
            i_graph.set_infected_vertex(subsets_containing_1[j])

        i_graph.simulate_infection()
        result = i_graph.is_graph_infected()
        print("\tResult:" + str(result))
        if not result:
            if current_infection_count + 1 < minimum:
                minimum = current_infection_count + 1
                vertex_subset_winner = subsets_containing_1[:minimum]
            break
    print("Minimum of " + str(gamble+1) + " gambles so far: " + str(minimum))
    print("Minimum vertex subset winner: " + str(vertex_subset_winner))