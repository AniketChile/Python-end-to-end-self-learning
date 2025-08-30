# Implement a decorator that caches the return values of function so that when it's called with the same arguments, the cached value is returned instead of re-executing the function
import time
def cache(func):
    cachedData = {}
    print(cachedData)
    def wrapper(*args):
        if args in cachedData:
            return cachedData[args]
        result = func(*args)
        cachedData[args] = result
        return result
    return wrapper
    

@cache
def longrunfunc(a,b):
    time.sleep(4)
    return a+b

print(longrunfunc(5,2))
print(longrunfunc(4,2))
print(longrunfunc(4,2))

# ok now i think i am pretty confident in python so you can ask me the interview questions that are mostly ask on the python be it theortical or explain or the coding like including everything that is mostly asked in the python interview.
