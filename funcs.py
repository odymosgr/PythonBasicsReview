def foo(a, b, *args, **kwargs):
  print(a,b)
  for arg in args:
    print(arg)

  for key in kwargs:
    print(key, kwargs[key])

foo(1,2,3,4,5,six=6,seven=7)


# enforce keyword args
def foo2(*args, last):
  print(last)

foo2(1,2,3, last=100)


# unpack
def foo3(a,b,c):
  print(a,b,c)

l = [1,2,3]
t = (1,2,3)
d = {'a':1, 'b':2, 'c':3}
foo3(*l)
foo3(*t)
foo3(**d)


#local global vars
def foo4():
  global num
  x = num
  print('num inside: ', x)
  num +=1

num = 0
foo4()
print('num outside: ', num)





def foo5(x):
  x = 5

var = 10
foo5(var)
print(var)


def foo6(alist):
  alist.append(5)
  alist[0] = -1

var = [1,2,3,4]
foo6(var)
print(var)





