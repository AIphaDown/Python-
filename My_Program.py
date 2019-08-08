import sys

user1 = input("what's your name?")
user2 = input("and your name?")

user1_answer = input(user1 + ", do you choose rock, paper, or scissors?")
user2_answer = input(user2 + ", do you choose rock, paper, or scissors?")
christianMinecraftserver = input("Would any of you like to learn about our lord and savior Cheesus Puffus?")

def compare(a1, a2):
    if a1 == a2:
        return("It's a draw!")
    elif a1 == "rock":
        if a2 == "scissors":
            return("Rock wins! GG No ree")
        else:
            return("Paper Wins! oof.")

    elif a1 == "scissors":
        if a2 == "paper":
            return ("Scissors wins! Winner Winner Chicken Dinner!")
        else:
            return ("Rock wins. I'm brock hard!!")

    elif a1 == "paper":
        if a2 == "rock":
            return ("Papel wins! Usted chupa ha!")
        else:
            return ("Scissors wins! But it was me DIO!")
    else:
        return ("Your dumb. Type either rock, paper, or scissors.")
        sys.exit()
print( compare(user1_answer , user2_answer))