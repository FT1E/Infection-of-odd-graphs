
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


odd_graph = og.OddGraph(3)
i_graph = InfectedGraph(odd_graph.vertex_set, odd_graph.edge_list)
i_graph.set_infected_vertex(3)
i_graph.set_infected_vertex(17)
i_graph.set_infected_vertex(9)
i_graph.set_infected_vertex(5)
i_graph.simulate_infection()

print(i_graph.is_graph_infected())
