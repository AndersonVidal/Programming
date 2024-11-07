def quintomania(n, a):
    i = 0
    v = 1
    perfect = set([5,7])
    while v < n:
        diff = abs(a[i] - a[v])
        if diff not in perfect:
            return 'NO'
        i += 1
        v += 1
    return 'YES'

t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().strip().split(' ')))
    print(quintomania(n, a))

