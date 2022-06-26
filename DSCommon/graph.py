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
        self._V = int(line0_split[0])
        self._E = int(line0_split[1])
        self._adj = list()
        for i in range(self._V):
            self._adj.append(list())

        for i in range(1, len(lines)):
            e = lines[i].split()
            if len(e) >= 2:
                v = int(e[0])
                for l in range(1, len(e)):
                    w = int(e[l])
                    self.add_edge(v, w)


    def add_edge(self, v, w):
        self._adj[v].append(w)
        self._adj[w].append(v)


    def adj(self, v):
        return self._adj[v]


    def V(self):
        return self._V
    

    def E(self):
        return self._E


    def __str__(self):
        return str(self._adj)


    def __repr__(self):
        return str(self._adj)


    def reverse(self):
        pass



class DiGraph(Graph):
    def __init__(self, V=0, E=0, file_name=None):
        self._V = V
        self._E = E
        if file_name != None:
            self.init_from_file(file_name)
        else:
            self._adj = list()
            for i in range(self._V):
                self._adj.append(list())


    def add_edge(self, v, w):
        self._adj[v].append(w)


    def reverse(self):
        dig = DiGraph(self.V(), self.E())
        for i in range(self.V()):
            for v in self.adj(i):
                dig.add_edge(v, i+1)
        return dig



class Edge():
    def __init__(self, v, w, weight):
        self.v = v
        self.w = w
        self.weight = weight


    def __str__(self):
        l = [str(self.v), "->", str(self.w), ", w ", str(self.weight)]
        return "".join(l)


    def __repr__(self):
        l = [str(self.v), "->", str(self.w), " w ", str(self.weight)]
        return "".join(l)



class WeightedDiGraph(Graph):
    def init_from_file(self, file_name):
        try:
            f = open(file_name, "r")
        except e as error:
            print(error)
            return 0

        lines = f.readlines()
        line0_split = lines[0].split()
        self._V = int(line0_split[0])
        self._E = int(line0_split[1])
        self._adj = list()
        for i in range(self._V):
            self._adj.append(list())

        for i in range(1, len(lines)):
            e = lines[i].split()
            v = int(e[0])
            w = int(e[1])
            weight = int(e[2])
            edge = Edge(v, w, weight)
            self.add_edge(edge)


    def add_edge(self, e):
        self._adj[e.v].append(e)


    def __str__(self):
        return str(self._adj)




if __name__ == '__main__':
    #  graph = Graph("g.txt")
    #  print(graph)
    #  directed_graph = DiGraph(file_name="dg.txt")
    #  print(directed_graph)
    #  reversed_digraph = directed_graph.reverse()
    #  print(reversed_digraph)
    #  directed_graph2 = DiGraph(file_name="dg2.txt")
    #  print(directed_graph2)
    #  weighted_directed_graph = WeightedDiGraph("wdg.txt")
    #  print(weighted_directed_graph)
    g = DiGraph(file_name="dfs-demo.txt")
    print(g)
