class Solution:
    def rob(self, nums) -> int:
        if not nums:
            return 0

        if len(nums) < 2:
            return nums[0]

        dp = [nums[0], max(nums[0], nums[1])]
        if nums[0] < nums[1]:
            last_steal = [0, 1]
        else:
            last_steal = [0, 0]

        for i in range(2, len(nums)):
            if i - last_steal[-1] > 1:
                if dp[i - 1] > dp[i - 1] + nums[i]:
                    dp.append(dp[i - 1])
                else:
                    last_steal.append(i)
                    dp.append(dp[i - 1] + nums[i])
            else:
                if dp[i - 2] + nums[i] > dp[i - 1]:
                    dp.append(dp[i - 2] + nums[i])
                    last_steal.append(i)
                else:
                    if dp[i - 1] > nums[i]:
                        dp.append(dp[i - 1])
                    else:
                        last_steal.append(i)
                        dp.append(nums[i])
        return max(dp)

if __name__ == "__main__":
    solution = Solution()
    answer = solution.rob([2, 1, 1, 2])
    print(answer)