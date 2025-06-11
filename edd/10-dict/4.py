words = set()
results = []
while (cmd:=input()) != '#':
    words.add(cmd.strip())
wordlist = sorted(list(words))
for w1 in wordlist:
    for w3 in filter(lambda a: a.startswith(w1) and len(a) > len(w1), wordlist):
        w2 = w3[len(w1):]
        if w2 in words:
            results.append((w3, w1, w2))
results.sort()
for w3, w1, w2 in results:
    print(f'{w3} = {w1} + {w2}')