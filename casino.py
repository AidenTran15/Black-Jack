
import random 
 # Card Value
 # 1: Ace
 # 2 - 10: 2 - 10
 # 11: Jack
 # 12: Queen
 # 13 : King
 # Suits
 # H: Hearts
 # D: Diamonds
 # C: Clubs
 # S: Spades


class cards:
     def __init__(self):
         self.cardsL = []
         for x in range(1,14):
             card = x
             for i in range(4):
                if i == 0:
                    suit = 'H'
                elif i == 1:
                    suit = 'D'
                elif i == 2:
                    suit = 'C'
                elif i == 3:
                    suit = 'S'
                self.cardsL.append([card, suit])

