import heapq
for _ in range(int(input())):
  input()
  nums = list(map(int, input().split()))
  heapq.heapify(nums)
  x = ''
  y = ''
  while len(nums) > 0:
    try:
      x += str(heapq.heappop(nums))
      y += str(heapq.heappop(nums))
    except:
      pass
  x = int(x)
  y = int(y)
  print(x + y)