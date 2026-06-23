import itertools
import sys
import threading
import time


class Spinner:
    def __init__(self, message):
        self.message = message
        self._done = threading.Event()
        self._thread = threading.Thread(target=self._animate, daemon=True)

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._done.set()
        self._thread.join()
        self._clear_line()

    def _animate(self):
        for frame in itertools.cycle("|/-\\"):
            if self._done.is_set():
                break

            sys.stdout.write(f"\r{frame} {self.message}")
            sys.stdout.flush()
            time.sleep(0.12)

    def _clear_line(self):
        sys.stdout.write("\r" + " " * (len(self.message) + 4) + "\r")
        sys.stdout.flush()
