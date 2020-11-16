def expo(x, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        m = n // 2
        return expo(x,m) * expo(x,m)
    
    m = (n-1) // 2
    return expo(x,m) * expo(x,m) * x


x = int(input())
n = int(input())

print(expo(x,n))