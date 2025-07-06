#cafe management system
total={"bill":0}
def again():
    print("do you want bill or order more")
    print("enter 1 for more order")
    print("enter 2 for bill")
    c=int(input("enter a number"))
    if(c==1):
        happy()
    if(c==2):
        print("Thankyou","lavisha","your bill is",total["bill"]) 
def happy():
    print("enter 1 for burger")
    print("enter 2 for spring roll")
    print("enter 3 for fries")
    print("enter 4 for pizza")
    print("enter 5 for pasta")
    a=int(input("enter a number"))
    if(a==1):
        print("burger")
        total["bill"]+=59
        again()
    if(a==2):
        print("spring roll")
        total["bill"]+=80
        again()
    if(a==3):
        print("fries")
        total["bill"]+=99
        again()
    if(a==4):
        print("pizza")
        total["bill"]+=280
        again()
    if(a==5):
        print("pasta")
        total["bill"]+=320
        again()

happy()
