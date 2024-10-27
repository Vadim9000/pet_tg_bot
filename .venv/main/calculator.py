contin = 'y'
while contin == 'y':
    f_num = float(input("Enter a first number: "))
    oper = input("Enter a operator: ")
    s_num = float(input("Enter a second number: "))
    if oper == "+":
        print(f_num + s_num)
    elif oper == "-":
        print(f_num - s_num)
    elif oper == "*":
        print(f_num * s_num)
    elif oper == "/":
        print(f_num / s_num)
    else:
        print("Invalid operator")
    contin = input("Press 'y' to continue")