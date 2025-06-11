def getSortedOccurrencies(arr):
  occurrencies = dict()
  for el in arr:
    current_count = occurrencies.get(el)
    occurrencies[el] = 1 if current_count is None else current_count + 1
  arr = list(occurrencies.keys())
  n = len(arr)
  for i in range(2, n + 1):
    for j in range(n - i + 1):
      if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]
  return [occurrencies[el] for el in arr]
  
  
for _ in range(int(input())):
  vals = list(map(int, input().split()))
  print(*getSortedOccurrencies(vals), sep=' ')
  