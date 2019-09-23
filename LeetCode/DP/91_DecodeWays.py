class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s == "":
            return 0

        s = list(s)
        dp = [0]*len(s)
        if s[0] == '0':
            return 0
        else:
            dp[0] = 1

        if len(s) == 1:
            return 1

        if int(s[0]+s[1])<=26:
            if s[1] == '0':
                dp[1] = 1
            else:
                dp[1] = 2
        else:
            if s[1] == '0':
                return 0
            dp[1] = 1
        for i in range(2, len(s)):
            num = int(s[i-1]+s[i])
            if 10<=num<=26:
                if s[i] == '0':
                    dp[i] = dp[i-2]
                else:
                    dp[i] = dp[i-1]+dp[i-2]
            elif num == 0:
                return 0
            elif num>26:
                if s[i] == '0':
                    return 0
                else:
                    dp[i] = dp[i-1]
            elif num<10:
                dp[i] = dp[i-2]
            else:
                raise RuntimeError("Error")
            # print(dp)
        return dp[-1]

if __name__ == "__main__":
    solution = Solution()
    answer = solution.numDecodings("1123")
    print(answer)