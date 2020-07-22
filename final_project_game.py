# final.project.py
# [Demetre Devidze]


import random

smart = ". Play smarter next time!"
luck = " Best of luck!"
guess_it = "what is your guess:"
hint1 = "But I will give you a hint! Think about the powers of 2. Two to the power of "
motivation = " tries is enough! If you play smart you will be able to win the game every single time!"
bye = "! No hard feelings, have a nice day! \nPS, come back whenever you like, I will always be around!"
win = "You got it right! You can play again if you like. Just pressing the run button."
help1 = ". \nEvery time you give me a guess, I will tell you whether it is bigger or smaller than the answer."
help2 = " chances to guess a random integer between 1 and "
help3 = "Remember, more guesses means a bigger range of integers to guess from."
num_of_tries = "how many tries would you like to have?\n"
level = "Pick the level of difficulty by having as many guesses as you like."
answer_list = "yes" or "Yes" or "YES" or "sure" or "SURE" or "Sure" or "Yeah" or "YEAH" or "yeah" or "yep"
answers_and = "yes" and "YES" and "Yes" and "sure" and "yeah"
user_name = input("Hey, what's your name? \n")
lets_go = "Great decision " +user_name+ "! " +level+ "\n" +help3+ "\n" +num_of_tries
lose = "Sorry " +user_name+ "! You are out of guesses!"
good = "Good! Remember " +user_name+ " you get "
good_bye = "Okay " +user_name+bye
well_done = "Well done " +user_name+ "! " +win
too_big = "Too big " +user_name+ "! Try again!"
too_small = "Too small " +user_name+ "! Try again!"
start_game = "Hi " +user_name+ ", would you like to play a game on guessing random integers?\n"
play_game = input(start_game)


if play_game == answer_list:
    lev_of_diff = input(lets_go)
    range1 = int(lev_of_diff) - 1
    rules = good+str(lev_of_diff)+help2+str(2 ** int(lev_of_diff) - 1)
    print(rules+help1+luck)
    print("PS, "+str(lev_of_diff)+motivation)
    answer = random.randint(1, int(2**int(lev_of_diff) - 1))
    for guess_number in range(int(lev_of_diff)):
        guess = input(guess_it)
        if int(guess) == answer:
            print(well_done)
            break
        elif int(guess) > answer:
            print(too_big)
        elif int(guess) < answer:
            print(too_small)
    else:
        print(lose)
        print(hint1+str(lev_of_diff)+" is "+str(2 ** int(lev_of_diff))+smart)
else:
    print(good_bye)