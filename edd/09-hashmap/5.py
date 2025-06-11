from functools import reduce
books = {
    'F': set(),
    'G': set(),
}
while (cmd:=input()) != '0':
    isbn, name = cmd.split()
    books[name].add(isbn)
both = set(reduce(lambda acc, a : acc & a, books.values()))
for_fernando = set(filter(lambda a: int(a[-1]) % 2 == 0, both))
for_gustavo = both - for_fernando
books['F'] = (books['F'] - both) | for_fernando
books['G'] = (books['G'] - both) | for_gustavo

print(len(books['F']), len(books['G']))
    