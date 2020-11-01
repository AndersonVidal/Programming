class Stack:
  def __init__(self):
    self.itens = []
  
  def isEmpty(self):
    return self.itens == []
  
  def push(self, item):
    self.itens.append(item)
  
  def pop(self):
    return self.itens.pop()
  
  def peek(self):
    return self.itens[len(self.itens) - 1]
  
  def size(self):
    return len(self.itens)


def move(i,j,table,visits):
  if i == 0:
    # ⬇️
    if table[i+1][j] == 0 and (i+1,j) not in visits: return (i+1,j)
    if j == 0:
      # ➡️
      if table[i][j+1] == 0 and (i,j+1) not in visits: return (i,j+1)
    elif j == 4:
      # ⬅️
      if table[i][j-1] == 0 and (i,j-1) not in visits: return (i,j-1)
    else:
      # ➡️⬅️
      if table[i][j+1] == 0 and (i,j+1) not in visits: return (i,j+1)
      if table[i][j-1] == 0 and (i,j-1) not in visits: return (i,j-1)
  elif i == 4:
    if j == 0:
      # ➡️
      if table[i][j+1] == 0 and (i,j+1) not in visits: return (i,j+1)
    elif j == 4:
      # ⬅️
      if table[i][j-1] == 0 and (i,j-1) not in visits: return (i,j-1)
    else:
      # ➡️⬅️
      if table[i][j+1] == 0 and (i,j+1) not in visits: return (i,j+1)
      if table[i][j-1] == 0 and (i,j-1) not in visits: return (i,j-1)
    # ⬆️ 
    if table[i-1][j] == 0 and (i-1,j) not in visits: return (i-1,j)
  else:
    # ⬇️➡️⬆️⬅️
    if table[i+1][j] == 0 and (i+1,j) not in visits: return (i+1,j)
    if j < 4:
      if table[i][j+1] == 0 and (i,j+1) not in visits: return (i,j+1)
    if table[i-1][j] == 0 and (i-1,j) not in visits: return (i-1,j)
    if j > 0:
      if table[i][j-1] == 0 and (i,j-1) not in visits: return (i,j-1)
  # ❌
  return (i,j)

def have_way(table):
  stack = Stack()
  visits = set()
  i = 0
  j = 0

  if table[i][j] == 1: return False

  stack.push((i,j))
  visits.add((i,j))
  while not stack.isEmpty() and ((i,j) != (4,4)):
    newPos = move(i,j, table, visits)
    visits.add((i,j))
    # 🔙
    if newPos == stack.peek():
      stack.pop()
      if stack.isEmpty(): 
        continue
      i,j = stack.peek()
    # 🔜
    else:
      stack.push((i,j))
      i,j = newPos

  if i == 4 and j == 4:
    return True
  return False 

def input_table():
  table = []

  inputStr = input()
  while inputStr == "":
    inputStr = input()

  table.append(list(map(int, inputStr.strip().split(' '))))
  for _ in range(4):
    line = list(map(int, input().strip().split(' ')))
    table.append(line)
  
  return table

def run():
  n = int(input())

  while n > 0:
    table = input_table()
    if have_way(table): 
      print("COPS")
    else:
      print("ROBBERS")
    n -= 1 

run()