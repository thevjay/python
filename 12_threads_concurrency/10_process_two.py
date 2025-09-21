from multiprocessing import Process

import time

def cpu_heavy():
    print("Starting CPU heavy task")
    total = 0
    for i in range(10**8):
        total += i
    print("CPU heavy task completed")

if __name__ == "__main__": 
    start=time.time()
    processs = [Process(target=cpu_heavy) for _ in range(2)]
    [t.start() for t in processs]
    [t.join() for t in processs]
    end=time.time()
    print("Total time taken:", end - start)