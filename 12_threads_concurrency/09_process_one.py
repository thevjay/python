import threading
import time

def cpu_heavy():
    print("Starting CPU heavy task")
    total = 0
    for i in range(10**7):
        total += i
    print("CPU heavy task completed")

start=time.time()
threads = [threading.Thread(target=cpu_heavy) for _ in range(2)]
[t.start() for t in threads]
[t.join() for t in threads]
end=time.time()

print("Total time taken:", end - start)