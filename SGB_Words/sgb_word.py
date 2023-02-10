from time import time
import heapq
from collections import deque

class SGB_Words:
    def __init__(self,filename):
        self.filename = filename
        self.Vertex = []

        # Store words in a list() named Vertex
        with open(filename,'r') as f:
            for e in range(200):
                self.Vertex.append(f.readline().split()[0])

        # Adjacent List of Arcs in Undirected Graph
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
                    self.AdjacentList[word_1].update({word_2})

        # Adjacent List of Arcs in Directed Graph
        self.DirectedList = {node : set() for node in self.Vertex}

        for word_1 in self.Vertex:
            for word_2 in self.Vertex:
                if word_1 == word_2:
                    continue

                w1 = [c for c in word_1]
                w2 = [c for c in word_2]
                count = 0

                for i in range(1,len(w1)):
                    if w1[i] in w2:
                        count += 1
                        w2.remove(w1[i])
                
                if count == 4:
                    self.DirectedList[word_1].update({word_2})

        # Check total Arcs in Undirected Graph
        self.Arcs = 0
        for key in self.AdjacentList.keys():
            self.Arcs += len(self.AdjacentList[key])

        # Check total Arcs in Directed Graph
        self.Directed = 0
        for key in self.DirectedList.keys():
            self.Directed += len(self.DirectedList[key])
        
        for key in self.DirectedList.keys():
            print(key,self.DirectedList[key],len(self.DirectedList[key]))

        self.visited = set()
        self.queue = []


    
    def BFS(self,start_node):
        self.queue.append(start_node)



 
def main():
    global t1,t2,t3,t4,t5,cc,vertex,edge
    global word_1, word_2,edge_dir

    word_1 = 'which'
    word_2 = 'halma'

    t1 = time()
    sgb_word = SGB_Words('sgb_data.txt')
    t2 = time()

    t4 = time()
    vertex = len(sgb_word.Vertex)
    edge = int(sgb_word.Arcs / 2)
    edge_dir = int(sgb_word.Directed)
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
    print(' - Total Directed Edge    :   {}'.format(edge_dir))

    print(' - Import file            :   {:.5f}'.format(t2-t1))

    print(' - Execution time         :   {:.5f}'.format(t5-t1))
    print()