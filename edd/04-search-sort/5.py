def bubble_count(arr):
  n = len(arr)
  count = 0
  for i in range(2, n + 1):
    for j in range(n - i + 1):
      if arr[j] > arr[j + 1]:
        count += 1
        arr[j], arr[j + 1] = arr[j + 1], arr[j]
  return count
for _ in range(int(input())):
  tis = list(map(int, input().split()))
  print(bubble_count(tis))