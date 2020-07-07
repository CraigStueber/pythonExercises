import random

def game(choice):

    options = ["rock", "paper", "scissors"]
    bot = random.choice(options)

    if choice == "rock" and bot == "scissors":
        print("you chose rock and i played scissors, you got lucky")
    elif choice == "rock" and bot == "paper":
        print (" you chose rock and i played paper, YOU LOSE! Bow before your computer GOD!!!")
    elif choice == "rock" and bot == "rock":
        print ("we chose the same thing...")
    elif choice == "paper" and bot == "paper":
        print ("we chose the same thing.")
    elif choice == "paper" and bot == "scissors":
        print ("you chose paper and i chose scissors, YOU LOSE! Bow before your computer GOD!!!")
    elif choice == "paper" and bot == "rock":
        print ("you chose paper and i chose rock, you got lucky")
    elif choice == "scissors" and bot == "scissors":
        print ("We chose the same thing")
    elif choice == "scissors" and bot == "paper":
        print ("you chose scissors and i chose paper, you got lucky")
    elif choice == "scissors" and bot == "rock":
        print ("you chose scissors and i chose rock, YOU LOSE! Bow before your computer GOD!!!")

def again(x):

    while True:
        if x == "y":
            game(input("rock, paper or scissors?   \n"))
            again(input("play again? y / n   \n"))
        else:
            print("QUITTER!!! I KNEW YOU WERE SCARED!!! BEGONE HUMAN!!")
            break
        break

game(input("rock, paper or scissors?   \n"))
again(input("play again? y / n   \n" ))

   

