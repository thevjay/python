import threading
import time

def monitor_tea_temp():
    while True:
        print(f"Tea temperature is being monitored in thread: {threading.current_thread().name}")
        time.sleep(2)

threading.Thread(target=monitor_tea_temp, daemon=True).start()

print("Main Making tea...")