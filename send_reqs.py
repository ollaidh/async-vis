import requests


if __name__ == "__main__":
    response = requests.get("http://127.0.0.1:8888/stocks/history")
    print(response.text)

    response = requests.get("http://127.0.0.1:8888/stocks/info")
    print(response.text)

    response = requests.get("http://127.0.0.1:8888/stocks/sectors")
    print(response.text)