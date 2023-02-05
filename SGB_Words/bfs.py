V = [1,2,3,4,5,6,7,8,9,10,11,12,13]
E = [(1,2),(1,3),(1,11),(2,4),(2,6),(3,4),(4,6),(5,9),(5,10),(6,7),(6,8),(8,10),(9,13),(11,12),(11,13),(12,13)]
# print(len(E))

queue = []
visited = [0 for i in range(len(V))]

def BFS(start_node):
    path = [start_node]

    queue.append(start_node)
    visited[start_node-1] = 1

    Adj = {node : set() for node in V}
    for e in E:
        Adj[e[0]].update({e[1]})
        Adj[e[1]].update({e[0]})

    while len(queue) != 0:

        s = queue.pop(0)
        visited[s-1] = 1
        
        for t in Adj[s]:
            if visited[t-1] == 0:
                queue.append(t)
                path.append(t)
                visited[t-1] = 1
    
    print(path)

# BFS(1)