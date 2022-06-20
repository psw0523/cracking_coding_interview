class Graph():
    def __init__(self, file_name=None):
        if file_name is not None:
            self.init_from_file(file_name)


    def init_from_file(self, file_name):
        try:
            f = open(file_name, "r")
        except e as error:
            print(error)
            return 0

        lines = f.readlines()
        line0_split = lines[0].split()
        self.V = int(line0_split[0])
        self.E = int(line0_split[1])
        self.adj = list()
        for i in range(self.V):
            self.adj.append(list())

        for i in range(1, len(lines)):
            e = lines[i].split()
            v = int(e[0])
            w = int(e[1])
            self.add_edge(v, w)


    def add_edge(self, v, w):
        self.adj[v-1].append(w)
        self.adj[w-1].append(v)


    def V(self):
        return self.V


    def E(self):
        return self.E


    def adj(self, v):
        return self.adj[v-1]


    def __str__(self):
        return str(self.adj)



class DirectedGraph(Graph):
    def add_edge(self, v, w):
        self.adj[v-1].append(w)


if __name__ == '__main__':
    graph = Graph("g.txt")
    print(graph)
    directed_graph = DirectedGraph("dg.txt")
    print(directed_graph)
    directed_graph2 = DirectedGraph("dg2.txt")
    print(directed_graph2)
