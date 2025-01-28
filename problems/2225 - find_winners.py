'''
 w = {
    1
    2
    10
    
 }

 l = {
    3
    4
    6
    7
    8
    9
 }


'''
from collections import defaultdict
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = set()
        losers = defaultdict(int)

        for match in matches:
            w, l = match

            losers[l] += 1

            if w not in losers:
                winners.add(w)
            if l in winners:
                winners.remove(l)
        
        return [
            sorted(winners),
            sorted([x for x in losers if losers[x] == 1])
        ]
            

        