
V = [1,2,3,4,5,6,7,8,9,10,11,12,13]
E = [(1,2),(1,3),(1,11),(2,4),(2,6),(3,4),(4,6),(5,9),(5,10),(6,7),(6,8),(8,10),(9,13),(11,12),(11,13),(12,13)]
# print(len(E))
visited = [0 for i in range(len(V))]

def DFS(start_node):
    path = [start_node]
    # print(path)

    stack = []
    stack.append(start_node)
    visited[start_node-1] = 1

    # Node adjacent with start_node:
    Adj = {node : set() for node in V}
    for e in E:
        Adj[e[0]].update({e[1]})
        Adj[e[1]].update({e[0]})
    

    while len(stack) != 0:
        s = stack.pop()
        # print(s)
        for t in Adj[s]:
            # print(t)
            if visited[t-1] == 0:
                visited[t-1] = 1
                path.append(t)
                stack.append(s)
                stack.append(t)
                break

    print(path)

DFS(1)