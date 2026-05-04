print("Greetings my dear friend!")
name =input("What is your name my dear friend? ")
print(f"Welcome dear {name} to the number Guessing Game\n""Try to guess the number I am thinking of from 1-100\n""You have 10 tries to get it right!")
import random
random_number = random.randint(1,100)

for attempt in range(1,11):
    guess = int(input(f"Attempt {attempt}: Enter your guess: "))

    if guess>random_number:
        print("OOH GO LOWER!")
    elif guess<random_number:
        print("NAHH GO HIGHER!")
    else:
        print(f"DING DING DING! YOU GOT IT {name}! the number is {random_number}\n"f"You got the answer in {attempt} attempt(s)" )
        break
else:
    print(f"OOPS YOU LOST {name} ! The number was {random_number}")
    