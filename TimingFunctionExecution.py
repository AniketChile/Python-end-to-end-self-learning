# write a decorator that measures the time a function takes to execute
import time

def timer(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(f"the {func.__name__} took {end-start} time to get executed")
        return result
    return wrapper

@timer
def example(n):
    time.sleep(n)

example(6)