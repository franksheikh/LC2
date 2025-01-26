from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counts = defaultdict(int, {
            0:1
        })
        ps = 0
        c = 0
        for n in nums:
            ps += n
            c += counts[ps-k]
            counts[ps] += 1
        return c