import asyncio
import time

async def brew(name):
    print(f"Brewing {name}...")
    await asyncio.sleep(3) # Non-blocking call
    # time.sleep(3) # Blocking call, simulating a long-running task
    print(f"{name} is ready!")

async def main():
    await asyncio.gather(
        brew("chai"),
        brew("coffee"),
        brew("green tea")
    )

asyncio.run(main())

# Output:
# Brewing chai...   
# Brewing coffee...
# Brewing green tea...
# (after 2 seconds)
# Chai is ready!
# Coffee is ready!
# Green tea is ready!
