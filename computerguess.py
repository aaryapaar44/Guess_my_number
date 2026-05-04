import random
print("Welcome my dear friend")
name=input("What shall i call you?\n")
print(f"Welcome my dear {name}, I will be your number Akinator for the day.")
print("Let me know if the number is Correct or if I should go Higher or Lower")

low=1
high=100


for attempt in range(1,11):
    guess = random.randint(low, high)
    print(f"Attempt {attempt}: My guess is {guess}")
    feedback= input("Is it (H)igher, (L)ower or (C)orrect?").upper()

    if feedback=='C':
        print(f"My mastery knows no bounds. I got it in only {attempt} attempt(s) ")
        break
    elif feedback=='H':
        low=guess+1
    elif feedback=='L':
        high=guess-1
    else:
        print(f"Invalid Input {name}! Please chose between 'H', 'L', 'C' ")
        break
    if low > high:
        print(f"\nWait... if it's higher than {low-1} and lower than {high+1}...")
        print("You're tricking me! That's impossible.")
        break
else:
    print("\n I ran out of tries. You managed to outsmart me..")