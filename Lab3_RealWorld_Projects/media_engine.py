def monitor(func):
    def wrapper(*args, **kwargs):
        print("Processing Started")
        result = list(func(*args, **kwargs))
        print("Processing Completed")
        return result
    return wrapper

@monitor
def play_count_stream(limit):
    for i in range(limit):
        if i % 2 == 0:
            yield i**2