import functools

def note(func):
    "note function"
    @functools.wraps(func)
    def wrapper():
        "wrapper function"
        print("note somthing")
        return func
    return wrapper

@note
def test():
    "test function"
    print("i am test")

test()
print(test.__doc__)
#无@functools.wraps(func)装饰时：wrapper function
#有@functools.wraps(func)装饰时：test function
