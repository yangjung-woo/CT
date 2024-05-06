class Solution(object):
    # 1. 괄호 쌍은 반드시 짝수 , 그리고 짝이 맞아야 한다 +- =0 
    # 2. 여는 괄호가 먼저 와야 한다 
    def isValid(self, s):  
        stack =[] #Use a stack of characters.
        for c in s:
            if c == '(':
                stack.append(')')
            elif c == '{':
                stack.append('}')
            elif c == '[':
                stack.append(']')
            elif not stack or stack.pop() != c:
                return False
        return not stack
            