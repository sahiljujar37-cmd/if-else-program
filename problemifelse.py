#WAP a program to check the nummber enetr by user is odd or even


a = int(input("enter any no "))

if(a%2==0):
    print("even")
else:
    print("odd")

    #WAP to find the greatest of 3 no enter by user

a = int(input("enter 1st no"))
b = int(input("enter 2nd no"))
c = int(input("enter 3rd no"))

if(a>b and a>c):
    print("A is greater no",a)
elif(b>a and b>c):
    print("B is greater no",b)
else:
    print("c is greater no",c)

    #WAP to check whether no is multiple of 7

    a = int(input("enter any no"))


    if(a%7==0):
        print("no. is multiple of 7",a)
    else:
        print("no is not multiple of 7",a)