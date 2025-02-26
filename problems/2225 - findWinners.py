from collections import defaultdict
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losers = defaultdict(int)
        for match in matches:
            winner, loser = match
            losers[loser] += 1
            if winner not in losers:
                losers[winner] = 0
        
        winners = sorted([key for key,val in losers.items() if val == 0])
        losers = sorted([key for key,val in losers.items() if val == 1])

        return [
            winners, 
            losers
        ]


from collections import defaultdict
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = set()
        losers = defaultdict(int)

        for match in matches:
            new_winner, new_loser = match
            losers[new_loser] += 1
            if new_loser in winners:
                winners.remove(new_loser)
            if new_winner not in losers:
                winners.add(new_winner)
        
        l1 = list(winners)
        l2 = [key for key,val in losers.items() if val == 1]
        
        return [
            sorted(l1),
            sorted(l2)
        ]