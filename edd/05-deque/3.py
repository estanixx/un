from collections import deque
people = deque()
while (msg:= input()) != 'termina':
  cmd = msg.split()
  match cmd[0]:
    case 'agrega':
      people.append(int(cmd[1]))
    case 'engulle':
      if people[0] > people[-1]:
        people.pop()
      else:
        people.popleft()
if len(people) >= 1:
  print(f'cabeza {people[0]} cola {people[-1]}')
else:
  print('uroboro vacio')