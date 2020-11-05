from sys import setrecursionlimit
setrecursionlimit(100000)

def merge(arr, l, r):
    i,j = (0,0)
    count = 0
    
    while i < len(l) or j < len(r):
        if i == len(l):
            arr[i + j] = r[j]
            j += 1
        elif j == len(r):
            arr[i + j] = l[i]
            i += 1
        elif l[i] <= r[j]:
            arr[i+j] = l[i]
            i += 1
        else:
            arr[i+j] = r[j]
            count += len(l) - i
            j += 1

    return count

def countInversions(arr):
    if len(arr) < 2:
        return 0
    
    mid = len(arr) // 2
    
    left = arr[:mid]
    right = arr[mid:]

    countL = countInversions(left)
    countR = countInversions(right)

    mergeInvs = merge(arr, left, right)

    return countL + countR + mergeInvs

def run():
    while True:
        n = int(input())
        if n == 0: break
        array = list(map(int, input().split()))
        print(countInversions(array))

run()