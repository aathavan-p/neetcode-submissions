class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxProf = 0

        while r<len(prices):
            if prices[l]<prices[r]:
                prof = prices[r]-prices[l]
                maxProf = max(prof, maxProf)
            
            else:
                l = r
            r+=1

        return maxProf