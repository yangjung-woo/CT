# DP: 완전탐색을 체계적이고 효율적으로 탐색
# 크고 복잡한 문제를 작은 문제들로 나눈다 subproblem
# 중복 계산하는 문제를 또 다시 계산하지 않음 
# 하위 문제에 대한 답을 통해 원래 문제에 대한 답을 계산한다 

# ex 피보나치 수열

def fibo(n): # 재귀 방식 매우 많은 계산량이 필요 O(2**n)
    if n ==1 or n ==2:
        return 1
    return fibo(n-1) + fibo(n-2)

# DP 방식 (딕셔너리, 리스트 둘다 사용가능)
dp={}

# top down 방식
def fibo_dp(n):
    if n ==1 or n ==2:
        return 1
    
    if n not in dp:
        dp[n] = fibo_dp(n-1) + fibo_dp(n-2)
    

    return dp[n]

print(fibo(500))