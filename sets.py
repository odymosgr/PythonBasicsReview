# Sets: unordered, mutable, no duplicates

myset = {1,2, 5}
myset = {1,2,3,2,3}
myset = set("hello")
myset = set([1,2,3,"hello"])

print(myset.pop())
print(myset)

odds = set(range(1,13,2))
evens = set(range(2,14,2))
primes = {2,3,5,7,11}

u = odds.union(evens)
print(u)

i = odds.intersection(primes)
print(i)

dif = odds.difference(primes)
print(dif)

symdif = odds.symmetric_difference(primes)
print(symdif)

copyset = u.copy()
copyset = set(u)