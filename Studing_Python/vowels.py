# python program to count vowels in a string

str1 = input("Please Enter your own string : ")
vowels = 0

for i in str1:
    if(i == "a" or i == "e" or i == "i" or i == "o" or i == "u" or i == "A" or i == "E" or i == "I" or i == "O" or i == "U"):
        vowels = vowels + 1

print("Total Number of vowels in this string = ", vowels)