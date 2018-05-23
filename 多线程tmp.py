from concurrent.futures import *
import  threading

lock = threading.Lock()
threadPool=ThreadPoolExecutor(max_workers=2)

print("执行前num:%s",num)

num=0

def add(i):
    global num
    for i in range(5):
        lock.acquire()
        try:
            num = num + i
        finally:
            lock.release()

def sub(i):
    global num
    for i in range(5):
        lock.acquire()
        try:
            num = num - i
        finally:
            lock.release()

threadPool.submit(add,1)
threadPool.submit(sub,1)
threadPool.shutdown()

print("执行后num:%s",num)













