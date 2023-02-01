# Tuples: ordered, immutable, allows duplicate elements

mytuple = ("Max", 25, "Male")
# Tuple for iterable
mytuple2 = tuple(["Jane", 23, "Female"])

print(mytuple)
print(mytuple2)

for i in mytuple:
  print(i)

print(len(mytuple))

tuple_slice = mytuple[:2]
print(tuple_slice)

name, age, sex = mytuple
print(name)

name2, *rest = mytuple2
print(rest)

# Tuples require less space in memory and are created faster than Lists
