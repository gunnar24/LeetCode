class Solution(object):
    def maximumWealth(self, accounts):
        sumMoney = []
        maxMoney = []
        for i in accounts:
            
            sumMoney.append(sum(i))
            
            
            maxMoney = max(sumMoney)
            
        return maxMoney