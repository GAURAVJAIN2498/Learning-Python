db = [1, 2, 3, 4, 5]
output = []
for d in db:
    if d != 3:
        b = d ** d
        output.append(b)
    
print(output) 

# ETL operation
# List comprehension

db = [1, 2, 3, 4, 5]
output = [d ** d if d != 3 else 0 for d in db]
#output = [d ** d for d in db if d != 3]
print(output)