import os
path = os.getcwd()
os.chdir('./staff/')
path = os.getcwd()
print(f"My path is {path}")

with open ("data.txt", 'r') as file:
    for data in file:
        data = data.rstrip("\n")
        fname, lname, depart, loc=data.split(', ')
        print("=============")
        print("Firstname: ", fname)
        print("Lastname: ", lname)
        print("Department: ", depart)
        print("Location: ", loc)
        print("=============")
