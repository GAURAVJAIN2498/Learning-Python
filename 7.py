#tuple

t = (1, 2, 3, 4, 5)
print(t[3])  #accessing tuple element       

#python memory manager

x = 7
y = 8
z = 9
id(x)
id(y)
id(z)
 #memory address of x in hexadecimal
print(id(x)) 
print(id(y))  #memory address of y
print(id(z))  #memory address of z
hex(id(18)) 


names = ["vishal", "mehul", "gaurav", "sachin"]
type(names)  #list
# names = ("vishal", "mehul", "gaurav", "sachin")
# type(names)  #tuple
final = names
final[2] = "*****"
print(names)  #names list is also changed because final and names are pointing to the same list in memory
print(final)  
names is final
# names[2] = "*****"
# print(names) #final list is also changed because final and names are pointing to the same list in memory