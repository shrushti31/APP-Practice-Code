def log_function_call(fun):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {fun.__name__}")
        result = fun(*args, **kwargs)
        print(f"Function {fun.__name__} executed successfully")
        return result
    return wrapper

@log_function_call
def add(a, b):
    return a + b
result = add(5, 3)
print(result)