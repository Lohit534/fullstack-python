op1=int(input("Enter operand1:"))
op=input("Enter operator:")
op2=int(input("Enter operand2:"))
if op == '+':
    result=op1 + op2
elif op=='-':
    result=op1 - op2
elif op=='*':
    result=op1 * op2
elif op=='%':
    result= op1 % op2
elif op=='/':
    if op1==0:
        print("division by zero")
    else:
        result=op1/op2
else:
    print("None")
print("=",result)
