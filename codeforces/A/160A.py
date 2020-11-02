def getTotalAmount(coins):
    res = 0
    for coin in coins:
        res += coin
    return res

def divideCoints(coins):
    coins.sort(reverse=True)
    halfAmount = getTotalAmount(coins) // 2
    count = 0
    i = 0
    while halfAmount > 0 and i < len(coins):
        halfAmount -= coins[i]
        count += 1
        i += 1
    if halfAmount == 0: count += 1

    return count

def run():
    n = int(input())
    coins = list(map(int, input().split()))

    print(divideCoints(coins))

run()