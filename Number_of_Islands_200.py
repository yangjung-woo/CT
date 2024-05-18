# 지도에 표시된 섬의 갯수를 구하시오 

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

from collections import deque

class Solution(object):
    def numIslands(grid):
        number_of_island=0
        m,n = len(grid) , len(grid[0])
        visited = [[False]*n for _ in range(m)]


        def bfs(x,y):
            dy = [0,1,0,-1]
            dx = [1,0,-1,0]
            visited[x][y] = True
            queue = deque()
            queue.append((x,y))

            while queue:
                curr_x ,curr_y = queue.popleft()
                for i in range(4):
                    next_x = curr_x + dx[i]
                    next_y = curr_y + dy[i]
                    if next_x>=0 and next_y>= 0 and next_x <m and next_y <n :  #방문하면 안되는 좌표 빼고 바문 
                        if grid[next_x][next_y] =='1' and visited[next_x][next_y] is False:
                            queue.append((next_x,next_y))
                            visited[next_x][next_y] = True

        for i in range(m):
            for j in range(n):
                if grid[i][j] =='1' and visited[i][j] is False:
                    bfs(i,j)
                    number_of_island +=1 

        return number_of_island

        
print(Solution.numIslands(grid))