while True:
    op1 = int(input("Enter operand1: "))
    result = op1  
    while True:
        op = input("Enter operator : ")
        if op == '=':
            print("=", result)
            break  
        op2 = int(input("Enter operand2: "))
        if op == '+':
            result += op2
        elif op == '-':
            result -= op2
        elif op == '*':
            result *= op2
        elif op == '%':
            result %= op2
        elif op == '/':
            if op2 == 0:
                print("Division by zero error")
                continue 
            else:
                result /= op2
        else:
            print("Invalid operator")
         