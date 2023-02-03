# lambda arguments: expression
add10 = lambda x: x+10
print(add10(5))

mult = lambda x,y: x*y
print(mult(2,5))

a = list(range(1,5))
print(list(a))
b = map(lambda x: x*2, a)
print(list(b))

c = [x*4 for x in a]
print(c)

d = filter(lambda x: x%2==0, a)
print(list(d))

from functools import reduce
prod_a = reduce(lambda x,y: x*y, a)
print(prod_a)


