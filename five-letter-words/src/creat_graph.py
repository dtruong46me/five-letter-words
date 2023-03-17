
class Graph:
    def __init__(self, filename):
        self.filename = filename

        self.vertex = []
        with open(self.filename, 'r') as f:
            words = set(f.read().split())

        self.nodes = {}
        for word in words:
            self.nodes[word] = set()

graph = Graph('data/sgb_data.txt')
print(graph.nodes)