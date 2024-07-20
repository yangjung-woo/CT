'''
0~ n-1 번방까지 총  n개의 방이 있다 
0을 제외한 모든 방은 잠겨있다 
모든 방을 visit  하는게 목표 

rooms[i] , 열쇠 뭉치가 있음 , 열쇠뭉치에 해당하는 방을 방문가능한데

모든 방을 방문 가능하면   True 아니면 False 반환 


example 1 
Input: rooms = [[1],[2],[3],[]]
Output: true

Input: rooms = [[1,3],[3,0,1],[2],[0]]
Output: false


'''
from collections import deque

rooms = [[1],[2],[3],[]]


class Solution(object):
    def canVisitAllRooms(rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        n=len(rooms)

        visited = [False for _ in range(n)]

        # dfs로 풀어볼까?
        def dfs(v):
            visited[v] = True
            for k in rooms[v]:
                if visited[k] ==False:
                    dfs(k)
        dfs(0)

        # bfs로 풀어볼까?
        ###
        
        visited[0] = True
        queue = deque()
        queue.append(rooms[0])

        while queue:
            key_list = queue.popleft()

            for k in key_list:
                if visited[k] ==False:
                    queue.append(rooms[k])
                    visited[k] = True
        ###
        
        
        ### return all(visited) : 리스트 내 모든 요소가 참이면 참 아니면 거짓

        return all(visited)
        '''
        
        for i in range(n):
            if visited[i] == False:
                return False
        return True 
        '''
    
print(Solution.canVisitAllRooms(rooms))
        