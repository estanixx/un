m = int(input())
buyers = dict()
winners = set()
nwinners = 0
while (cmd:=input()) != 'end':
    cmd, num = cmd.split()
    num = int(num)
    match(cmd):
        case 'winner':
            winners.add(num)
        case 'sms':
            if buyers.get(num) is None:
                buyers[num] = 1
            else:
                buyers[num] += 1
            
            if num in winners:
                print(num, int(m / (len(winners) * buyers[num])))
                nwinners += 1
if nwinners == 0:
    print('0') 


            