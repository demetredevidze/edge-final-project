# day_1_game.py
# [Demetre Devidze]
# 2020-07-06


import random

hint1 = "But I will give you a hint! Think about the powers of 2."
motivation = "If you play smart you will be able to win the game every single time!"
bye = "No hard feelings, have a nice day! \nPS, come back whenever you like, I will always be around!"
win = "You got it right! You can play again if you like. Just pressing the run button."
help1 = ". \nEvery time you give me a guess, I will tell you whether it is bigger or smaller than the answer."
help2 = " chances to guess a random integer between 1 and "
help3 = "Remember, more guesses means a bigger range of integers to guess from."
user_name = input("Hey, what's your name? \n")
num_of_tries = "how many tries would you like to have:"
level = "Pick the level of difficulty by having as many guesses as you like."
answer_list = "yes" and "Yes" and "YES" and "sure" and "SURE" and "Sure" and "lets do it" and "yeah" and "YEAH" and "Yeah" and "yep"
lets_start = "Great decision " +user_name+ "! " +level+ "\n" +help3+ "\n" +num_of_tries

print("Hi " +user_name+ ", would you like to play a game on guessing random integers?")
play_game = input()

if play_game == "yes" and "Yes" and "YES" and "sure" and "SURE" and "Sure" and "lets do it" and "yeah" and "YEAH" and "Yeah" and "yep":
    print(lets_start)
    lev_of_diff = input()
    rules = "Good! Remember " +user_name+ " you get " +str(lev_of_diff)+help2+ str(
        2 ** int(lev_of_diff))
    print(rules+help1+ " Best of luck!")
    print("PS, " + str(lev_of_diff) + " tries is enough! " +motivation)
    answer = random.randint(1, int(2**int(lev_of_diff)))
    for guess_number in range(int(lev_of_diff)):
        guess = input("what is your guess:")
        if int(guess) == answer:
            print("Well done " +user_name+ "! " +win)
            break
        elif int(guess) > answer:
            print("Too big " +user_name+ "! Try again!")
        elif int(guess) < answer:
            print("Too small " +user_name+ "! Try again!")
    else:
        print("Sorry " +user_name+ "! You are out of guesses!")
        print(hint1 + " Two to the power of " +str(lev_of_diff)+ " is " +str(
        2 ** int(lev_of_diff))+ ". Play smarter next time!")
else:
    print("Okay " +user_name+ "! " +bye)