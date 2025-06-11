for _ in range(int(input())):
  total, multiply, module = map(int, input().split())
  tnums = range(1, total + 1)
  while (l:=len(tnums)) > 1:
    tnums = sorted([ (multiply * i) % module for i in tnums])[l//2:]
  print(tnums[-1])
  
  