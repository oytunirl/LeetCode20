class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        temp = s
        for x in range(len(s)):
            temp = temp[1:]
            temp += s[x]
            print(temp)
            if temp == goal:
                return True
        return False
        