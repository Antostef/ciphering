from inspect import signature
from functools import wraps
import timeit

def time_this(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = timeit.default_timer()
        result = func(*args, **kwargs)
        end_time = timeit.default_timer()
        
        print(f"This function took {round(end_time - start_time, 4)} seconds")
        return result
    return wrapper


def type_assert(*ty_args, **ty_kwargs):
    def decorate(func):
        # Map function argument names to supplied types
        sig = signature(func)
        bound_types = sig.bind_partial(*ty_args, **ty_kwargs).arguments
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            bound_values = sig.bind(*args, **kwargs)
            for name, value in bound_values.arguments.items():
                if name in bound_types:
                    if not isinstance(value, bound_types[name]):
                        raise TypeError(f"Argument {name} must be {bound_types[name]}")
            return func(*args, **kwargs)
        return wrapper
    return decorate


def inbound_assert(*bo_args, **bo_kwargs):
    def decorate(func):
        bounded_args = bo_kwargs.get("params")

        @wraps(func)
        def wrapper(*args, **kwargs):
            for key, value in bounded_args.items():
                arg_value = kwargs.get(key)

                if value[0] is not None:
                    if arg_value < value[0]:
                        raise ValueError(f"Argument {key} with value {arg_value} is lower than the lowest bound: {value[0]}")
                if value[1] is not None:
                    if arg_value > value[1]:
                        raise ValueError(f"Argument {key} with value {arg_value} is higher than the highest bound: {value[1]}")
            return func(*args, **kwargs)
        return wrapper
    return decorate

