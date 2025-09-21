import asyncio
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

def check_stock(item):
    print(f"Checking stock for {item}...")
    time.sleep(3)  # Simulate a time-consuming task  Blocking operation
    return f"Stock for {item}: 100 units"

async def main():
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, check_stock, "laptop")
        print(result)

asyncio.run(main())

