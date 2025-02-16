import subprocess
import sys
import time
from contextlib import contextmanager
from send_reqs import main


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
        main()
    print("Server is down!")
