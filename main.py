import threading
import random

l1 = threading.Lock()
def list(lst):
    l1.acquire()
    for i in range(10):
        lst.append(random.randint(1, 10))
    print("10 случайных чисел:", lst)
    l1.release()

def summ(lst):
    s = sum(lst)
    print("Сумма:", s)

def avg(lst):
    avg = sum(lst)/len(lst)
    print("Среднее:", avg)

lst = []
t1 = threading.Thread(target=list, args=(lst,))
t2 = threading.Thread(target=summ, args=(lst,))
t3 = threading.Thread(target=avg, args=(lst,))

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()
