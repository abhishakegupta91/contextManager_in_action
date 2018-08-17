# Automatically deleted Temporary Directory

import shutil
import tempfile


class tempdir(object):
    def __enter__(self):
        self.dirname = tempfile.mkdtemp()
        return self.dirname

    def __exit__(self):
        shutil.rmtree(self.dirname)


with tempdir() as dirname:
    # ...
    # statements
    # ...
    pass
