import aiohttp
import random
import asyncio


ENDPOINTS = ["history", "info", "sectors"]


def generate_url(root_url: str) -> str:
    endpoint = random.choice(ENDPOINTS)
    return f"{root_url}/{endpoint}"


async def send_requests(count: int) -> None:
    async with aiohttp.ClientSession() as session:
        for i in range(count):
            url = generate_url("http://127.0.0.1:8888/stocks")
            async with session.get(url) as response:
                current_task = asyncio.current_task()
                assert current_task
                assert response.status == 200


async def run() -> None:
    tasks = [
        asyncio.create_task(send_requests(10), name=f"request-{i}") for i in range(4)
    ]
    await asyncio.gather(*tasks)


def main():
    asyncio.run(run())


if __name__ == "__main__":
    main()
