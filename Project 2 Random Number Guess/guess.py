import random


def guess_the_game(x):
    randon_number = random.randint(1,x)
    guess = 0
    while guess != randon_number:
        guess = int(input(f"Take a guess between 1 - {x} : --->  "))
        if guess < randon_number:
            print(f"Guess again! {guess} is too low")
        elif guess > randon_number:
            print(f"Guess again! {guess} is too high")
        else:
            break

    return f"You did it. The random number was {randon_number}"

print(guess_the_game(5))



