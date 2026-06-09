string=input("Enter you own string here: ")
string2=('')
for i in string:
    string2=i+string2
print("The original string is: ", string)
print("The reversed string is", string2)