#739. Daily Temperatures
# 매일 온도를 나타내는 배열 temperatures
# 해당 날짜에서 따뜻해지기 위해 기다려야 하는 날짜를 list 형식으로 반환 
# 1 <= temperatures.length <= 10^5 , n2 로는 풀수 없음 
# s

class Solution(object):
    def dailyTemperatures(self, temperatures):
        answer = [0]* len(temperatures)
        stack = []
        for cur_day, cur_temp in enumerate(temperatures):
            while stack and stack[-1][1] < cur_temp:
                prev_day , t = stack.pop()
                answer[prev_day] = cur_day- prev_day
            stack.append((cur_day, cur_temp))
        return answer


# solution 낮은온도면  append , 높은 온도면 pop  
class Solution(object):
    def dailyTemperatures(self, temperatures): 
        answer = [0]*len(temperatures)
        stack = 0
        for current_day, current_temp in enumerate(temperatures):
            while stack and stack[-1][1] < current_temp:
                prev_day,_ = stack.pop()
                answer[prev_day] = current_day - prev_day
            stack.append((current_day,current_temp))
        return answer
            

