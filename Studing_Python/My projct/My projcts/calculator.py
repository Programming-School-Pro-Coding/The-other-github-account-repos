num1 = float(input("please Enter the first number : "))
operator = input("please Enter the operator : ")
num2 = float(input("please Enter the second number : "))

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)
else:
    print("wrong operator please try again")

def power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result
print(power(5,5))