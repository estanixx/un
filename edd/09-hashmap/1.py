sets = {
    'F': set(),
    'V': set(),
}
while (cmd:=input()) != '#':
    name, number = cmd.split()
    sets[name].add(int(number))
print(len(sets['F']), len(sets['V']), len(sets['V'] | sets['F']))