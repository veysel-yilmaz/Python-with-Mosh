"""i = 1
guess = int(input('Guess: '))
while i <= 3:
    print(f"Guess: {guess}")
    i = i + 1"""
#answer:
secret_number = 9
guess_count = 0 # press shift+F6 to rename all instances!
guess_limit = 3 # instead of writing 3 in while loop.
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
        print('You won!')
        break # stops while loop and gets the programme out from while loop.
        # if we wont write break here, the result will ask for guess again.
else:
    print('Sorry, you failed!')
