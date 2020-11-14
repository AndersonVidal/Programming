def counter(n, values):
    memory = set()
    tam = [0] * 100100
    for i in range(n):
        value = values[i]
        tam[value] += 1
        memory.add(value)
    
    res = len(memory)
    cont = [0] * 100100
    for i in range(n):
        value = values[i]
        tam[value] -= 1
        cont[i] = res
        if tam[value] == 0:
            res -= 1
    
    return cont

def printAnswer(count, m):
    for i in range(m):
        li = int(input())
        print(count[li - 1])

def run():
    n, m = list(map(int, input().split()))
    values = list(map(int, input().split()))
    count = counter(n, values)
    printAnswer(count, m)

run()