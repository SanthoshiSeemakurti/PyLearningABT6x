import functools


def before_after_UI_test(func):
    def wrapper():
        print("Before UI test")
        func()
        print("After UI test")
    return wrapper()


@before_after_UI_test
def test_ui():
    print("I'm testing web UI test")
