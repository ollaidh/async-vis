import aiohttp
import random
import asyncio


ENDPOINTS = ["history", "info", "sectors"]


def generate_url(root_url: str) -> str:
    endpoint = random.choice(ENDPOINTS)
    return f"{root_url}/{endpoint}"


async def main():
    for i in range(10):
        url = generate_url("http://127.0.0.1:8888/stocks")
        print(i, url)
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                print(response.status)


if __name__ == "__main__":
    asyncio.run(main())
