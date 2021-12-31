# Level-3
# vowels in english are 'a', 'e', 'i', 'o', 'u'.
def num_of_vowels(word):
    vowels = []
    for i in "AEIOUaeiou":
        if(i == "a" or i == "e" or i == "i" or i == "o" or i == "u" or i == "A" or i == "E" or i == "I" or i == "O" or i == "U"):
            vowels = vowels + 1
            return vowels

# output
test1 = num_of_vowels("25Normal")
test2 = num_of_vowels("GKC")
test3 = num_of_vowels("hinkaw sabara")


print(test1)  # 2 printed
print(test2)  # 0 printed
print(test3)  # 5 printed
