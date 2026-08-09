class Solution(object):
    def isPalindrome(self, s):
        val=""
        for char in s:
            if char.isalnum():
                val += char.lower()
        return val==val[::-1]
    