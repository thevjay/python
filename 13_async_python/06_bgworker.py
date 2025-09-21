import asyncio
import threading
import time

def background_worker():
    while True:
        time.sleep(1)
        print(f"Background worker running in thread: {threading.current_thread().name}")

async def fetch_orders():
    await asyncio.sleep(3)
    print("Order fetched")

threading.Thread(target=background_worker,daemon=True).start()

asyncio.run(fetch_orders())