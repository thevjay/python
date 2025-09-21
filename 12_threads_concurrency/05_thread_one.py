import threading
import time

def boil_milk():
    print(f"{threading.current_thread().name}: Start boiling milk")
    time.sleep(2)
    print(f"{threading.current_thread().name}: Milk boiled")

def toast_bun():
    print(f"{threading.current_thread().name}: Start toasting bun")
    time.sleep(3)
    print(f"{threading.current_thread().name}: Bun toasted")

# boil_milk()
# toast_bun()

start = time.time()

t1 = threading.Thread(target=boil_milk, name="Thread-Milk")
t2 = threading.Thread(target=toast_bun, name="Thread-Bun")

t1.start()
t2.start()

t1.join()
t2.join()

end = time.time()
print(f"Total time taken in seconds: {end - start:.2f}")

# Threads in Python → good for I/O-bound tasks (web requests, database calls, reading files).
# Multiprocessing in Python → good for CPU-bound tasks (math loops, data crunching, image processing).