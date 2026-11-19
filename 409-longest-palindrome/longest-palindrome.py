class Solution:
    def longestPalindrome(self, s: str) -> int:

        freq = {}

        for i in s:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1

        ans = 0

        for j in freq:
            if freq[j] % 2 == 0:
                ans += freq[j]
            else:
                ans += freq[j] - 1

        if ans < len(s):
            ans += 1

        return ans