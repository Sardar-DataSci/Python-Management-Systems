####Student Marks Calculator###
print("==============Student Marks Calculator==============")
name=input("Enter Your name:")
id=int(input("Enter your student id:"))
sub1=int(input("Enter your English Marks:"))
sub2=int(input("Enter your Mathematics Marks:"))
sub3=int(input("Enter your Chemsitry Marks:"))

print("==============Student Report card==============")

print("Name:",name)
print("Id:",id)

shortid=name[0:3]
print(shortid)
sttotalmarks=sub1+sub2+sub3
totalmarks=sttotalmarks/300*100
percentage=totalmarks

print("Total marks:",sttotalmarks)
print("Percentage:",percentage)

if(percentage>90):
    print("Grade:A+")
    print("Status:Pass")
elif(percentage>80 and percentage<90) :
    print("Grade:A")
    print("Status:Pass")
elif(percentage>70 and percentage<80):
    print("Grade:B")
    print("Status:Pass")      
elif(percentage>60 and percentage<70):
    print("Grade:C")
    print("Status:Pass")    
else:
    print("Fail")    