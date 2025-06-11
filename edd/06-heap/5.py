import heapq
duration = int(input())
tones = [ list(map(int, input().split()))[1:] for _ in range(int(input())) ]
song = []
for start, interval in tones:
  current = start
  while current <= duration:
    heapq.heappush(song, current)
    current += interval
while len(song) > 0:
  print(heapq.heappop(song))