from threading import Thread, Lock
import  time

dbvalue = 0

def increase(lock):
  global dbvalue

  # lock.acquire()
  with lock:
    local_copy = dbvalue
    local_copy += 1
    time.sleep(0.1)
    dbvalue = local_copy

  # lock.release()

if __name__ == "__main__":
  lock = Lock()

  print('start value :', dbvalue)

  thread1 = Thread(target=increase, args=(lock,))
  thread2 = Thread(target=increase, args=(lock,))

  thread1.start()
  thread2.start()

  thread1.join()
  thread2.join()

  print('end value   :', dbvalue)
  print('end main')