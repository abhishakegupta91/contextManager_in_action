from contextlib import contextmanager


@contextmanager
def my_file_io(filename, mode):
    f = open(filename, mode)
    yield f
    f.close()


with my_file_io('demo.txt', 'w') as fin:
    print("Hello World, this is to write in a file")
    fin.write('Hello World !!!')
