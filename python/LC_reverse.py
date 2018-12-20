#Leet Code - reverse string

class Solution():
    def reverseString(self, s):
        final = ""
        length = len(s)
        for i in range(length-1, -1, -1):
            final += s[i]
        print final



test = Solution()
tmp = "hello"
test.reverseString(tmp)