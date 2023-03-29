import os

class DirectedGraph:
    def __init__(self, filename):
        
        self.filename = os.path.join(os.path.dirname(__file__),'..','data',filename)

        self.nodes = []
        with open(self.filename,'r') as f:
            for _ in range(1000):
                self.nodes.append(f.readline().split()[0])
        
        self.adj = {node : set() for node in self.nodes}
        
        for u in self.nodes:
            u_suffix = u[-4:]
            for v in self.nodes:
                if u_suffix in v and u != v:
                    u_suffix_chars = set(u_suffix)
                    v_chars = set(v)
                    if len(u_suffix_chars.intersection(v_chars)) == len(u_suffix_chars):
                        self.adj[u].add(v)

if __name__ == '__main__':
    directed_graph = DirectedGraph('sgb_data.txt')
    print(directed_graph.adj ,len(directed_graph.adj))