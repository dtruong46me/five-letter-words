from time import time

class SGB_Words:
    def __init__(self,filename):
        self.filename = filename

        # Store words in a list() named Vertex
        self.Vertex = []
        with open(filename,'r') as f:
            for e in range(5757):
                self.Vertex.append(f.readline().split()[0])

        # Store connection between 2 words in a list() named Edge
        self.Edge = []
        for word_1 in self.Vertex:
            for word_2 in self.Vertex:
                checker = 0
                if word_1 == word_2:
                    continue
                for c in word_1:
                    if c in word_2:
                        checker += 1
                if checker == 5:
                    if (word_1,word_2) not in self.Edge and (word_2,word_1) not in self.Edge:
                        self.Edge.append((word_1,word_2))

    # Applying BFS/DFS to calculate the number of Connected Components of a Graph
    def ConnectedComponents(self)->int:
        return

    # Applying Dijkstra to find the shortest way between 2 words
    def PathTwoWord(self, word_1:str, word_2:str) -> list:
        return

def main():
    global t1,t2,t3,t4,cc
    t1 = time()
    sgb_word = SGB_Words('sgb_data.txt')
    t2 = time()
    cc = SGB_Words().ConnectedComponents()
    t3 = time()
    path = SGB_Words().PathTwoWord(word_1 = 'after', word_2 = 'stead')
    t4 = time()

    print('')


if __name__ == '__main__':
    main()
    
    print('STATISTICS')
    print()
    print('Project                :   SGB - Words')
    print('Input file             :   sgb_data.txt')
    print('Connected Components   :   {}'.format(int(cc)))
    print('Import file            :   {:.5f}'.format(t2-t1))
    print('Find C.Components      :   {:.5f}'.format(t3-t2))
    print('Find Path of 2 words   :   {:.5f}'.format(t4-t3))