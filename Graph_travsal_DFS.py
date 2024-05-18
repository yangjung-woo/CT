# 그래프 DFS 탐색 

graph = {
    'A': ['B','D','E'],
    'B':['A','C','D'],
    'C':['B'],
    'D':['A','B'],
    'E':['A']
}
visited=[]

def DFS_graph(curr):
    visited.append(curr)

    for v in graph[curr]:
        if v not in visited:
            DFS_graph(v)

DFS_graph('A')
print(visited)


    

