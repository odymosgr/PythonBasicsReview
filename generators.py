def mygenerator():
  yield 1
  yield 2
  yield 6

# g = mygenerator()
# for i in g:
#   print(i)

g2 = mygenerator()
value = next(g2)
print(value)

print(sum(g2))

g3 = mygenerator()
print(sorted(g3))

def countdown(num):
  print('Starting')
  while num > 0:
    yield num
    num -= 1

cd = countdown(4)
print(next(cd))
print(next(cd))
print(next(cd))
print(next(cd))
# print(next(cd))


print('Fibonacci')

def fibonacci(limit):
  a, b = 0, 1
  while a < limit:
    yield a
    a, b = b, a+b

fib=fibonacci(100)
for i in fib:
  print(i)



mygenerator = (i for i in range(100) if i%2 == 0)
print(next(mygenerator))
print(next(mygenerator))
print(next(mygenerator))