# day_1_game.py
# [Demetre Devidze]



import random

rules = "Rules are simple! You get 5 chances to guess a random integer between 0 and 30. "
hint1 = "PS, 5 tries is definitely enough! If you play smart you will be able to win the game every single time!"
hint2 = "Think about the powers of 2. Two to the power of five is 32, so you have enough number of tries."
user_name = input("Hey, what's your name? \n")
print("Hi " + user_name + ", would you like to play a game on guessing random numbers?")
play_game = input()

if play_game == "yes" or "Yes" or "YES" or "yeah" or "YEAH" or "Yeah" or "Sure" or "sure" or "SURE" or "lets do it":
    print("Great decision " + user_name + "! " + rules + " Good luck!")
    print(hint1)
    answer = random.randint(0, 30)
    for guess_number in range(5):
        guess = input("what is your guess:")
        if int(guess) == answer:
            print("Well done " + user_name + "! You got it right!")
            break
        elif int(guess) > answer:
            print("Too big " + user_name + "! Try again!")
        elif int(guess) < answer:
            print("Too small " + user_name + "! Try again!")
    else:
        print("Sorry " + user_name + "! You are out of guesses!")
        print("But I will give you a hint! " + hint2 + " Play smarter next time!")
else:
    print("Okay " + user_name + "! No hard feelings, have a nice day!")