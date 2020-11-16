
def mult(A, B, n):
    if n <= 3:
        return A*B
    
    m = n // 2
    p = A // 10**m
    q = A % 10**m
    r = B // 10**m
    s = B % 10**m

    pr = mult(p, r, m)
    qs = mult(q, s, m)
    y = mult(p+q, r+s, m+1)

    ab = pr * 10**(2*m) + (y - pr - qs) * 10**m + qs

    return ab

print(mult(int(input()), int(input()), int(input())))
