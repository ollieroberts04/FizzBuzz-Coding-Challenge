# When making the code, I first wanted to get the core idea of the number incrementing and checking the input to the
# desired output, done by simply making a function to check what should be input and comparing it the player input.
# After that I first got it to work with two players, by switching between players each time and then moved on to make
# it work with multiple more players. To do this I had to change lots of the code from before, I decided to use sort of
# circular Queue, but obviously only reading the front without dequeuing it, and then removing a player from the queue
# when they get eliminated. The queue is a list of the player numbers. Therefor the while loop lasts until the queue is
# of length one, and therefore only one player remaining.
# After, I decided to add players having multiple lives. To do this I changed the queue from a list to a dictionary,
# with the key as the player number and the value as the number of lives remaining. In order to implement this, I had
# to change how the size checking, winner checking and next player would be decided. I was able to get the next player
# by changing the getFront to make the front the next key value pair without 0 as the value. This also allowed me to
# get the winner by calling the dictionary keys and calling the getFront as it won't have 0 lives. And to check the
# size I used the statement to add up all the values that were not equal to zero using sum()

# to test the solution I tested erroneous inputs, boundry data and accepted input to check all were working correctly

import time


class Players:
    def __init__(self, size, lives):
        self.size = size
        self.players = {player: lives for player in range(1, size + 1)} # makes a dictionary with player numbers as keys and lives as values
        self.front = -1
    def getFront(self):
        self.front = (self.front + 1) % self.size
        while list(self.players.values())[self.front] == 0: # checks the next player is still active
            self.front = (self.front + 1) % self.size
        return list(self.players.keys())[self.front] # return the player number of next player
    def removeLife(self, player):
        self.players[player] -= 1
    def getPlayers(self):
        return list(self.players.keys()) # returns a list only of player numbers
    def getSize(self):
        return sum(player != 0 for player in self.players.values()) # adds up total of players without 0 lives
    def getNumOfLives(self, player):
        return self.players[player]

def explanation():
    print('''The game is based on counting up numbers starting from 1. Players take turns providing the next
correct value.
For each turn:
• If the number is divisible by 3, the player must input: fizz
• If the number is divisible by 5, the player must input: buzz
• If the number is divisible by both 3 and 5, the player must input: fizz buzz
• Otherwise, the player must input the number itself
 You only have 10 seconds to input the answer! ''')
    print('''Example round: 1 1
2 2
3 fizz
4 4
5 buzz
6 fizz
… …
15 fizz buzz
Example mistake:
• If the number is 3 and the player enters 3 instead of fizz, they are eliminated.''')

def getFizzBuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return 'fizz buzz'
    elif num % 3 == 0:
        return 'fizz'
    elif num % 5 == 0:
        return 'buzz'
    else:
        return str(num)

def getPlayerInput(playerNum, num):
    start = time.time()
    playerInput = input(f'(Player {playerNum}) {num}:  ').lower()
    end = time.time()
    if end - start > 10:
        return None
    else:
        return playerInput

def getNumOfPlayers():
    num = input('How many players?: ')
    while not(num.isdigit()) or int(num) <= 1:
        print('Please enter a number greater than 1')
        num = input('How many players?: ')
    return int(num)

def getNumOfLives():
    num = input('How many lives should players get?: ')
    while not(num.isdigit()) or int(num) < 1:
        print('Please enter a number greater than 1')
        num = input('How many lives should players get?: ')
    return int(num)


explanation()
print()
number = 0
numOfPlayers = getNumOfPlayers()
numOfLives = getNumOfLives()
activePlayers = Players(numOfPlayers, numOfLives) # create queue of players
while activePlayers.getSize() > 1: # repeats until only one player has more than 0 lives
    number += 1
    player = activePlayers.getFront() # gets the player whose go is now
    correctAnswer = getFizzBuzz(number) # generates the correct answer
    playerAnswer = getPlayerInput(player, number)
    if not (playerAnswer == correctAnswer):
        activePlayers.removeLife(player) # takes away a life if they get it wrong
        if playerAnswer is None:
            print('Took too long long to answer.')
        else:
            print(f'\nWrong, the answer was {correctAnswer}')
        print(f'Player {player} lost a life. {activePlayers.getNumOfLives(player)} lives left.\n')
winner = activePlayers.getPlayers()[activePlayers.getFront()-1] # assigns the winner to the only player without 0 lives
print(f'Player {winner} won!')