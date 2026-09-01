class Solution(object):
    def isAnagram(self, s, t):
        stack=[]
        for char in s:
            stack.append(char)
        for char in t:
            if char in stack:
                stack.remove(char)
            else:
                return False
                break
        return len(stack)==0
        

       


        