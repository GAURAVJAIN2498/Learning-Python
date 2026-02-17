def mysum(*data):
    print(data)  # data is a tuple of all the arguments passed to the function
    sum = 0
    for i in data:
        print(i)
        sum = sum + i
    return sum

mysum(*[1, 2, 3, 4, 5])
# mysum(1, 2, 3, 4, 5)