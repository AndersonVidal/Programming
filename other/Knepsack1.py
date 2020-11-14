"""
There are N items, numbered 1,2,…,N. For each i (1≤i≤N), Item i has a weight of wi and a value of vi.
Taro has decided to choose some of the N items and carry them home in a knapsack. The capacity of the knapsack is W, 
which means that the sum of the weights of items taken must be at most W.

Find the maximum possible sum of the values of items that Taro takes home.

All values in input are integers.
1≤N≤100
1≤W≤10^5
1≤wi≤W
1≤vi≤10^9

Input is given from Standard Input in the following format:
N  W
w1 v1
w2 v2
:
wN vN

Print the maximum possible sum of the values of items that Taro takes home.
"""
"""
# O(n*m) -> O(10^7)

def calculeKnepsack(wt, vt, n, w):
    dp = [[0 for x in range(w + 1)] for x in range(n + 1)] 
    for item in range(1,n+1):
        for capacity in range(1,w+1):
            maxValue = dp[item - 1][capacity]
            maxValueCurr = 0
            wItem = wt[item - 1]
            
            if capacity >= wItem:
                maxValueCurr = vt[item - 1]
                remainingCapacity = capacity - wItem
                maxValueCurr += dp[item - 1][remainingCapacity]
            
            dp[item][capacity] = max(maxValue, maxValueCurr)
    
    return dp[n][w]
"""
def calculeKnepsack(n, w):
    dp = [0] * (w + 1)
    for i in range(n):
        wi, vi = map(int,input().split())
        for j in range(w, wi-1, -1):
            totalValue = dp[j - wi] + vi
            if totalValue > dp[j]:
                dp[j] = totalValue

    return dp[w]

def run():
    n, w = list(map(int, input().split()))
    print(calculeKnepsack(n, w))
run()
