from contextlib import contextmanager
import time


@contextmanager
def timethis(label):
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print("{0} : {1}".format(label, end))


with timethis('counting'):
    n = 10000
    while n:
        n -= 1
