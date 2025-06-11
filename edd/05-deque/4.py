import re
for _ in range(int(input())):
  exp = re.sub(r'[\s;]', '', input())
  last_exp = exp
  while exp != '':
    exp = re.sub(r"\[\]|\(\)|\{\}", '', exp)
    if exp == last_exp:
      print('incorrecta')
      break
    last_exp = exp
  else:
    print('correcta')