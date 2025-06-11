for _ in range(int(input())):
  weights = sorted(list(map(int, input().split(', '))))
  breakpoint = len(weights)
  min_diff = 10 ** 9
  for bp in range(breakpoint):
    wizq, wder = sum(weights[:bp]), sum(weights[bp:])
    min_diff = min(abs(wizq - wder), min_diff)
  print(min_diff)
      