class Solution:
    def divisorGame(self, N: int) -> bool:
        if N < 1 or N > 1000:
            return False

        dp = [False, False, True]
        for N_pick in range(3, N + 1):
            dp.append(False)
            for firstPick in range(1, N_pick):
                if N_pick % firstPick == 0 and not dp[N_pick - firstPick]:
                    dp[N_pick] = True
                    break
        return dp[N]

if __name__ == "__main__":
    solution = Solution()
    answer = solution.divisorGame(3)
    print(answer)