import subprocess
import sys
import time
from contextlib import contextmanager
import send_requests


@contextmanager
def run_python(args: list[str]):
    process = subprocess.Popen([sys.executable, *args], stdout=subprocess.DEVNULL)
    try:
        yield process
    finally:
        process.terminate()
        process.wait()


if __name__ == "__main__":
    args = ["server.py"]
    with run_python(args):
        time.sleep(0.5)
        send_requests.main()
    print("Server is down!")
