import random
def number_guessing():
    random_number = random.randint(1, 100)
    # print(random_number)  
    while True:
        try:
            guess = int(input("Guess the number: "))
            print(f"Your guess: {guess}")#This line is just to print guessed number i just kept this for my reference
        except ValueError:
            print("Invalid input, Please re-enter a number.")
            continue
        
        if random_number == guess:
            return True
        elif abs(random_number - guess) <= 10:
            if random_number > guess:
                print( "Close but a bit low")
            else:
                print("close but a bit high")
        elif guess < random_number:
            print("Too low!")
        else:
            print("Too high!")

result = number_guessing()
if result:
    print("Congratulations! You guessed the correct number!")
