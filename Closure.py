def outer(x):
    def inner(y):
        return x + y
    return inner

result = outer(10)
print(result(5))