from itertools import product
a = [1,2]
b = [3,4,'apple']
prod = product(a,b)
print(list(prod))
a = [1]
b = [3,4]
prod = product(a,b, repeat=2)
print(list(prod))


from itertools import permutations
a = [1,2,3]
perm = permutations(a)
print(list(perm))
perm = permutations(a,2)
print(list(perm))



from itertools import combinations, combinations_with_replacement
a = [1,2,3,4]
comb = combinations(a,2)
print(list(comb))

comb_wr = combinations_with_replacement(a,2)
print(list(comb_wr))




from itertools import accumulate
import operator
a = [1,2,3,4]
acc = accumulate(a)
print(list(acc))
acc = accumulate(a, func=operator.mul)
print(list(acc))



from itertools import groupby
group_obj = groupby(a, key=lambda x: x<3)
for k, v in group_obj:
  print(k, list(v))





from itertools import count, cycle, repeat
for i in count(10,29):
  print(i)
  if i>=100: break

a=[1,2,3]
s=1
for i in cycle(a):
  s = s+1
  print(i)
  if s > 10: break

for i in repeat(1111, 5):
  print(i)