import subprocess
import time
from contextlib import contextmanager
import send_requests
import argparse
import sys


def parse_args(args: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--tasks",
        help="How many coroutines to run for sending request",
        type=int,
        required=True,
    )
    parser.add_argument(
        "--requests",
        help="How many request to send per coroutine",
        type=int,
        required=True,
    )
    parser.add_argument(
        "--trace",
        help="If true trace execution with viztracer",
        action="store_true",
    )
    parser.add_argument(
        "--suppress-output",
        help="If true FastAPI logs will not be printed",
        action="store_true",
    )
    parser.add_argument(
        "--pre-sleep-ms",
        help="How much time to wait (in ms) for FastAPI server to startup",
        type=int,
        default=500,
    )
    return parser.parse_args(args)


@contextmanager
def run_python(
    args: list[str],
    *,
    trace: bool,
    suppress_output: bool,
):
    stdout = subprocess.DEVNULL if suppress_output else None
    executable = "viztracer" if trace else sys.executable
    process = subprocess.Popen([executable, *args], stdout=stdout)
    try:
        yield process
    finally:
        process.terminate()
        process.wait()


if __name__ == "__main__":
    args = ["server.py"]
    options = parse_args(sys.argv[1:])
    with run_python(
        args,
        trace=options.trace,
        suppress_output=options.suppress_output,
    ):
        time.sleep(options.pre_sleep_ms / 1000)
        send_requests.main(options.tasks, options.requests)
    print("Server is down!")
