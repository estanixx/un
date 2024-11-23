queue = []
while (opt:=input()) != "0 0":
  _, max_q = opt.split()
  max_q = int(max_q)
  if max_q < len(queue):
    continue
  
  queue.append(max_q)
  while any(max_t < len(queue) for max_t in queue):
    to_remove = next(i for i, max_t in enumerate(queue) if max_t < len(queue))
    queue.pop(to_remove)

print(len(queue))