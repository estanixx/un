nums = []
while (opt:=input()) != 'E':
  action, number = opt.split()
  number = int(number)
  match action:
    case 'A':
      nums.append(number)
    case 'M':
      res = sum([i for i in nums if i % number == 0])
      print(res)