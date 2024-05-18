# 동적계획법 
# 문제에 대한 정답이 될 가능성이 있는 모든 해결책을 "체계적" , "효율적" 으로 탐색하는 방법 

# 큰 문제들을 작은 문제들로 나누고 해결

# 대표적인 사용 예시 : 피보나치수열 


def fibo(n):
    if n ==0:
        return 0
    if n==1 or n ==2:
        return 1
    
    return fibo(n-1) +fibo(n-2)  # 시간복잡도 O(2**n) 매우높음 

def fibo_dp(n):
    dp =[0]* (n+1)
    dp[0] = 0 
    dp[1] = 1
    for  i in range(2,n+1):
        dp[i] = dp[i-1] +dp[i-2]
    return dp[n]
#print(fibo_dp(150))

## 백준 1043 1로 만들기 문제 
n = int(input())
'''
정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.

X가 3으로 나누어 떨어지면, 3으로 나눈다.
X가 2로 나누어 떨어지면, 2로 나눈다.
1을 뺀다.
정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.

'''
dp = [0 for _ in range(n+1)]
for i in range(2,n+1):
    dp[i]= dp[i-1]+ 1 # 1을 뺀다 

    if i %3 ==0:
        dp[i] = min(dp[i] ,dp[i//3]+1 )
    if i %2 ==0:
        dp[i] = min(dp[i] ,dp[i//2]+1 )
print(dp[n]) 


# 백준 9095번 1,2,3더하기 
T = int(input())
for _ in range(T):

    N = int(input())
    dp=[ 0 for _ in range(11)]
    dp[1]= 1
    dp[2]= 2
    dp[3] =4
    for i in range(4,N+1):
        dp[i]= dp[i-1]+dp[i-2]+dp[i-3]
    print(dp[N])

# 백준 2579 번 계단 오르기  


'''
계단 오르는 데는 다음과 같은 규칙이 있다.

계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있다. 즉, 한 계단을 밟으면서 이어서 다음 계단이나, 다음 다음 계단으로 오를 수 있다.
연속된 세 개의 계단을 모두 밟아서는 안 된다. 단, 시작점은 계단에 포함되지 않는다.
마지막 도착 계단은 반드시 밟아야 한다.
따라서 첫 번째 계단을 밟고 이어 두 번째 계단이나, 세 번째 계단으로 오를 수 있다. 하지만, 첫 번째 계단을 밟고 이어 네 번째 계단으로 올라가거나, 첫 번째, 두 번째, 세 번째 계단을 연속해서 모두 밟을 수는 없다.

각 계단에 쓰여 있는 점수가 주어질 때 이 게임에서 얻을 수 있는 총 점수의 최댓값을 구하는 프로그램을 작성하시오.
'''
T = int(input())
stairs =[0 for i in range(301)]
dp = [0 for i in range(301)]
for i in range(T):
    stairs[i]= int(input())
dp[0] = stairs[0]
dp[1] = stairs[0] + stairs[1]
dp[2] = max(stairs[1] + stairs[2], stairs[0] + stairs[2])
for i in range(3, T):
    dp[i] = max(dp[i - 3] + stairs[i - 1] + stairs[i], dp[i - 2] + stairs[i])
print(dp[T - 1])
