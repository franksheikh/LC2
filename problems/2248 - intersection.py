#1
from collections import defaultdict
class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        n = len(nums)
        count_map = defaultdict(int)
        res = []
        res_set = set()
        for arr in nums:
            for val in set(arr):
                count_map[val] += 1
                if count_map[val] == n:
                    res_set.add(val)
            
        return sorted(res_set)
#2
from collections import defaultdict
class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        n = len(nums)
        count_map = defaultdict(int)
        res = []
        for arr in nums:
            for val in arr:
                count_map[val] += 1
                if count_map[val] == n:
                    res.append(val)
            
        res.sort()
        return res