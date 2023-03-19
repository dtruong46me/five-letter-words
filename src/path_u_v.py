import os

class DirectedGraph:
    def __init__(self, filename):
        
        self.filename = os.path.join(os.path.dirname(__file__),'..','data',filename)

        self.nodes = []
        with open(self.filename,'r') as f:
            for _ in range(5757):
                self.nodes.append(f.readline().split()[0])

        
        self.adj = {node : set() for node in self.nodes}
        for word1 in self.nodes:
            for word2 in self.nodes:
                if 