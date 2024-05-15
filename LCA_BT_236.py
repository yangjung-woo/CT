# LeetCode 256 최저 공통 조상 찾기 

'''
제약조건 
2 < node 수 < 10**5   => 시간복잡도: O(n)이하여야 함 
모든 Node.value는 유일하다 
p != q 


구현 전 접근
1. 탐색할 노드 q , p 에서 상위 노드로 신호를 보냄 
2. 신호가 left , right 에서 모두 전달되면 공통조상임을 알수 있음 
3. left or rignt 둘중 하나 전달되면 상위노드에게 패스 
4. 아무런 신호가 없으면 동작 x 

def LCA():
 l = LCA
 r = LCA 
 return 
 postorder 순회 
'''

# Definition for a binary tree node.
# 

class TreeNode(object):
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return None
        left = Solution.lowestCommonAncestor(root.left,p,q)
        right = Solution.lowestCommonAncestor(root.right,p,q)

        if root==p or root ==q:# p ,q 이면 그값 그대로 반환 root까지 도달시 끝 
            return root
        elif left and right: # 하위노드로 붜 left right 모두 존재 = 최저 조상
            return root
        return left or right 
        # left도 없고 right 도 없으면 none 반환 
        # left만 있으먄 left만 반환 / right만 있으면 rignt만 반환 
    