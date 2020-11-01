def getBigAnd(k, array):
  res = 0
  for i in range(30,-1,-1):
    andBit = 1 << i
    count = 0
    j = 0
    aux = []
    while j < len(array):
      if array[j] & andBit:
        count += 1
        aux.append(array[j])
      j += 1
    
    if count >= k:
      res += andBit
      array = aux
  
  return res 

def run():
  t = int(input())
  while t > 0:
    _, k = map(int, input().split())
    array = list(map(int, input().split()))
    print(getBigAnd(k, array))    
    t -= 1

run()