from collections import deque
for _ in range(int(input())):
  pieces = deque(map(int, input().split()))
  while True:
    # if the summation of the two last pices, remove them and add the average.
    if len(pieces) == 1:
      break
    piece1, piece2 = pieces.pop(), pieces.pop()
    if (piece1 + piece2) % 2 == 0:
      last_piece = (piece1 + piece2) // 2
      pieces.append(last_piece)
    else:
      pieces.append(piece2)
      pieces.append(piece1)
      break
  print(len(pieces), pieces[-1])
    
    
      
      