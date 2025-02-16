import requests
import random


ENDPOINTS = ["history", "info", "sectors"]


def generate_url(root_url: str) -> str:
    endpoint = random.choice(ENDPOINTS)
    return f"{root_url}/{endpoint}"


if __name__ == "__main__":
    for i in range(10):
        url = generate_url("http://127.0.0.1:8888/stocks")
        print(i, url)
        response = requests.get(url)
        print(response.status_code)
