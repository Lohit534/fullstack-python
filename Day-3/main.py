import arth as me
number_1=int(input())
while True:
    op = input()
    if op == "=":
        print("= ",number_1)
        break
    number_2 = int(input())
    if op == "+":
        number_1 = me.add(number_1 , number_2)
    elif op == "-":
        number_1 = me.sub(number_1 , number_2)
    elif op == "*":
        number_1 = me.mul(number_1 , number_2)
    elif op == "/":
        number_1 = me.div(number_1 , number_2)
    elif op =="%":
        number_1=me.div(number_1,number_2)
    elif op=="**":
        number_1=me.div(number_1,number_2)
    print(number_1)