class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        minv = float('inf')
        running_sum = 0
        for num in nums:
            running_sum += num
            minv = min(minv, running_sum)
        
        if minv < 0:
            return abs(minv) + 1
        else:
            return 1