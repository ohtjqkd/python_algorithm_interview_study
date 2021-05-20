# leete no. 121

class Solution:
    def maxProfit(self, prices):
        return third(prices)


def first(prices):
    length = len(prices)
    max_dp = [0 for _ in range(length)]
    min_dp = [float('inf') for _ in range(length)]
    max_dp[-1] = prices[-1]
    min_dp[0] = prices[0]
    for i in range(1, length):
        if min_dp[i-1] > prices[i]:
            min_dp[i] = prices[i]
        else:
            min_dp[i] = min_dp[i-1]
        if max_dp[-i] < prices[-(i+1)]:
            max_dp[-(i+1)] = prices[-(i+1)]
        else:
            max_dp[-(i+1)] = max_dp[-i]
    return max([tup[0]-tup[1] for tup in zip(max_dp, min_dp)])

def second(prices): # 단 방향으로 해도 됨
    length = len(prices)
    max_dp = [0 for _ in range(length)]
    max_dp[-1] = prices[-1]
    for i in range(1, length):
        if max_dp[-i] < prices[-(i+1)]:
            max_dp[-(i+1)] = prices[-(i+1)]
        else:
            max_dp[-(i+1)] = max_dp[-i]
    return max([m-prices[i] for i, m in enumerate(max_dp)])

def third(prices): # 가장 빠름
    answer = 0
    min_v = prices[0]
    for i in range(1, len(prices)):
        answer = max(answer, prices[i]-min_v)
        if prices[i] < min_v:
            min_v = prices[i]
    return answer
prices = [7,6,4,3,1]
prices = [7,1,5,3,6,4]
print(Solution().maxProfit(prices))