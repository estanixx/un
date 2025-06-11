import heapq
for _ in range(int(input())):
  nums = list(map(int, input().split()))[:-1]
  heapq.heapify(nums)
  while len(nums) > 2:
    a, b = heapq.heappop(nums), heapq.heappop(nums)
    heapq.heappush(nums, a + b)
  print(*nums, sep=' ')