tupdata=("Jawad",19,"Bs Accounting",4.0,"Kasur",)
print("Student Name:",tupdata[0])
print("Student CGPA is:",tupdata[-2])
print("Student Name and Age:",tupdata[:2])
print("Student Program and CGPA:",tupdata[2:4])
if tupdata[3]>=4.0:
    print("Excellent Student")
elif tupdata[3]>3.0 and tupdata[3]<3.5:
    print("Good Student")
else:
    print("Need Improvement")        