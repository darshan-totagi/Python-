num1=int(input("enter the num1:"))
num2=int(input("enetr the num2:"))
opr=input("enter the operator(+,-,/,*):")
if opr=="+":
    print(num1+num2)
elif opr=="-":
    print(num1-num2)
elif opr=="*":
    print(num1*num2)
elif opr=="/":
    print(num1/num2)
else:
    print("invalid operator")
