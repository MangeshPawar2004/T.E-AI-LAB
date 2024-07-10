class Graph:
    def __init__(self, n):
        self.n = n
        self.g = [[] for j in range(n)]
        self.visited = [False] * n

    def addEdge(self, u, v):
            self.g[u].append(v)
            self.g[v].append(u)



    def dfs(self, v):
        self.visited[v] = True
        print(v, end=" ")
        for i in range(self.n):
            if self.g[v][i] == 1 and self.visited[i] == False:
                self.dfs(i)

    def bfs(self, v):
        q = [v]
        self.visited[v] = True

        while q:
            vertex = q.pop()
            print(vertex, end=" ")

            for neighbour in self.g[vertex]:
                if not self.visited[neighbour]:
                    q.append(neighbour)
                    # print(i,end=" ")
                    self.visited[neighbour] = True


vertex = int(input("enter no of vertex"))
g1 = Graph(vertex+1)

n = int(input("enter no of edges to add"))

# for i in range(n+1):
#     src = int(input(f"enter source node for edge: {i+1} "))
#     des = int(input(f"enter destination node for edge: {i+1} "))
#     g1.addEdge(src, des)
#
# choice_Source = int(input("Choose Src node to implement dfs"))
# g1.dfs(choice_Source)

# g1.addEdge(0, 1)
# g1.addEdge(0, 2)
# g1.addEdge(1, 2)
# g1.addEdge(1, 3)
# g1.addEdge(2, 3)
# g1.addEdge(2, 4)
#
# g1.dfs(1)


for i in range(n):
    src = int(input(f"enter source node for edge: {i + 1}:  "))
    des = int(input(f"enter destination node for edge: {i + 1}:  "))
    g1.addEdge(src, des)

choice_Source = int(input("Choose Src node to implement bfs"))
g1.bfs(choice_Source)

# g1.bfs(0)
