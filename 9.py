from datetime import date


def sum(*x): # *x is tuple of all the arguments passed to the function
    j = 0
    for i in x:
        j += i 
    return j

print(sum(1, 2, 3, 4, 5))



def process_data(*data):
    output = []
    for d in data:
        if d != 6:
            b = d ** d
            output.append(b)
    return output
        
print(process_data(1, 2, 3, 4, 5))