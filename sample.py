import time
import threading


def square(numbers):
    print("Square of Numbers")
    for i in numbers:
        time.sleep(1)
        print('square of ',i,'=',(i*i))


def cube(numbers):
    print("\nCube of Numbers")
    for i in numbers:
        time.sleep(1)
        print('cube of ',i,'=',(i*i*i))


arr = [2,3,4,7]
t = time.time()
# square(arr)
# cube(arr)
t1 = threading.Thread(target=square, args=(arr,))
t2 = threading.Thread(target=cube, args=(arr,))

t1.start()
t2.start()

t1.join()
t2.join()

print('\ntime taken',(time.time()-t))

