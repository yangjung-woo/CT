# BFS 그래프 순회 기본 코드 

# graph 예시 

from collections import deque


graph = {
    'A': ['B','D','E'],
    'B':['A','C','D'],
    'C':['B'],
    'D':['A','B'],
    'E':['A']
}

def BFS_graph(graph,start_v):
    visited = [start_v]
    queue = deque(start_v)  # visited  와 queue에 시작점 추가 
    while(queue):
        curr_v = queue.popleft()  # queue에서 현재노드 빼고 
        for v in graph[curr_v]: # queue에서 현재노드 빼고  인접한 노드 전부 큐에 저장
            if v not in visited: # 단 방문하지 않은 노드만 
                visited.append(v)
                queue.append(v)
    return visited

print(BFS_graph(graph,'A'))


def BFS_myself(graph,startnode):
    visited = [startnode]
    queue = deque(startnode)

    while queue:
        curr = queue.popleft()
        for v in graph[curr]:
            if v not in visited:
                queue.append(v)
                visited.append(v)
    return visited
