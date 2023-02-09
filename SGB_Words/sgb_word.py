from time import time
import heapq
from collections import deque

class SGB_Words:
    def __init__(self,filename):
        self.filename = filename

        # Store words in a list() named Vertex
        self.Vertex = []
        with open(filename,'r') as f:
            for e in range(5757):
                self.Vertex.append(f.readline().split()[0])
        
        # print(self.Vertex)

        # Store connection between 2 words in a dict() which each node has the set of node adjacent to it     
        self.Edge = []
        self.AdjacentList = {node : set() for node in self.Vertex}
        for word_1 in self.Vertex:
            for word_2 in self.Vertex:
                checker = 0
                if word_1 == word_2:
                    continue
                
                w1 = [c for c in word_1]
                w2 = [c for c in word_2]

                for c in w1:
                    if c in w2:
                        checker += 1
                        w2.remove(c)

                if checker == 4:
                    if (word_1,word_2) not in self.Edge and (word_2,word_1) not in self.Edge:
                        self.Edge.append((word_1,word_2))
                    self.AdjacentList[word_1].update({word_2})
                    self.AdjacentList[word_2].update({word_1})

        self.visited = set()
        self.queue = []

    # Applying BFS/DFS to calculate the number of Connected Components of a Graph
    def BFS(self, node):
        path = [node]
        self.queue.append(node)
        self.visited.update({node})
        # print(self.visited)

        while len(self.queue) != 0:

            s = self.queue.pop(0)
            self.visited.update({s})

            for t in self.AdjacentList[s]:
                if t not in self.visited:
                    path.append(t)
                    self.visited.update({t})
                    self.queue.append(t)
        if len(path) > 1:

            print('Path : ',path)

    def ConnectedComponents(self)->int:
        cc = 0

        for node in self.Vertex:
            if node not in self.visited:
                self.visited.update({node})
                cc += 1
                self.BFS(node)
        return cc

 
def main():
    global t1,t2,t3,t4,t5,cc,vertex,edge,path,res
    global word_1, word_2

    word_1 = 'which'
    word_2 = 'halma'

    t1 = time()
    sgb_word = SGB_Words('sgb_data.txt')
    t2 = time()
    # cc = sgb_word.ConnectedComponents()
    # t3 = time()
    # path = sgb_word.ShortestPath(word_1, word_2)
    # if path is None:
    #     res = 'No path found!'
    # else:
    #     res = '->'.join(path)
    t4 = time()
    vertex = len(sgb_word.Vertex)
    edge = len(sgb_word.Edge)
    t5 = time()

    print('')


if __name__ == '__main__':
    main()
    
    print('STATISTICS')
    print()
    print(' - Project                :   {}'.format('Five Letter Words'))
    print(' - Input file             :   {}'.format('sgb_data.txt'))
    print(' - Total Nodes            :   {}'.format(vertex))
    print(' - Total Edges            :   {}'.format(edge))
    # print(' - Connected Components   :   {}'.format(int(cc)))
    # print(' - Path \'{}\'->\'{}\'  :   {}'.format(word_1,word_2,res))
    print(' - Import file            :   {:.5f}'.format(t2-t1))
    # print(' - Find C.Components      :   {:.5f}'.format(t3-t2))
    # print(' - Find Path of 2 words   :   {:.5f}'.format(t4-t3))
    print(' - Execution time         :   {:.5f}'.format(t5-t1))
    print()