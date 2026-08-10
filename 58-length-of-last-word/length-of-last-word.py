class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res=s.strip().split()
        print(res)
        length=len(res)
        print(length)
        word=res[-1]
        print(word)
        count=0
        for i in word:
            count=count+1
        return count
s=Solution()
s.lengthOfLastWord("  hello safa  ")