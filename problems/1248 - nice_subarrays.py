from collections import defaultdict
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        counts = defaultdict(int,{0:1})
        ps = c = 0
        for n in nums:
            ps += n % 2
            c += counts[ps - k]
            counts[ps] += 1
        return c