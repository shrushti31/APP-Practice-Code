def repeat(num_times):
    """Decorator factory that repeats a function call 'num_times'."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = None
            for i in range(1, num_times + 1):
                print(f"--> Execution #{i}")
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

# Applying the decorator with an argument
@repeat(num_times=3)
def greet(name):
    print(f"Hello, {name}!")

# Usage
greet("shrushti")