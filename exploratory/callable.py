"""
Having recently run into an object not being callable (it was a *dict* instance),
I've decided to explore further the implications of it. Let's see what happens
when we define a __call()__ method...
"""


class SomeCallable:
    def __init__(self, func):  # Pass a function here...
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f"__call__ invoked function: {self.func.__name__}")
        return self.func(*args, **kwargs)


def print_args(*args, **kwargs):
    print("Arguments:")
    for item in args:
        print(f"\t- {item}")
    print("Keyword args:")
    for key, value in kwargs.items():
        print(f"\tKey: {key}, value: {value}")


def add_one(num: int):
    return num + 1


@SomeCallable
def monkey():
    print("Monkey!")


if __name__ == '__main__':
    a = SomeCallable(print_args)
    b = SomeCallable(add_one)

    a(1, 2, 3, 4, 5, one=1, two='Two', three=3.0)
    c = b(41)
    print(f"c = {c}")

    d = SomeCallable(a.__call__)  # Pass another class instance's __call__ method

    d(9, 8, 7, eenie=0, meenie=2, moe=b)

    monkey()  # Decorated function - __call__ method of the decorating class should be invoked

    e = SomeCallable(add_one.__call__)  # Explicitly pass function object's __call__ method
    print(f"When I'm {e(63)}")
