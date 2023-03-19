from creat_graph import Graph

class Connected_Components:
    def __init__(self, filename):
        self.graph = Graph(filename)

        self.visited = set()
        self.queue = []
        self.cnt_components = 0

    def BFS(self, start_node):
        path = []
        self.queue.append(start_node)
        self.visited.update({start_node})

        while len(self.queue) != 0:

            s = self.queue.pop(0)
            self.visited.update({s})

            for t in self.graph.adj[s]:
                if t not in self.visited:
                    path.append(t)
                    self.visited.update({t})
                    self.queue.append(t)
        
        # if len(path) > 1:
        #     print(path)

    def Con_Components(self)->int:

        for node in self.graph.nodes:
            if node not in self.visited:
                self.visited.update({node})
                self.cnt_components += 1
                self.BFS(node)
        return self.cnt_components

if __name__ == '__main__':
    cc = Connected_Components(filename='sgb_data.txt')
    cc.BFS('words')
    print(cc.Con_Components())