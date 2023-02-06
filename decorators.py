import functools

def start_end_decorator(func):

  @functools.wraps(func)
  def wrapper(*args, **kwargs):
    print("Start")
    res = func(*args, **kwargs)
    print("End")
    return res
  return wrapper

@start_end_decorator
def print_name(x):
  print(x)
  return 5

# print_name = start_end_decorator(print_name)

# res = print_name("Tolis")
# print(res)

# print('-----------')
# print(help(print_name))
# print(print_name.__name__)

def repeat(num_times):
  def decorator_repeat(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
      for _ in range(num_times):
        result = func(*args, **kwargs)
      return result
    return wrapper
  return decorator_repeat


@repeat(num_times=3)
def greet(name):
  print(f'Hello {name}')

greet('Alex')


class CountCalls:
  def __init__(self, func):
    self.func = func
    self.num_calls = 0

  def __call__(self, *args, **kwds):
    print('Hi from call')
    self.num_calls += 1
    print(f'This is executed {self.num_calls} times')
    return self.func(*args, **kwds)

@CountCalls
@repeat(num_times=3)
@start_end_decorator
def say_hello(name):
  greeting = f'Hello {name}'
  print(greeting)
  return greeting

say_hello('John')
say_hello('John')
