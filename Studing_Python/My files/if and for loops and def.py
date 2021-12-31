def cal():
    number1 = float(input("Please Enter number : "))
    oprator = input("Please Enter oprator : ")
    number2 = float(input("Please Enter number2 : "))
    if oprator == "+":
        print(number1 + number2)
    elif oprator == "-":
        print(number1 - number2)
    elif oprator == "*":
        print(number1 * number2)
    elif oprator == "/":
        print(number1 / number2)
    else:
        print("The oprator is False")

cal()