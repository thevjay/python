import threading
import time

def prepare_chai(type_,wait_time):
    print(f"{threading.current_thread().name}: Start preparing {type_} chai")
    time.sleep(wait_time)
    print(f"{threading.current_thread().name}: {type_} chai is ready")

t1 = threading.Thread(target=prepare_chai, args=("Masala",2), name="Thread-Masala")
t2 = threading.Thread(target=prepare_chai, args=("Ginger",3), name="Thread-Ginger")

start = time.time()

t1.start()
t2.start()  

t1.join()
t2.join()

end = time.time()
print(f"Total time taken in seconds: {end - start:.2f}")
