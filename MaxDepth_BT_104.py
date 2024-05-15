# 이진트리 최대 깊이 구하기 
# level order 탐색 활용 

# BFS 가능하지 않을까??


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


cnt = 0

# post order 방식 DFS 탐색 
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        max_depth = 0
        if root is None:
            return max_depth

        left_cnt = Solution.maxDepth(self,root.left)
        right_cnt = Solution.maxDepth(self,root.right)
        max_depth = max(left_cnt,right_cnt)+1 

        return max_depth


# BFS 가능하지 않을까??
        
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """        
        max_depth = 0

        if root is None:
            return 0
        q = deque()
        q.append((root,1))

        while q:

            cur_node ,cur_depth= q.popleft()
            max_depth = max(max_depth, cur_depth) 

            if cur_node.left:
                q.append((cur_node.left, cur_depth+1))
            if cur_node.right:
                q.append((cur_node.right, cur_depth+1))
        return max_depth
