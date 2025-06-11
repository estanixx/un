import heapq
turns = []
last = None
while (msg := input()) != 'end':
  match(msg):
    case 'sig':
      if len(turns) > 0:
        last = heapq.heappop(turns)
    case msg if msg.isdigit():
      heapq.heappush(turns, int(msg))
print(last)