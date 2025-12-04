
import odd_graph_generator as og

class InfectedGraph:

    def __init__(self, vertex_set, edge_list):
        self.vertex_set = vertex_set
        self.infected_vertices = dict()
        for vertex in self.vertex_set:
            self.infected_vertices[vertex] = False
#         by default no vertex is infected
        self.edge_list = edge_list
        self.infected = None

    def set_infected_vertex(self, vertex):
        self.infected_vertices[vertex] = True

    def set_infected_vertices(self, vertex_subset):
        for vertex in vertex_subset:
            self.infected_vertices[vertex] = True

    # TODO - Improve this algorithm a bit
    def simulate_infection(self):

        change=True
        infected_vertex_count = dict()
        while change:
            change = False
            for vertex in self.vertex_set:
                infected_vertex_count[vertex] = 0

            infection_spread_vertex = None
            for edge in self.edge_list:
                if self.infected_vertices[edge[0]] == self.infected_vertices[edge[1]]:
                    continue
                elif self.infected_vertices[edge[1]]:
                    infection_spread_vertex = edge[0]
                else:
                    infection_spread_vertex = edge[1]
                infected_vertex_count[infection_spread_vertex] += 1
                if infected_vertex_count[infection_spread_vertex] >= 2:
                    self.infected_vertices[infection_spread_vertex] = True
                    change = True



    def is_graph_infected(self):
        # if it's already infected
        if self.infected == True:
            return True

        # if it wasn't wholly infected
        # you could set one more vertex to be infected
        # then simulate infection again
        # so yeah that's why it has these 2 blocks (little bit of memoization)
        for vertex in self.infected_vertices:
            if not self.infected_vertices[vertex]:
                return False
        self.infected = True
        return True

