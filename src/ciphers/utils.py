import timeit

def time_this(func):
    def wrapper(*args, **kwargs):
        start_time = timeit.default_timer()
        result = func(*args, **kwargs)
        end_time = timeit.default_timer()
        
        print(f"This function took {round(end_time - start_time, 4)} seconds")
        return result
    return wrapper
