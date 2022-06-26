from stack import Stack
from graph import Graph

class DFS():
    def __init__(self, g):
        self.visited = [False] * g.V()
        self.id = [0] * g.V()
        self.connect = 1
        self.ts = Stack(g.V())

        for v in range(g.V()):
            if self.visited[v] is False:
                self.dfs(g, v)
                self.connect += 1

    #  def postorder(self, v):
        #  self.ts.

    def dfs(self, g, v):
        self.id[v] = self.connect
        self.visited[v] = True
        for w in g.adj(v):
            if self.visited[w] is False:
                self.dfs(g, w)
        # post order
        #  self.ts.push(v)


    #  def topological_sort(self, g):
        #  r = list()
        #  while self.ts.is_empty() == False:
            #  r.append(self.ts.pop())
        #  return r


    def connected(self, v, w):
        return self.id[v] == self.id[w]



if __name__ == '__main__':
    g = Graph("dfs-demo.txt")
    dfs = DFS(g)
    print(dfs.connected(1, 3))
