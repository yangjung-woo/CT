# 재귀함수 개념 >> DFS 구현시 반드시 필요 개념 
# 이진트리 , DP , 완전탐색, 백트래킹에 모두 사용 

def factorial(n):
    if n == 1:
        return 1
    
    return n*factorial(n-1)
# 하지만 시간복잡도 O(n**2)

def fibo(n):
    if n ==1 or n ==2 :
        return 1
    return fibo(n-1) + fibo(n-2)
# 하지만 시간복잡도 O(2**n
# ) 즉 피보나치 수열은 재귀함수 만으로 매우 높은 시간복잡도 


def dp_fibo(n):
    dp = [0] * (n+1)
    dp[0], dp[1] = 0, 1
    for i in range(2, n+1):
        dp[i] = dp[i-2] + dp[i-1]
    return dp[n]

# DP 시간복잡도 O(n) 

class Node:
    def __init__(self, value = 0, left=None , right =None):
        self.value = value
        self.left = None
        self.right = None 
class BinaryTree:
    def __init__(self):
        self.root = None

bt = BinaryTree()
bt.root = Node(value=1)
bt.root.left = Node(value=2)
bt.root.right=Node(value=3)
bt.root.left.left = Node(value=4)
bt.root.left.right = Node(value=5)
bt.root.right.right = Node(value=6)

# 이진탐색 O(nlogn) 시간복잡도 

# 완전 이진트리: 마지막 level을 제외한 모든 차수가 2임 


print(factorial(5))

print (fibo(10))
print(dp_fibo(10))