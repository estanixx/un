size = int(input())
vals = sorted(list(map(int, input().split())))
kilometers = {code: idx for idx, code in enumerate(vals)}
for _ in range(int(input())):
  p1, p2 = map(int, input().split())
  kilo_count = abs(kilometers[p1] - kilometers[p2])
  print(f'{kilo_count} kms')
