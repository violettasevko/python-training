import numbers
contin = 'y'
while contin == 'y':
    f_num = int(input("Input number>>"))
    oper = input("Input operation>>")
    s_num = int(input("Input another number>>"))
    if oper == '+':
        print(f_num + s_num)
    elif oper == '-':
        print(f_num - s_num)
    elif oper == '/':
        print(f_num / s_num)
    elif oper == '*':
        print(f_num * s_num)
    else:
        print("Error")
    contin = input("Input 'y' to continue and any key to exit")