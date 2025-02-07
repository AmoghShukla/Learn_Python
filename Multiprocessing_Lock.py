import time
import multiprocessing

def deposit_funds(Balance,Lock):
    for i in range(100):
        time.sleep(0.01)
        Lock.acquire()
        Balance.value = Balance.value + 1
        Lock.release()

def withdraw_funds(Balance,Lock):
    for i in range(100):
        time.sleep(0.01)
        Lock.acquire()
        Balance.value = Balance.value - 1
        Lock.release()

if __name__ == '__main__':
    Balance = multiprocessing.Value('i',200)
    Lock = multiprocessing.Lock()
    d = multiprocessing.Process(target=deposit_funds,args=(Balance,Lock))
    w = multiprocessing.Process(target=withdraw_funds, args=(Balance,Lock))

    d.start()
    w.start()

    d.join()
    w.join()

    print(Balance.value)

