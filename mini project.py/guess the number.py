import random
secret=random.randint(1,100)
print("I am thinking a number between 1 to 100")
for i in range(1,7):
    guess=int(input("Take a guess:"))
    if guess<secret:
        print("your guess is too low")
    elif guess>secret:
        print("your guess is too high")
    else:
     break
if guess==secret:
    print("congo,you guessed the right number"+str(i)+"guesses!")
else:
    print("oops! your guess was wrong,the number is"+" "+ str(secret))

