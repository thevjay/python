import asyncio
import aiohttp

async def fetch_url(session, url):
    async with session.get(url) as response:
        print(f"Fetched {url} with status {response.status}")

async def main():
    urls = [
        "https://httpbin.org/delay/2"
    ] * 3
    
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        # tasks =[t1,t2,t3]
        await asyncio.gather(*tasks)

asyncio.run(main())
# Output:
# Fetched https://httpbin.org/delay/2 with status 200


# Real-world example

# Imagine you go to a tea shop 🍵:

# Normal way (without with):

# You order a cup, drink it, and you must remember to return the cup.

# With with:

# You order chai using a “chai service,” drink it, and the waiter automatically takes the cup back for you.

# You don’t need to worry about cleanup.