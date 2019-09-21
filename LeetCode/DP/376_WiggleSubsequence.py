class Solution:
    def wiggleMaxLength(self, nums) -> int:
        if not nums:
            return 0

        if len(nums) == 1:
            return 1

        if nums[1] - nums[0]>0:
            up_down = 1
        elif nums[1] == nums[0]:
            up_down = 0
        else:
            up_down = -1

        if nums[1] == nums[0]:
            max_len = 1
        else:
            max_len = 2

        for i in range(2, len(nums)):
            # print(up_down, max_len, nums[i], nums[i-1])
            # current = 1 if (nums[i] - nums[i - 1] > 0) 0 elif (nums[i]-nums[i-1]==0) else -1
            if nums[i] - nums[i-1] > 0:
                current = 1
            elif nums[i] - nums[i-1] == 0:
                current = 0
            else:
                current = -1
            if current == up_down or current == 0:
                continue

            up_down *= -1
            max_len+=1

        return max_len

    def wiggleMaxLength_DP(self, nums) -> int:
        if not nums:
            return 0

        dp_up = [0]
        dp_down = [0]
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                dp_down.append(dp_down[i - 1])
                dp_up.append(dp_down[i] + 1)
            elif nums[i] == nums[i - 1]:
                dp_down.append(dp_down[i - 1])
                dp_up.append(dp_up[i - 1])
            else:
                dp_up.append(dp_up[i - 1])
                dp_down.append(dp_up[i] + 1)

        return max(dp_up[-1], dp_down[-1]) + 1

if __name__ == "__main__":
    solution = Solution()
    answer = solution.wiggleMaxLength_DP([102,101,20,91,156,78,75,142,69,81,46,142,113,163,190,178,13,36,134,54])
    print(answer)