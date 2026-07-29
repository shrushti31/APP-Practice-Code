def countdown():
    n = 5
    while n >= 1:
        yield n
        n -= 1

for i in countdown():
    print(i)