class Solution:
    def getDescentPeriods(self, prices):
        window = 1
        result = 1
        for i in range(1, len(prices)):
            if prices[i - 1] - prices[i] == 1:
                window += 1
            else:
                window = 1
            result += window
        return result
