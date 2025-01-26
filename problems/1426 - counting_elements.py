class Solution:
    def countElements(self, arr: List[int]) -> int:
        num_set = set(arr)
        c = 0
        for n in arr:
            if n + 1 in num_set: c+= 1
        return c

        