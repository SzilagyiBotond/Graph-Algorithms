import copy
from copy import deepcopy


class Graph:
    def __init__(self, vertices, file_name):
        self.__vertices = vertices
        self.__edges = 0
        self.__dicin = {}
        self.__dicout = {}
        self.__costs = {}
        self.__file_name = file_name
        for _ in range(self.__vertices):
            self.__dicin[_] = []
            self.__dicout[_] = []
        # self._load_file()

    def return_vertices(self):
        return list(self.__dicin.keys())

    def return_edges(self):
        return list(self.__costs.keys())

    def return_number_of_vertices(self):
        return len(self.__dicin.keys())

    def add_vertex(self, vertex):
        if not self.is_vertex(vertex):
            self.__vertices += 1
            self.__dicin[vertex] = []
            self.__dicout[vertex] = []
        else:
            raise GraphException("Vertex already added")

    def is_vertex(self, vertex):
        if vertex not in self.return_vertices():
            return False
        return True

    def is_edge(self, edge):
        if edge in self.return_edges():
            return True
        return False

    def add_edge(self, predecessor, successor, cost):
        # if not self.is_vertex(predecessor) or not self.is_vertex(successor):
        #     raise GraphException("Invalid predecessor or successor")
        edge = (predecessor, successor)
        # if not self.is_edge(edge):
        self.__costs[edge] = cost
        self.__dicin[successor].append(predecessor)
        self.__dicout[predecessor].append(successor)
        # else:
        #     raise GraphException("Edge already added")

    # def alternative_add(self, vertex1, vertex2, cost):
    #     edge = (vertex1, vertex2)
    #     self.__costs[edge] = cost
    #     self.__dicin[vertex2].append(vertex1)
    #     self.__dicin[vertex1].append(vertex2)
    #     self.__dicout[vertex2].append(vertex1)
    #     self.__dicout[vertex1].append(vertex2)

    def modify_cost(self, predecessor, successor, new_cost):
        edge = (predecessor, successor)
        if self.is_edge(edge):
            self.__costs[edge] = new_cost
        else:
            raise GraphException("Edge not found")

    def return_cost(self, predecessor, successor):
        edge = (predecessor, successor)
        if self.is_edge(edge):
            return self.__costs[edge]

    def remove_edge(self, predecessor, successor):
        edge = (predecessor, successor)
        if not self.is_vertex(predecessor) or not self.is_vertex(successor):
            raise GraphException("Invalid predecessor or successor")
        if self.is_edge(edge):
            self.__dicin[successor].remove(predecessor)
            self.__dicout[predecessor].remove(successor)
            del self.__costs[(predecessor, successor)]
        else:
            raise GraphException("Edge not found")

    def load_file(self):
        with open(self.__file_name, "r") as content:
            for lines in content:
                line = lines[:-1]
                data = line.split(" ")
                if len(data) == 2:
                    self.__vertices = int(data[0])
                    self.__edges = int(data[1])
                else:
                    self.add_edge(int(data[0]), int(data[1]), int(data[2]))

    def remove_vertex(self, vertex):
        if not self.is_vertex(vertex):
            raise GraphException("Vertex not found")
        if len(self.__dicin[vertex]) != 0:
            for predecessor in self.__dicin[vertex]:
                self.__dicout[predecessor].remove(vertex)
                del self.__costs[(predecessor, vertex)]
        if len(self.__dicout[vertex]) != 0:
            for successor in self.__dicout[vertex]:
                self.__dicin[successor].remove(vertex)
                del self.__costs[(vertex, successor)]
        del self.__dicin[vertex]
        del self.__dicout[vertex]

    def return_indegree(self, vertex):
        if self.is_vertex(vertex):
            return len(self.__dicin[vertex])
        raise GraphException("Vertex not found")

    def return_outdegree(self, vertex):
        if self.is_vertex(vertex):
            return len(self.__dicout[vertex])
        raise GraphException("Vertex not found")

    def set_of_inbound_edges(self, vertex):
        if self.is_vertex(vertex):
            inbound_edges = []
            if self.return_indegree(vertex) != 0:
                for predecessor in self.__dicin[vertex]:
                    inbound_edges.append((predecessor, vertex, self.__costs[(predecessor, vertex)]))
            return inbound_edges
        raise GraphException("Vertex not found")

    def set_of_outbound_edges(self, vertex):
        if self.is_vertex(vertex):
            outbound_edges = []
            if self.return_outdegree(vertex) != 0:
                for successor in self.__dicout[vertex]:
                    outbound_edges.append((vertex, successor, self.__costs[(vertex, successor)]))
            return outbound_edges
        raise GraphException("Vertex not found")

    def return_a_copy(self):
        copied_graph = copy.deepcopy(self)
        return copied_graph

    def save_graph(self, file_name):
        with open(file_name, "w") as f:
            for vertex in self.return_vertices():
                if len(self.__dicin[vertex]) == 0 and len(self.__dicout[vertex]) == 0:
                    f.write(f"{vertex} -1\n")
                elif len(self.__dicout[vertex]) != 0:
                    for edge in self.set_of_outbound_edges(vertex):
                        f.write(f"{edge[0]} {edge[1]} {edge[2]}\n")

    def alternative_read(self):
        with open(self.__file_name, "r") as content:
            for lines in content:
                line = lines[:-1]
                data = line.split(" ")
                if len(data) == 2:
                    if int(data[0]) not in self.__dicin.keys():
                        self.__dicin[int(data[0])] = []
                    if int(data[0]) not in self.__dicout.keys():
                        self.__dicout[int(data[0])] = []
                else:
                    if it(data[0]) not in self.__dicin.keys():
                        self.__dicin[int(data[0])] = []
                    if int(data[0]) not in self.__dicout.keys():
                        self.__dicout[int(data[0])] = []
                    if int(data[1]) not in self.__dicin.keys():
                        self.__dicin[int(data[1])] = []
                    if int(data[1]) not in self.__dicout.keys():
                        self.__dicout[int(data[1])] = []
                    self.add_edge(int(data[0]), int(data[1]), int(data[2]))

    def undirected_load(self):
        with open(self.__file_name, "r") as content:
            for lines in content:
                line = lines[:-1]
                data = line.split(" ")
                if len(data) == 2:
                    self.__vertices = int(data[0])
                    self.__edges = int(data[1])
                else:
                    if int(data[0]) not in self.__dicin.keys():
                        self.__dicin[int(data[0])] = []
                    if int(data[0]) not in self.__dicout.keys():
                        self.__dicout[int(data[0])] = []
                    if int(data[1]) not in self.__dicin.keys():
                        self.__dicin[int(data[1])] = []
                    if int(data[1]) not in self.__dicout.keys():
                        self.__dicout[int(data[1])] = []
                    self.add_edge(int(data[1]), int(data[0]), int(data[2]))
                    self.add_edge(int(data[0]), int(data[1]), int(data[2]))

    def DFS(self, visited, vertex, recent_connected_components: list):
        """

        :param visited: list, that holds the truth value, whether a vertex was visited or not
        :param vertex: current visited vertex
        :param recent_connected_components: list that holds the current connected components
        :return:
        """
        visited[vertex] = True  # The vertex is marked as visited
        recent_connected_components.append(vertex)  # The vertex is added to the current connected component list
        for v in self.__dicin[vertex]:
            if not visited[v]:
                recent_connected_components = self.DFS(visited, v,
                                                       recent_connected_components)  # We run recursively this modified DFS for a vertex that is connected to the initial one, and is not visited yet.
        return recent_connected_components  # We return the current connected component as a list

    def connected_components(self):
        visited = [False for _ in self.__dicin.keys()]  # we mark every vertex as not visited
        connected_components_list = []  # in this list we store the connected components as lists
        graphs = []  # in this list we store the connected components as graphs
        for vertex in self.__dicin.keys():
            if not visited[vertex]:
                cc = []  # This will hold the current connected component
                graph_1 = Graph(0,
                                "empty.txt")  # We create an empty graph object, to store the connected components as a graph
                connected_components_list.append(self.DFS(visited, vertex,
                                                          cc))  # We add to the connected component list the connected component we just found
                for vertex_1 in cc:  # in this for we add the vertices and edges to the graph from the connected component
                    if vertex_1 not in graph_1.__dicout.keys():
                        graph_1.__dicin[vertex_1] = []
                        graph_1.__dicout[vertex_1] = []
                    for v in self.__dicin[vertex_1]:
                        if v not in graph_1.__dicout.keys():
                            graph_1.__dicout[v] = []
                            graph_1.__dicin[v] = []
                        graph_1.add_edge(vertex_1, v, 1)
                graphs.append(graph_1)
        return connected_components_list, graphs

    def Bellman_Ford(self, source):
        father = [-1] * self.__vertices  # we set the fathers list -> everyone's father is -1(nonexistent)
        distance = [float("Inf")] * self.__vertices  # we set the distance to infinite to each vertex
        distance[source] = 0  # the distance to the source is set to 0
        for _ in range(self.__vertices - 1):  # we have at most nr_of_vertex iterations
            modification = False
            for start in self.__dicout.keys():
                for end in self.__dicout[start]:
                    if distance[start] != float("Inf") and self.__costs[(start, end)] + distance[start] < distance[
                        end]:  # if we find a better route to the end we update it
                        distance[end] = self.__costs[(start, end)] + distance[start]  # we update the distance to end
                        modification = True
                        father[end] = start  # the new father/predecessor of end is start
            if not modification:  # if no modification was made in the current iteration, we won't do another one, we return
                return distance, father
        for _ in range(
                self.__vertices - 1):  # we check if there is a negative cost cycle, and if there is we throw an exception
            for start in self.__dicout.keys():
                for end in self.__dicout[start]:
                    if distance[start] != float("Inf") and self.__costs[(start, end)] + distance[start] < distance[end]:
                        raise GraphException("There is a negative cost cycle")
        return distance, father  # we return the distance and father lists

    def find(self, parent, i):
        if parent[i] != i:
            parent[i] = self.find(parent, parent[i])
        return parent[i]

    def union(self, parent, rank, x, y):

        if rank[x] < rank[y]:
            parent[x] = y
        elif rank[x] > rank[y]:
            parent[y] = x

        else:
            parent[y] = x
            rank[x] += 1

    def Kruskal(self):
        result = []
        costs = sorted(self.__costs.items(), key=lambda cost: cost[1])

        new_cost=[]
        for i in costs:
            new_cost.append([i[0][0],i[0][1],i[1]]);
        for i in new_cost:
            j=[i[1],i[0],i[2]]
            if j in new_cost:
                new_cost.remove(j)
        for i in new_cost:
            print(i)
        e=0
        i=0
        parent=[]
        rank=[]
        for node in range(self.__vertices):
            parent.append(node)
            rank.append(0)
        while e<self.__vertices-1:
            u,v,w=new_cost[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)
            # Else discard the edge

        minimum_cost = 0
        print("Edges in the constructed MST")
        g=Graph(self.__vertices,"empty.txt")
        for u, v, weight in result:
            minimum_cost += weight
            g.add_edge(u,v,weight)
            g.add_edge(v,u,weight)
            print("%d -- %d == %d" % (u, v, weight))
        print(g.return_edges())
        print("Minimum Spanning Tree", minimum_cost)




class GraphException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

# graph=Graph(4,"graph.txt")
# print(graph.return_vertices())
# graph.save_graph("saved.txt")
