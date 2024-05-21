import random
from collections import Counter
#Counter is a class from the module collections
def roll(numOfDice=5): #method to roll dice
    return [random.randint(1, 6) for i in range(numOfDice)]


def showDice(dice): #method to print out values 
    print("Dice:", " ".join(map(str, dice))) #.join makes everything one string 



def scoreUpperSection(dice, num): #method to work out the score 
    return dice.count(num) * num #for a specific number in the upper section of the scorecard





def scoreThreeOf_a_Kind(dice): # to work out "three of a kind" 
    if any(count >= 3 for count in Counter(dice).values()):
        return sum(dice)
    return 0






def scoreFourOf_a_Kind(dice): #work out "four of a kind"
    if any(count >= 4 for count in Counter(dice).values()):
        return sum(dice)
    return 0





def scoreFullHouse(dice):
    counts = Counter(dice).values()
    if 3 in counts and 2 in counts:
        return 25
    return 0


def scoreSmallStraight(dice): # to work out small straight - uDice stands for unique dice 
    uDice = sorted(set(dice))
    if len(uDice) >= 4 and any(uDice[i:i+4] == [x, x+1, x+2, x+3] for i, x in enumerate(uDice[:-3])):
        return 30                       #enumerate helps you loop through a list and  
    return 0                            #gets the position (index) of each item
                                        #and the item itself


def scoreLargeStraight(dice):
    uDice = sorted(set(dice))
    if len(uDice) == 5 and uDice == list(range(uDice[0], uDice[0]+5)):
        return 40
    return 0

def scoreYahtzee(dice):
    if len(set(dice)) == 1:
        return 50
    return 0



def scoreChance(dice):
    return sum(dice)



def chooseCat(dice, scores): #choose categories
    print("Choose a category to score:")
    print("1. Upper Section (1-6)")
    print("2. Three of a Kind")
    print("3. Four of a Kind")
    print("4. Full House")
    print("5. Small Straight")
    print("6. Large Straight")
    print("7. Yahtzee")
    print("8. Chance")

    while True:
        choice = input("What numbers the category? ")
        if choice.isdigit() and 1 <= int(choice) <= 8:
            choice = int(choice)
            if scores[choice - 1] == -1:
                break
            else:
                print("Categorys already been used so choose another.")
        else:
            print("No, cant choose that. Choose again.")
    
    if choice == 1:
        num = int(input("What number (1-6) for the upper section? "))
        score = scoreUpperSection(dice, num)
    elif choice == 2:
        score = scoreThreeOf_a_Kind(dice)
    elif choice == 3:
        score = scoreFourOf_a_Kind(dice)
    elif choice == 4:
        score = scoreFullHouse(dice)
    elif choice == 5:
        score = scoreSmallStraight(dice)
    elif choice == 6:
        score = scoreLargeStraight(dice)
    elif choice == 7:
        score = scoreYahtzee(dice)
    elif choice == 8:
        score = scoreChance(dice)
    
    scores[choice - 1] = score
    return scores



#game loop in this method
def yahtzee():
    print("Yahtzee is a dice game where players take turns rolling five dice")
    print("and try to score points by getting specific combinations.")
    print("This version of Yahtzee in Python is multi-")
    print("player and controlled through the terminal.")
    startGame = input("Do you want to play Yahtzee? ").strip().lower()
    if startGame == "yes":
        players = int(input("Great. How many people are playing? "))
        rounds = 5
        scores = [[-1]*8 for i in range(players)]




        for roundNumber in range(rounds): #outer loop for number of rounds
            for player in range(players): #inner loop to go over each player
                print(f"\nPlayer {player + 1}'s turn (Round {roundNumber + 1})") #f for f string
                dice = roll()
                for i in range(2):
                    showDice(dice)
                    reroll = input("Enter the positions (1-5) of dice to reroll (e.g., 1 3 4 - (AND INCLUDE THE SPACES) ), or press Enter to keep: ")
                    if reroll.strip():
                        rerollIND = [int(pos) - 1 for pos in reroll.split()]
                        newRolls = roll(len(rerollIND))
                        for i, new_roll in zip(rerollIND, newRolls): #zip takes two or more lists and pairs up their elements. 
                            dice[i] = new_roll                       #Each pair is a tuple containing one element from each list at the same position
                    else:
                        break

                showDice(dice)
                scores[player] = chooseCat(dice, scores[player])
                print(f"Scores for Player {player + 1}: {scores[player]}")
        
        
        totScores = [sum(player_scores) for player_scores in scores]
        for player, score in enumerate(totScores):
            print(f"Total score for Player {player + 1}: {score}")
        
        winner = totScores.index(max(totScores)) + 1
        print(f"Player {winner} wins with {max(totScores)} points")
    else:
        print("Ok, maybe next time? Bye")
        quit()

yahtzee()
