class Solution:
    def repeatedCharacter(self, s: str) -> str:
        letter_set = set()
        for c in s:
            if c in letter_set: return c
            if c not in letter_set: letter_set.add(c)
