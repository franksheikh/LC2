class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ps = [nums[0]]
        for i in range(1,len(nums)):
            ps.append(nums[i] + ps[-1])
        return ps
