secret_word = "Awesome"
guess = ""
guess_count = 0
out_of_guesses = False

while guess != secret_word and not out_of_guesses:
    guess = input("Enter the secret word: ")
    guess_count += 1
    if guess_count == 3:
        out_of_guesses = True

if out_of_guesses:
    print("You're out of guesses, you lose but try again!")
else:
    print("You win!")
