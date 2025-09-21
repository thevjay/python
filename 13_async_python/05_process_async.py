import asyncio
from concurrent.futures import ProcessPoolExecutor
import time

def encrypt(data):
    return f"encrypted_{data[::-1]}"

async def main():
    loop = asyncio.get_running_loop()
    with ProcessPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, encrypt, "sensitive_data")
        print(result)

if __name__ == "__main__":
    asyncio.run(main())