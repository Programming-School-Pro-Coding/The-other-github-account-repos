#Level-3
#vowels in english are 'a', 'e', 'i', 'o', 'u'.
def replace_vowels(word, char):
    f = ""
    for letter in word:
        if letter in "AEIOUaeiou":
            f += char
        else:
            f += letter
    return f


#output
test1 = replace_vowels("the aordvork", "#")
test2 = replace_vowels("minnie mouse", "?")
test3 = replace_vowels("shakespeare", "*")


print(test1) # "th# ##rdv#rk" printed
print(test2) # "m?nn?? m??s?" printed
print(test3) # "sh*k*sp**r*" printed