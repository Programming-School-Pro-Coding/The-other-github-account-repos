count = int(input("How many numbers do you have ? "))

numbers = []
for i in range(count):
          n = int(input("Enter a number: "))
          numbers.append(n * 2)
          print(f"in {i}: {numbers}")

print(numbers)