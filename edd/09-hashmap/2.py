registries = {
    'Dead': set(),
    'Alive': set(),
}
while (cmd:=input()) != 'E':
    cmd, code = cmd.split()
    match cmd:
        case 'B':
            if not code in registries['Dead'] and not code in registries['Alive']:
                registries['Alive'].add(code)
        case 'D':
            if code in registries['Alive']:
                registries['Alive'].remove(code)
                registries['Dead'].add(code)
        case 'R':
            if code in registries['Dead']:
                registries['Dead'].remove(code)
                registries['Alive'].add(code)
print(len(registries['Alive']))