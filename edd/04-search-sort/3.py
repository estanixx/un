def binaryIn(arr, el, start = 0, end = None):
  if end is None:
    end = len(arr) - 1
  pos = (start + end) // 2
  if start > end:
    return False
  middle = arr[pos]
  match middle:
    case middle if middle == el:
      return True
    case middle if middle > el:
      return binaryIn(arr, el, start, pos - 1)
    case _:
      return binaryIn(arr, el, pos + 1, end)  
  
  
def getDivisors(num):
  return tuple(n for n in range(1, num // 2 + 1) if num % n == 0) + (num,)
    
for _ in range(int(input())):
  _, sub = map(int, input().split())
  vals = tuple(map(int, input().split()))
  divisors = getDivisors(sub)
  if all(binaryIn(vals, divisor) for divisor in divisors):
    print("Es PrimiConjunto")
  else:
    print('No es PrimiConjunto')