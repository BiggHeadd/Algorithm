class Solution:
    def maxProduct(self, nums) -> int:
        if not nums:
            return 0

        max_stack, min_stack = [nums[0]], [nums[0]]
        for i in range(1, len(nums)):
            max_stack_mul_nums_i = max_stack[-1]*nums[i]
            min_stack_mul_nums_i = min_stack[-1]*nums[i]
            max_stack.append(max(max_stack_mul_nums_i, min_stack_mul_nums_i, nums[i]))
            min_stack.append(min(max_stack_mul_nums_i, min_stack_mul_nums_i, nums[i]))
        return max(max_stack)

if __name__ == "__main__":
    solution = Solution()
    array = [-2,-3,-1]
    answer = solution.maxProduct(array)
    print(answer)