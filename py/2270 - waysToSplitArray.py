class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        running_sum = 0
        count = 0
        for i in range(len(nums)-1):
            running_sum += nums[i]
            if running_sum >= total_sum - running_sum:
                count += 1
        return count