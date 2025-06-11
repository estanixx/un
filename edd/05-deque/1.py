from collections import deque
"""
1. Register the first time the seller purchased. (N)
1. If it's not the first time, check if the amount is the same, then buy.
2. Get the minimum between the requested amount and the total amount.
"""
n, t = map(int, input().split())
queue = deque()
for _ in range(n):
  r, k = map(int, input().split())
  queue.append((r, k))
# Approach: Process all requests. Break if no more resellers.
cont = 0
last_data = None
while t > 0:
  cont += 1
  # Get the resellers data. Break if empty.
  try:
    last_data = queue.popleft()
  except IndexError:
    break
  reseller, quantity = last_data
  # Quantity adjudgment.
  quantity = min(quantity, t)
  last_data = (reseller, quantity)
  t -= quantity
  # Ban-check.
  if cont % 5 != 0:
    queue.append(last_data)
else:
  print(*last_data, sep=' ')
  exit()
print('quedaron boletas disponibles')

  
  
  