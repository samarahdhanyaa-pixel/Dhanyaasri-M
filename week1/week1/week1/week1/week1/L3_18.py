secret_num= 7

guess = int(input("Guess the number: "))

while guess != secret_num:
    if guess > secret_num:
        print("Too high")
    else:
        print("Too low")
    guess = int(input("Guess again: "))

print("Correct!You've guessed it!")

