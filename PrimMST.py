import matplotlib.pyplot as plt
import networkx as nx

class Graph:
    def  __init__(self, v : int) -> None:
        self.vertices = v
        self.graph = [ [0 for _ in range(v) ] for _ in range(v)]


    def minKey(self, key : list, mstSet : list):

        mini = 10000
        min_index = 0

        for v in range(self.vertices):
            if mstSet[v] == False and key[v] < mini:
                mini = key[v]
                min_index = v
        return min_index

    def drawGraph(self):
        G = nx.Graph()
        G.name = "Graph Visualization"
        G.add_nodes_from([0 for _ in range(self.vertices)])
        
        for i in range(self.vertices):
            for j in range(self.vertices):
                weight = self.graph[i][j]
                if weight != 0:
                    G.add_edge(i, j, weight=weight)
        
        pos = nx.spring_layout(G, seed=7)        
        nx.draw(G, pos, with_labels=True, node_size=1000, font_color="white")
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_color="red")
        plt.margins(0.2)
        plt.show()
    
    def drawMSt(self, parent : list):
        G = nx.Graph()
        G.name = "MST With Prim's"
        G.add_nodes_from([0 for _ in range(self.vertices)])
        for i in range(1, self.vertices):
            G.add_edge(parent[i], i, weight=self.graph[i][parent[i]])
        
        pos = nx.spring_layout(G, seed=7)        
        nx.draw(G, pos, with_labels=True, node_size=1000, font_color="white")
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_color="red")
        plt.margins(0.2)
        plt.show()

    def printMST(self, parent : list):
        print("Edge \tWeight")
        for i in range(1, self.vertices):
            print(parent[i], "-", i, "\t", self.graph[i][parent[i]])

    def primMST(self):

        parent = [0 for _ in range(self.vertices)] # integer

        key = [10000 for _ in range(self.vertices)] # integer - Cost

        mstSet = [False for _ in range(self.vertices)]

        key[0] = 0

        parent[0] = -1

        for i in range(self.vertices):

            u = self.minKey(key, mstSet)

            mstSet[u] = True

            for v in range(self.vertices):
                if self.graph[u][v] != 0 and mstSet[v] == False and self.graph[u][v] < key[v] :
                    parent[v] = u
                    key[v] = self.graph[u][v]
        self.printMST(parent)
        self.drawMSt(parent)



g = Graph(5)

g.graph = [
    [ 0, 2, 0, 6, 0 ],
    [ 2, 0, 3, 8, 5 ],
    [ 0, 3, 0, 0, 7 ],
    [ 6, 8, 0, 0, 9 ],
    [ 0, 5, 7, 9, 0 ]
]

g.drawGraph()

g.primMST()
