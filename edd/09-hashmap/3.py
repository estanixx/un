from functools import reduce
students = [set([input() for _ in range(int(input()))]) for _ in range(5)]
print(1_000_000 // n_students if (n_students:=len(reduce(lambda acc, a: acc & a, students))) else 'Nadie gana' )