class Manager(object):
    def __enter__(self):
        return value

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            return
        else:
            # Handle Exception if required]
            return True  # if exception handle else False


# Usage:

with Manager() as val:
    # ...   # __enter__()
    # statements
    # ...   # __exit__()
    pass
