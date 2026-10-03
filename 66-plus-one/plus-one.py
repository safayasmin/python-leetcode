class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        r=''.join(map(str,digits))
        res=int(r)+1
        r2=list(map(int,str(res)))
        return r2
        












        