def _binaryIndexSearch(arr, el, start, end):
  pos = (start + end) // 2
  if start > end:
    return 0
  middle = arr[pos]
  match middle:
    case middle if middle == el:
      return pos + 1
    case middle if middle > el:
      return _binaryIndexSearch(arr, el, start, pos - 1)
    case _:
      return _binaryIndexSearch(arr, el, pos + 1, end)  
  
def binaryIndexSearch(arr, el):
  return _binaryIndexSearch(arr, el, 0, len(arr) - 1)

input()
vals = list(map(int, input().split()))
input()
search_vals = list(map(int, input().split()))

print(sum(binaryIndexSearch(vals, searched) for searched in search_vals))