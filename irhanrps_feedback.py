#Name: Irhan Iftikar
#Date: February 28, 2023
#Description: Rock, Paper, Scissor Program that plays a game between the user and computer
#Challenges: Game determines who the winner is after each round, game also keeps track of the score
#Bugs: No bugs found
#Sources: No outside sources used
import sys
import random       #imports random module that will randomize computer's answer
weapons = ["rock", "paper", "scissor"]     #List of answers for the computer
user_score = 0              #Initializes variable for user's score as 0
computer_score = 0          #Initializes variable for computer's score as 0
print("Welcome to the Rock, Paper, Scissor Game!")      #welcomes user to the program
while True:             #while loop that exists until user quits the program
    user_answer = input("Enter 'rock', 'paper', or 'scissor': ")        #prompts the user for choice of rock, paper, scissor

    if user_answer not in weapons:
        print("Invalid. Try again")

    else:
        computer_answer = random.choice(weapons)           #Randomly generates computer answer from the list

        if user_answer == computer_action:
            print("Tie")
        elif user_answer == "rock":               #If user enters rock...
            if computer_answer == "paper":         #If computer answer is paper...
                print("Computer wins!")             #prints computer wins
                computer_score += 1                 #Adds one to the computer's score
            elif computer_answer == "scissor":    #Otherwise computer answer is scissor...
                print("You win!")                   #Prints user wins
                user_score += 1                     #Adds one to the user's score
        elif user_answer == "paper":            #If user enters paper...
            if computer_answer == "scissor":       #If computer answer is scissor...
                print("Computer wins!")               #prints computer wins
                computer_score += 1                   #Adds one to the computer's score
            elif computer_answer == "rock":        #If computer answer is rock...
                print("You win!")                   #Prints user wins
                user_score += 1                     #Adds one to the user's score
        elif user_answer == "scissor":          #If user answers with scissor...
            if computer_answer == "rock":           #If computer answer was rock...
                print("Computer wins!")                 #prints computer wins
                computer_score += 1                     #Adds one to the computer's score
            elif computer_answer == "paper":        #Otherwise computer answer was paper...
                print("You win!")                       #Prints user wins
                user_score += 1                 #       Adds one to the user's score
        else:                                   #Otherwise answer wasn't eligible...
            print("Answer not understood. Try again")   #Prints answer wasn't understood 

        print(f"Your Answer: {user_answer} Computer Answer: {computer_answer})
        print("User Score: ", user_score, ".", "Computer Score: ", computer_score)  #prints score of the game

        while True:
            play_again = input("Would you like to play again? Enter 'yes' or 'no': ")   #Asks user if they would like to play again

            if play_again == "yes":            #If user answers yes...
                print("Continuing program!")        #Program continues
                break                            #Continues while loop
            elif play_again == "no":        #If user answers no...
                print("Ending program!")
                sys.exit()                           #Breaks while loop and stops program
            else:                       #Otherwise user answers a different answer...
                print("Invalid. Try again")


