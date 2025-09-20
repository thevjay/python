from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello! from say_hello function. chaicode")

say_hello()
print(say_hello.__name__)  # Output: wrapper
print(say_hello.__doc__)   # Output: None