def mysum(*data):
    print(data)  # data is a tuple of all the arguments passed to the function
    sum = 0
    for i in data:
        print(i)
        sum = sum + i
    return sum

mysum(*[1, 2, 3, 4, 5])
# mysum(1, 2, 3, 4, 5)

math = 50
science = 60
english = 70
history = 80
school_conditions = [
    math > 70,
    science > 80,   
    english > 60,   
    history > 50
]
if all(school_conditions):    #and operator kind of work karta hai, all() function sabhi conditions ko check karta hai aur agar sabhi conditions true hain to hi true return karta hai
    print("You are eligible")
else:
    print("You are not eligible")

if any(school_conditions):    #or operator kind of work karta hai, any() function sabhi conditions ko check karta hai aur agar kisi bhi condition true hai to true return karta hai
    print("You are eligible")   
else:    print("You are not eligible")
