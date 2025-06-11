for _ in range(int(input())):
  n, k = map(int, input().split())
  line = tuple(map(int, input().split()))
  goblin_turns = line[k-1]
  front_ppl_turns = sum(min(el, goblin_turns) for el in line[:k-1])
  back_ppl_turns = sum(min(goblin_turns - 1, el) for el in line[k:])
  turns = front_ppl_turns + goblin_turns + back_ppl_turns
  print(turns * 5)
  
  
  