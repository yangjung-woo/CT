
# 프로그래머스 DFS level3 문제 

from collections import deque


def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]


    # dfs 솔루션 
    def dfs(curr):
        visited[curr] = True
        for i in range(n):
            if visited[i] == False and computers[curr][i] == 1:
                dfs(i)
    # BFS 솔루션
    def bfs(start):
        queue = deque()
        queue.append(start)

        while queue:
            curr = queue.popleft()

            for i in range(n):
                if visited[i] == False and computers[curr][i] ==1:
                    queue.append(i)
                    visited[i] = True

    for i in range(n):
        if visited[i] == False:
            #dfs(i)
            bfs(i)
            answer +=1

    return answer

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))