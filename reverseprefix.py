class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        if k > len(s):
            return s[::-1]

        return s[:k][::-1] + s[k:]