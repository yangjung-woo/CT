# 구름 level3 하늘다리 놓기

n = int(input())
mount_list = list(map(int,input().split()))
stack = []
answer = 0
for m in mount_list:

    if len(stack) ==0 or stack[-1] > m: # 작으면 stack에 추가 
        stack.append(m)
    else: # 크거나 같다면 조건 
        #1. 같음
        if m == stack[-1]:
            answer +=1
        if m > stack[-1]:

            while(len(stack)>0):
                if stack[-1] ==m:
                    answer+=1
                    stack.append(m)
                    break
                elif stack[-1]< m:
                    stack.pop()
                elif stack[-1]>m:
                    stack.append(m)
                    break 

print(answer)


