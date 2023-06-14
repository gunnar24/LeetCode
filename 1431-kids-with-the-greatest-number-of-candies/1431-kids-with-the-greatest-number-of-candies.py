class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        
        ## n kids 
        ## candies is array
        ## extraCandies is Integer with extra candies I have
        candyMax = max(candies)
        #print(candyMax)
        result = []
        for i in range(len(candies)):
            if (candies[i] + extraCandies) >= candyMax:
                result.append(True)
            else: 
                result.append(False)
        
        return result