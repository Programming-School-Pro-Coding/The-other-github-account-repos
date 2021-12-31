# num1 = input("Please Enter the First Number: ")
# num2 = input("Please Enter the last Number: ")
operator = input("Enter the Operator: ")

def plus(num1, num2):
          resulte = float(num1) + float(num2)
          print(resulte)
          return resulte

def subs(num1, num2):
          resulte = float(num1) - float(num2)
          print(resulte)
          return resulte

def muti(num1, num2):
          resulte = float(num1) * float(num2)
          print(resulte)
          return resulte

def div(num1, num2):
          resulte = float(num1) / float(num2)
          print(resulte)
          return resulte

if operator == "+":
          plus(input("Please Enter the First Number: "), input("Please Enter the Last Number: "))
if operator == "-":
          subs(input("Please Enter the First Number: "), input("Please Enter the Last Number: "))
if operator == "*":
          muti(input("Please Enter the First Number: "), input("Please Enter the Last Number: "))
if operator == "/":
          div(input("Please Enter the First Number: "), input("Please Enter the Last Number: "))

print("The End ")