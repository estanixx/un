for _ in range(int(input())):
  participants, count_crit = list(map(int, input().split()))
  participants = list(range(1, participants + 1))
  while len(participants) != 1:
    idx = (count_crit - 1) % len(participants)
    just_quit = participants.pop(idx)
    participants = participants[idx:] + participants[:idx]
    count_crit = max(1, just_quit % len(participants))
  print(participants[0])
    