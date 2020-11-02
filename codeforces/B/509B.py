def verifyPebbles(k,piles):
    for i in range(0, len(piles) - 1):
        for j in range(i + 1, len(piles)):
            diff = abs(piles[i] - piles[j])
            if diff >= (k + 1):
                return False
    return True

def getColor(color,k):
    if color > k:
        return 1
    return color

def paintPebbles(k,piles):
    res = ''
    if not verifyPebbles(k, piles):
        res = 'NO'
        return res
    res = 'YES\n'
    for pile in piles:
        pileStr = ''
        color = 1
        for i in range(0, pile):
            color = getColor(color, k)
            pileStr += str(color) + ' '
            color += 1
        pileStr.strip()
        res += pileStr + '\n'
    return res
        
def run():
    n, k = list(map(int, input().split()))
    piles = list(map(int, input().split()))

    print(paintPebbles(k, piles))

run()