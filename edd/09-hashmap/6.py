from functools import reduce
party_militants = {
    i: set() for i in 'cdi'
}
while (cmd:=input()) != '#':
    code, party = cmd.split()
    party_militants[party[-1]].add(code)
group_intersections = (
    party_militants['c'] & party_militants['d'],
    party_militants['d'] & party_militants['i'],
    party_militants['i'] & party_militants['c']
)
militants = []
# Militants of one party: Full intersection
militants.append(
    set(reduce(lambda acc, a: acc & a, group_intersections))
)
# Militants of two parties: Substract the full intersection from the union of the intersections
militants.append(
    set(reduce(lambda acc, a: acc | a, group_intersections)) - militants[0]
)
# Militants of three parties: Substract two and one militants from all militants.
militants.append(
    set(reduce(lambda acc, a: acc | a, party_militants.values())) - militants[1] - militants[0]
)
print(*map(len, militants[::-1]))
