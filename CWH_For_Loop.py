#To print the items in the list having datatype integer and and greater than or equal to 6
list1=[2,4,6,8,"virat","dhoni","dhawan"]
print("Comman Method")
for item in list1:
    if type(item)==int and item>=6:
        print(item)
print("Un-Comman Method")
for item in list1:
    if str(item).isnumeric() and item>=6 :
        print(item)

