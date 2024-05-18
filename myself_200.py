# 섬의 개수 구하기 문제 BFS 

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
from collections import deque

def numsofisland(grid):

    # 맵의 사이즈 정의 , 방문 표시 설정 
    m,n = len(grid) , len(grid[0])
    visited = [[False]*n for _ in range(m)] # n , m  순서 주의 
    island_num = 0
    def BFS(x,y):
        dy = [0,1,0,-1]
        dx = [1,0,-1,0] # 상하좌우 이동 좌표 

        # 현재 방문한 노드 (x,y)를 추가 
        visited[x][y] = True
        queue = deque()
        queue.append((x,y))

        while queue: 
            cur_x , cur_y = queue.popleft()
            for i in range(4):
                next_x = cur_x + dx[i]
                next_y = cur_y + dy[i]
                # 다음 좌표가 범위내일 경우만 
                if next_x >=0 and next_x<m and next_y>=0 and next_y<n:
                    if grid[next_x][next_y] =='1' and visited[next_x][next_y] is False:
                        queue.append((next_x,next_y))
                        visited[next_x][next_y] = True




    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1' and visited[i][j] is False: # 아직 방문하지 않았고 섬이면 방문 (DFS or BFS)
                BFS(i,j)
                island_num += 1 #BFS / DFS 탐색이 중단되면 섬 하나가 끝난 것 그래서 1 추가 
    return island_num

print(numsofisland(grid))