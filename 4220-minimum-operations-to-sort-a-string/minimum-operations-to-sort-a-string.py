class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)

        if s == "".join(sorted(s)):
            return 0

        if n == 2:
            return -1

        if s[0] == min(s) or s[-1] == max(s):
            return 1

        if min(s) in s[1:-1] or max(s) in s[1:-1]:
            return 2

        return 3