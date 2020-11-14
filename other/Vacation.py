"""
Taro's summer vacation starts tomorrow, and he has decided to make plans for it now.

The vacation consists of N
days. For each i (1≤i≤N), Taro will choose one of the following activities and do it on the i-th day:

A: Swim in the sea. Gain Ai points of happiness.
B: Catch bugs in the mountains. Gain Bi points of happiness.
C: Do homework at home. Gain Ci points of happiness.

As Taro gets bored easily, he cannot do the same activities for two or more consecutive days.

Find the maximum possible total points of happiness that Taro gains.

All values in input are integers.
1≤N≤105
1≤ai,bi,ci≤104

Input is given from Standard Input in the following format:

N
a1 b1 c1
a2 b2 c2
:
aN bN cN

Print the maximum possible total points of happiness that Taro gains.
"""

def getMaxHappyPoints(matriz, n):
    aux = matriz.copy()
    for i in range(1,n):
        aux[i][0] = matriz[i][0] + max(aux[i-1][1], aux[i-1][2])
        aux[i][1] = matriz[i][1] + max(aux[i-1][0], aux[i-1][2])
        aux[i][2] = matriz[i][2] + max(aux[i-1][0], aux[i-1][1])
    
    a,b,c = aux[n-1]

    return max(a,b,c)
        
def run():
    n = int(input())
    matriz = []
    for _ in range(n):
        line = list(map(int, input().split()))
        matriz.append(line)
    print(getMaxHappyPoints(matriz, n))

run()