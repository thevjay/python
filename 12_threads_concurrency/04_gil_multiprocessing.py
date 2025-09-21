from multiprocessing import Process
import time

def crunch_numbers(name):
    print(f"Process {name}: Start of number crunching..")
    count = 0
    for _ in range(100_000_000):
        count += 1
    print(f"Process {name}: End of number crunching")
    
if __name__ == '__main__':
    start = time.time()
    process1 = Process(target=crunch_numbers, args=("Process-1",))
    process2 = Process(target=crunch_numbers, args=("Process-2",))

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    end = time.time()
    print(f"Total time taken in seconds: {end - start:.2f}")


# Threading in Python → good for I/O-bound tasks (web requests, database calls, reading files).

# Multiprocessing in Python → good for CPU-bound tasks (math loops, data crunching, image processing).

# That’s why your brew_chai (CPU heavy) was slow with threads, but faster with multiprocessing.