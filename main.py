from fastapi import FastAPI
import uvicorn
import asyncio
import time
import responses


app = FastAPI()


async def fetch_history():
    await asyncio.sleep(0.1)


async def fetch_info():
    await asyncio.sleep(0.05)


async def fetch_sectors():
    await asyncio.sleep(0.2)


def process_history():
    time.sleep(0.01)


def process_info():
    time.sleep(0.001)


def process_sectors():
    time.sleep(0.02)


@app.get("/stocks/history")
async def get_history():
    await fetch_history()
    process_history()
    return {"response": responses.MOCK_HISTORY_RESPONSE}


@app.get("/stocks/info")
async def get_info():
    await fetch_info()
    process_info
    return {"response": responses.MOCK_INFO_RESPONSE}


@app.get("/stocks/sectors")
async def get_sectors():
    await fetch_sectors()
    process_sectors()
    return {"response": responses.MOCK_SECTORS_RESPONSE}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8888)
