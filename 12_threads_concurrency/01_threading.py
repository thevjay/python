import threading
import time

def take_orders():
    for i in range(1,4):
        print(f"Taking order {i}")
        time.sleep(2)
    
def brew_chai():
    for i in range(1,4):
        print(f"Brewing chai {i}")
        time.sleep(3)

# create threads
order_thread = threading.Thread(target=take_orders)
brew_thread  = threading.Thread(target=brew_chai)

# start threads
order_thread.start()
brew_thread.start()

# wait for both threads to complete
order_thread.join()
brew_thread.join()

print("All tasks completed.")