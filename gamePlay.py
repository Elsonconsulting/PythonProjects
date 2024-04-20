# in this game the player and computer will have different decks.
# Initial bet minimum is £5
# The player will then see one of his cards and one of the computer cards
# The player can then choose to increase his stake
# The player will then request more cards until he sticks or exceeds 21 and auto looses
# If player achieves 21 he automatically wins
# If the player has not busted the computer will take cards until exceeds player value 
# If the computer exceeds player value and does not exceed 21 computer wins.

from random import randint

cDeck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]




def PlayerHand():
    pDeck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    x = randint(0,12)
    print(pDeck[x])

PlayerHand()








