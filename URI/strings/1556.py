from sys import setrecursionlimit
setrecursionlimit(100000)

def backtranck(word):
  lenght = len(word)
  # base case
  if lenght == 1:
    return set([word])
  
  mid = lenght // 2
  left = backtranck(word[0:mid])
  right = backtranck(word[mid:lenght])

  res = set()
  res.add(word)
  res = res.union(left.union(right))
  for elementL in left:
    for elementR in right:
      res.add(elementL + elementR)
  
  return res

def printAllSequences(sequences):
  sequences = sorted(list(sequences))
  for seq in sequences:
    print(seq)

def run():
  while True:
    try:
      word = input()
      sequences = backtranck(word)
      printAllSequences(sequences)
      print()
    except EOFError:
      break

run()