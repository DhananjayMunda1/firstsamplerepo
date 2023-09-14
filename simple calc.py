print ("Simple Calculator")
print("choose operator (+ - * / % )")

ch=input("Enter the operators")#[0]

if ch=='+':
    a=int(input("Enter the first operand"))
    b=int(input("Enter the second operand"))
    sum=a+b
    print("your entred result is :",sum)
elif ch=='-':
    a=int(input("Enter the first operand"))
    b=int(input("Enter the second operand"))
    sum=a-b
    print("your entred result is :",sum)
elif ch=='/':
    a=int(input("Enter the first operand"))
    b=int(input("Enter the second operand"))
    if(b==0):
        print ("second operand must not be zero")
    else:
        sum=a/b
        print("your entred result is :",sum)
elif ch=='*':
        a=int(input("Enter the first operand"))
        b=int(input("Enter the second operand"))
        sum=a*b
        print("your entred result is :",sum)
elif ch=='%':
        a=int(input("Enter he first operand"))
        b=int(input("Enter the seconf operand"))
        sum=a%b
        print("Your result is :",sum)
else:
    print("You enterd wrong operator")
