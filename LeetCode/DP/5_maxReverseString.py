class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        if len(s)==1:
            return s

        if len(s)==2 and s[0] != s[1]:
            return s[0]

        size = len(s)
        dp = [[False for _ in range(size)] for _ in range(size)]
        ans = ""
        max_string_len = 0
        for i in range(1, size):
            for j in range(i):
                if s[i] == s[j] and (i-j <= 2 or dp[j + 1][i - 1]):
                    dp[j][i] = True
                    if i-j > max_string_len:
                        max_string_len = i-j
                        ans = s[j:i + 1]
        return ans

if __name__ == "__main__":
    solution = Solution()
    ans = solution.longestPalindrome("cbbd")
    print(ans)