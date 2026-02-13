s = "linux"
s = s + " " + "world" + " " + "is great"
print(s)


name = ['vishal', 'mehul@ongraph.com', 'gaurav', 'sachin', '']
final_email = [n + "@company.com" for n in name if not n.endswith("ongraph.com")]
print(final_email)

final_email = [n if n.endswith('@ongraph.com') 
    else (n + "@company.com")
    for n in name]
print(final_email)

