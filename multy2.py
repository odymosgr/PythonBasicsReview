from multiprocessing import Process, Value, Array, Lock, Queue, Pool
import os
import time

def add_100(numbers, lock):
  for i in range(100):
    time.sleep(0.01)
    with lock:
      for i in range(len(numbers)):
        numbers[i] += 1

def square(numbers, queue):
  for i in numbers:
    queue.put(i*i)

def make_negative(numbers, queue):
  for i in numbers:
    queue.put(-1*i)

def cube(number):
  return number*number*number

if __name__ == '__main__':

  lock = Lock()
  # shared_number = Value('i', 0)
  shared_array = Array('d', [0.0, 100.0, 200.0])
  print('Array at beginning is : ', shared_array[:])

  p1=Process(target=add_100, args=(shared_array, lock))
  p2=Process(target=add_100, args=(shared_array, lock))

  p1.start()
  p2.start()

  p1.join()
  p2.join()

  print('Array at the end is : ', shared_array[:])

  numbers = range(1,6)
  q = Queue()

  p1=Process(target=square, args=(numbers, q))
  p2=Process(target=make_negative, args=(numbers, q))

  p1.start()
  p2.start()

  p1.join()
  p2.join()

  while not q.empty():
    print(q.get())

  # ---------- Pool -----------

  pool = Pool()
  numbers = range(10)

  # important methods:
  # map, apply, join, close

  result = pool.map(cube, numbers)
  # pool.apply(cube, numbers[0])

  # also there are async calls to map, apply

  pool.close()
  pool.join()

  print(result)