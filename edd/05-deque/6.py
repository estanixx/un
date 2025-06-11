from collections import deque
"""
Approach: Use a deques dict to index each stack.
1. Valid if the first deque isn't empty and the second one doesn't have a greater piece.
2. If not valid, continue (N).
2. If not valid, recieve the input but don't do anything.
3. Use the invalid flag and the C deque to determine case.
"""
for _ in range(int(input())):
  discos = int(input())
  # Deque Dict with A as the initial.
  deques = {
    'A': deque([i for i in range(discos)]),  
    'B': deque(),
    'C': deque(),
  }
  invalid = False
  # Main Loop.
  while (msg := input()) != 'X X':
    p, q = msg.split()
    valid_movement = len(deques[p]) > 0 and (len(deques[q]) == 0 or deques[p][-1] > deques[q][-1])
    if not valid_movement:
      invalid = True
    if invalid:
      continue
    element = deques[p].pop()
    deques[q].append(element)
    
  if invalid:
    print('secuencia invalida')
  elif len(deques['C']) == discos and list(deques['C']) == list(range(discos)):
    print('soluciona la torre')
  else:
    print('no soluciona la torre')