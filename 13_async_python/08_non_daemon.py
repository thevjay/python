import threading
import time

def monitor_tea_temp():
    while True:
        print(f"Tea temperature is being monitored in thread: {threading.current_thread().name}")
        time.sleep(2)

threading.Thread(target=monitor_tea_temp).start()

print("Main Making tea...")

# Profile 
# python -m cProfile -s time .\08_non_daemon.py