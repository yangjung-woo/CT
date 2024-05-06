# myway
class Solution(object):
    def isValid(self, s):  
        stack =[] #Use a stack of characters.
        for c in s:
            if c =='(':
                stack.append(')')
            elif c =='{':
                stack.append('}')   
            elif c =='[':
                stack.append(']')   
            elif not stack  or stack.pop() != c: # close 
                return False
        if not stack:
            return True
        else:
            return False



            


        