from contextlib import contextmanager


@contextmanager
def my_tag(name):
    print("<{0}>".format(name))
    yield
    print("</{0}>".format(name))


with my_tag('h1'):
    print("Hey I am a heading tag")
    print("Hello World")

with my_tag('Body'):
    print("Hey I am the body of message")
