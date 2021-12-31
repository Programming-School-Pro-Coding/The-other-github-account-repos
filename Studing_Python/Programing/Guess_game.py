secret_word = "Programing"
guess = ""
number_of_guess = 0
guess_limit = 3
out_of_guess = False

while guess != secret_word and not out_of_guess:
          if number_of_guess < guess_limit:
                    guess = input("Enter the Guess word: ")
                    number_of_guess += 1
          else:
                    out_of_guess = True

if out_of_guess:
          print("You lose !!!")
else:
          print("You win !!!")