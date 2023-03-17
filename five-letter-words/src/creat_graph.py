import os
import time

class Graph:
    def __init__(self, filename):
        
        self.filename = os.path.join(os.path.dirname(__file__),'..','data',filename)
        
        self.nodes = []
        with open(self.filename, 'r') as f:
            for _ in range(5757):
                self.nodes.append(f.readline().split()[0])
        # print(self.nodes, len(self.nodes))

        self.adj = {node : set() for node in self.nodes}
        for word1 in self.nodes:
            for word2 in self.nodes:
                if word1 != word2 and sum(c1!=c2 for c1,c2 in zip(word1,word2)) == 1:
                    self.adj[word1].add(word2)
                    self.adj[word2].add(word1)
        
        # print(self.adj['words'])

if __name__ == '__main__':
    
    start_time = time.time()
    graph = Graph(filename = 'sgb_data.txt')
    end_time = time.time()

    print('Execution time : {}'.format(end_time - start_time))
