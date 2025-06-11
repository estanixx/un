names = set([i for i in range(1, int(input()) + 1)])
while (cmd:=input()) != '#':
    cmd = cmd.split()
    match cmd:
        case cmd if len(cmd) == 3:
            _, diddy, mommy = cmd
            son = int(diddy) + int(mommy)
            while son in names:
                son += 1
            names.add(son)
        case cmd if len(cmd) == 2:
            _, query = cmd
            print('' if int(query) in names else 'no ', 'existe', sep='')