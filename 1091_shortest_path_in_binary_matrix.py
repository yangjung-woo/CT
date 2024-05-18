# n x n 매트릭스가 주어졌을때 출발지에서 목적지까지 도착하는 가장 빠른 경로를 반환하시오  => 최단경로: BFS 가 가장 유리 
# dfs 추천? 
'''
 출발지 (0,0)  , 도착지 (n-1,n-1) 
 8 방향으로 이동 가능 
 0이면 이동 가능 , 1 이면 이동 불가 

'''

from collections import deque
grid = [[0,1],[1,0]]
# DFS 접근 방식은 최단거리 계산에 올바르지 않음 !! 
def shortestPathBinaryMatrix(self, grid):
    now_len = 1
    n = len(grid) # size 
    visited = [[False]*n for _ in range(n)]

    def dfs(curr_x, curr_y ,l):
        dy= [0,1,0,-1, 1,-1,1,-1]
        dx= [1,0,-1,0, 1,1,-1,-1]
        visited[curr_x][curr_y] = True

        if curr_x == n-1 and curr_y == n-1:
            return l
        

        for i in range(8):
            next_x = curr_x + dx[i]
            next_y = curr_y + dy[i]

            if next_x >=0 and next_x < n and next_y >=0 and next_y < n:
                if visited[next_x][next_y] == False and grid[next_x][next_y] == 0:
                    l +=1 
                    dfs(next_x,next_y, l)

    shortest_length= dfs(0,0,now_len)
    return shortest_length

# bfs 사용 방식
def shortestPathBinaryMatrix(self, grid):


    if grid[0][0] == 1: 
        return -1

    n = len(grid)

    if grid[n-1][n-1] == 1: 
        return -1
    visited = [[False]*n for _ in range(n)]
    queue = deque()
    queue.append((0,0,1))
    visited[0][0] = True


    dy= [0,1,0,-1, 1,-1,1,-1]
    dx= [1,0,-1,0, 1,1,-1,-1]


    while queue:
        curr_x , curr_y ,curr_l= queue.popleft()
        # 목적지 도착시 curr_len 을 shortest len에 저장 
        if curr_x == n-1 and curr_y == n-1:
            return curr_l

        for i in range(8):
            next_x , next_y = curr_x +dx[i] , curr_y +dy[i]
            if next_x >=0 and next_x < n and next_y >=0 and next_y < n:
                if visited[next_x][next_y] == False and grid[next_x][next_y] == 0:
                    queue.append((next_x,next_y,curr_l+1))
                    visited[next_x][next_y] = True

    return -1

def MYSelf(grid):
    n = len(grid)
    visited = [[False]*n for _ in range(n)]

    dy= [0,1,0,-1, 1,-1,1,-1]
    dx= [1,0,-1,0, 1,1,-1,-1]

    if grid[0][0]==1 or grid[n-1][n-1]== 1:
        return -1
    
    def bfs(start_x, start_y,start_l):
        queue = deque()
        queue.append((start_x, start_y,start_l))

        while queue:
            curr_x , curr_y ,curr_l = queue.popleft()

            if curr_x ==n-1 and curr_y ==n-1:
                return curr_l
            for i in range(8):
                next_x = curr_x + dx[i]
                next_y = curr_y + dy[i]

                if next_x >=0 and next_x < n and next_y >= 0 and next_y < n:
                    if visited[next_x][next_y] == False and grid[next_x][next_y] == 0:
                        queue.append((next_x,next_y,curr_l+1))
                        visited[next_x][next_y] = True
        return -1


    visited[0][0] = True
    return bfs(0,0,1)
    

print(MYSelf(grid))



        