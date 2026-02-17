def lw(i, j):
    print("Learning Python")
    # return [i + j, i-j, i*j, i/j]
    return(i + j, i-j, i*j, i/j)  
    print("This will not be printed")   # This line will not be executed as it is after the return statement    
print(lw(18, 5))


def data(city, country, continent):
    print("ur city is : " + city)
    print("ur country is : " + country)
    print("ur  in : " + continent)
data("Mumbai", "India", "Asia")
