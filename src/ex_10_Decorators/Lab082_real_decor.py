import time

def print_logs(func):
    def wrapper():
        print("Start of the logs")
        func()
        print("End of the logs")
        print("")
    return wrapper

def time_decorator(func):
    def wrapper():
        start_time = time.time()
        print("Start time", start_time)
        func()
        end_time = time.time()
        print("End time", end_time)
        print("Total time taken by the function:", end_time - start_time)
        print("")
    return wrapper


@time_decorator
def test_ui_1():
    print("Add a function, time taken by this function 1")
    time.sleep(2)

#@time_decorator
@print_logs
def test_ui_2():
    print("Add a function, time taken by this function 2")
    time.sleep(5)


