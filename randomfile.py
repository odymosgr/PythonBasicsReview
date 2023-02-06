import random

a = random.random() # 0-1
print(a)
a = random.uniform(1,10)
print(a)
a = random.randrange(1,10)
print(a)
a = random.normalvariate(0, 1)
print(a)

mylist = list("ASDL")
a = random.choice(mylist)
print(a)
a = random.sample(mylist, 3) # unique elements
print(a)
a = random.choices(mylist, k=3) # with replacement
print(a)

random.seed(3)
print(random.random())
print(random.randrange(1,10))







import secrets

a = secrets.randbelow(10)
print(a)
a = secrets.randbits(4)
print(a)
a = secrets.choice(list('ABCDE'))
print(a)





import numpy as np

np.random.seed(3)

a = np.random.rand(3, 3)
print(a)
a = np.random.randint(0, 10, (3, 18))
print(a)
np.random.shuffle(a)
print(a)











