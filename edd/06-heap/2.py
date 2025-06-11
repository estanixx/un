import re
import heapq
teams = {group: { 'members': [], 'points': 0 } for group in 'ABC'}
while (ev := input()) != 'fin del juego':
  exp_matches = re.match(r"(A|B|C) (\d+)", ev)
  if exp_matches:
    group, num = exp_matches.group(1), int(exp_matches.group(2))
    heapq.heappush(teams[group]['members'], num);
  else:
    min_vals = {group: heapq.heappop(teams[group]['members']) for group in 'ABC' if len(teams[group]['members']) > 0 }
    if len(min_vals.keys()) == 0:
      continue
    min_val = min(min_vals.values())
    for group, val in min_vals.items():
      if val == min_val:
        teams[group]['points'] += 1
    
for team, data in teams.items():
  print(f'Equipo {team}: {data["points"]}')