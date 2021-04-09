import time

def duration(function):
    def wrapper(*args, **kwargs):
        before = time.time()
        func = function(*args, **kwargs)
        after = time.time()
        print(f"{function.__name__} run time was {after-before} seconds")
        return func
    return wrapper

"""
example:
@duration
def demo():
    time.sleep(2)
    print("************")

demo()
"""