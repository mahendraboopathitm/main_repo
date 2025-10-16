def infinite_counter():
    n = 1
    while True:
        yield n
        n += 1
for num in infinite_counter():
    if num > 5:
        break
    print(num)
