studentnum=input("Enter your full name:")
print("First Character of name is:",studentnum[0])
print("Last three charcters of name:",studentnum[-1],studentnum[-2],studentnum[-3])
print("First five charcters:",studentnum[:6])
print("Name into upercaseletter",studentnum.capitalize())
print("Name with slash",studentnum.replace(" ","-"))

marks=(78,85, 92, 88, 76)
marks=list(marks)
print("Higest marks are:")
print("First two marks:",marks[:2])
avergae=marks[0]+marks[1]+marks[2]+marks[3]+marks[4]/4
if avergae>=80:
    print("Excellent Student")
else:
    print("Need Improvement")    

Hobby=input("Enter your  hobbies")
Hobby=list(Hobby)    
print("Hobby 1:",Hobby[0])
print("Hobby 2:",Hobby[1])
print("Hobby 3:",Hobby[2])
