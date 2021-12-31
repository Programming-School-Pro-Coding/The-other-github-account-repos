import random

def game(right_number, number_of_tries):
    l = []
    print("Try to find the right number in", number_of_tries, "2 times at most !")
    while True:
        if number_of_tries == 0:
            print("Sadly you lose")
            l.append("lost")
            break

        else:
            number_of_tries -= 1

        input_number = int(input("Please Enter your number: "))
        l.append(str(input_number))

        if input_number > right_number:
            print("Your number is bigger")
        elif input_number < right_number:
            print("Your number is small")
        else:
            print("Congralations")
            l.append("won")
            break
    f = open("scores", "a")
    f.write(' '.join(l) + "\n")
    f.close()

def show_history():
    try:
        f = open("scores", "r")
        s = f.read()
        print(s)
        f.close()
    except:
        print("Can't open file")

print("Welcome to our game !!")

while True:
    print("Please choose one of the options : ")
    print("1 - play")
    print("2 - show history")
    print("3 - exit")

    choice = int(input("Please Enter 1 or 2 or 3 : "))

    if choice == 1:
        right_number = random.randint(0, 10)
        print(right_number)
        game(right_number, 5)
    elif choice == 2:
        show_history()
    elif choice == 3:
        print("Thanks for using our game ! hope we see you again.")
        exit(0)
    else:
        print("Please Enter 1 or 2 or 3")



