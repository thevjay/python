import threading
import time

def brew_chai(name):
    print(f"{threading.current_thread().name}: Start of Brewing chai for {name}")
    count = 0
    for _ in range(100_000_000):
        count += 1
    print(f"{threading.current_thread().name}: End of Brewing Chai for {name} is ready")
    return count


thread1 = threading.Thread(target=brew_chai, args=("Customer-1",), name="Thread-1")
thread2 =threading.Thread(target=brew_chai, args=("Customer-2",), name="Thread-2")

start = time.time()
thread1.start()
thread2.start()

thread1.join()
thread2.join()

end = time.time()
print(f"Total time taken in seconds: {end - start:.2f}")