def decorator_function(func):
    def wrapper_function():
        print("wrapper function worked")
        return func()
    print("decorator function worked")
    return wrapper_function

def show():
    print("show worked")

decorator_show = decorator_function(show)
decorator_show()


# @decorator_function
# def display():
#     print("display worked")
    
# display()