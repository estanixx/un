players = []
while (num := int(input())) != 0:
  try:
    players.remove(num)
    continue
  except ValueError:
    pass
  
  try:
    players.remove(num + 1)
    continue
  except ValueError:
    pass
  
  try:
    players.remove(num - 1)
    continue
  except ValueError:
    pass
  
  players.append(num)
print(*(players if len(players) != 0 else (0,)), sep=' ')