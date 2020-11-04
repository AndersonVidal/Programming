def getKnotDivisible(n,k):
    r = (k - 1) // (n - 1)
    return r + k

def run():
    tests = int(input())
    for _ in range(tests):
        n, k = list(map(int, input().split()))
        print(getKnotDivisible(n,k))

run()