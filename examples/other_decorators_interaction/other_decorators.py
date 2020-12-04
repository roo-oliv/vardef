from functools import wraps


def other_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("other_decorator wrapper executed")
        return func(*args, **kwargs)

    return wrapper


def arg_provider_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("arg_provider_decorator wrapper executed")
        args += ("PROVIDED_VALUE",)
        return func(*args, **kwargs)

    return wrapper
