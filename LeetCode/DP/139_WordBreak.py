class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        dp = []
        s = list(s)
        start = [0]
        for i in range(len(s)):
            inDict = False
            for startj in start:
                inDict = "".join(s[startj: i+1]) in wordDict
                if inDict:
                    start.append(i+1)
                    break
            dp.append(inDict)
        return dp[-1]

if __name__ == "__main__":
    solution = Solution()
    answer = solution.wordBreak("aaaaaaa", ["aaaa", "aaa"])
    print(answer)