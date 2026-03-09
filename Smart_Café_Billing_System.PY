#Smart Cafe Billing System
print("===============Smart Cafe Billing System===============")
name=input("Enter Your name:")
length=len(name)
lett1=name[0]
lett2=name[-1]
lett3=name[0:3]
print("\nHello Welcome",name,"To Smart Cafe")
print("\nYour Name Length is:",length)
print("\nYour name first letter is:",lett1)
print("\nYour name last letter is:",lett2)
print("\nYour name first 3 letter are:",lett3)

print("===============Menu===============")
print("\n1.Zinger Burger-Rs 450")
print("\n2.Fries-Rs 150")
print("\n3.Cold Drink-Rs 120")
print("=====================Bill================")
choice=int(input("\nChoose Your item from 1-3:\n"))


price_burger=450
price_fries=150
price_colddrink=120

if choice==1:
    item="Zinger Burger"
    price=price_burger
elif choice==2:
    item="Fries"
    price=price_fries
elif choice==3:
    item="Cold Drink"
    price=price_colddrink
else:
    print("\nInvalid Choice")
    exit()
print("Item:",item)
qty=int(input("\nEnter your Food Qantity:"))
print("Quantity:",qty)
totalBill=price*qty

if (totalBill>=1000):
    discount=totalBill *0.1
    final=totalBill-discount
    message="10% Discount Applied"
elif(totalBill>=500):
    discount=totalBill*0.05
    final=totalBill-discount
    message="5% Discount Applied"
else:
    discount=0
    final=totalBill
    message="No discount"
print("\n==============Bill=============\n")
print("\nItem:",item)
print("\nQuantity:",qty)
print("\ntotal Price:",totalBill)
print("\nDiscount:",discount)
print("\nMessage:",message)
print("\nFinal Bill:",final)    

print("\nThank You for visitng Cafe",name,"\n")


