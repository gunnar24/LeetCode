class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        total = 0
        for i in jewels: 
            for j in stones: 
                if i == j: 
                    total += 1
        return total  