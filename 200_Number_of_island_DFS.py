# 섬 개수 구하기 문제 leetcode 200 DFS 



grid = [["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]]

def numberofisland(grid):
    total= 0
    m,n = len(grid),len(grid[0])

    visited = [[False]*n for _ in range(m)]


    def dfs(curr_x,curr_y):
        dy = [0,1,0,-1]
        dx = [1,0,-1,0]

        visited[curr_x][curr_y] = True

        for i in range(4):
            next_y = curr_y + dy[i]
            next_x = curr_x + dx[i]

            if next_x>=0 and next_x < m and next_y >=0 and next_y <n:
                if grid[next_x][next_y] =='1' and visited[next_x][next_y] == False:
                    dfs(next_x,next_y)


    for i in range(m):
        for j in range(n):
            if grid[i][j] =='1' and visited[i][j] ==False:
                dfs(i,j)
                total += 1
    return total


print(numberofisland(grid))
