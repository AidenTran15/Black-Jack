import install_requirements
import casino
import pygame
import sys 
import os
import math
import time
import tkinter as tk
from tkinter import messagebox


pygame.init()
cardBack = pygame.image.load(os.path.join('png', 'cardBack.png'))
screen = pygame.display/set_mode((1300, 900))
pygame.display.set_caption('Black Jack')
clock = pygame.time.Clock()
myfont = pygame.font.SysFont('monospace', 70)
smallFont = pygame.image.load(os.path.join('back', 'background.jpg'))
screen.fill((0,128,0))
clock = pygame.time.Clock()
deck = casino.cards()
cardList = deck.getCards()
d = casino.dealer(cardList)
p = casino.player(cardList)

pygame.display.flip()


onTable= []
topCards = []

cardImg= [None]
    # Load 52 Images
two_clubs = pygame.image.load(os.path.join('png', '2_of_clubs.png'))
two_diamonds = pygame.image.load(os.path.join('png', '2_of_diamonds.png'))
two_hearts = pygame.image.load(os.path.join('png', '2_of_hearts.png'))
two_spades = pygame.image.load(os.path.join('png', '2_of_spades.png'))

three_clubs = pygame.image.load(os.path.join('png', '3_of_clubs.png'))
three_spades = pygame.image.load(os.path.join('png', '3_of_spades.png'))
three_diamonds = pygame.image.load(os.path.join('png', '3_of_diamonds.png'))
three_hearts = pygame.image.load(os.path.join('png', '3_of_hearts.png'))

four_clubs = pygame.image.load(os.path.join('png', '4_of_clubs.png'))
four_spades = pygame.image.load(os.path.join('png', '4_of_spades.png'))
four_diamonds = pygame.image.load(os.path.join('png', '4_of_diamonds.png'))
four_hearts = pygame.image.load(os.path.join('png', '4_of_hearts.png'))

five_clubs = pygame.image.load(os.path.join('png', '5_of_clubs.png'))
five_spades = pygame.image.load(os.path.join('png', '5_of_spades.png'))
five_diamonds = pygame.image.load(os.path.join('png', '5_of_diamonds.png'))
five_hearts = pygame.image.load(os.path.join('png', '5_of_hearts.png'))

six_clubs = pygame.image.load(os.path.join('png', '6_of_clubs.png'))
six_spades = pygame.image.load(os.path.join('png', '6_of_spades.png'))
six_diamonds = pygame.image.load(os.path.join('png', '6_of_diamonds.png'))
six_hearts = pygame.image.load(os.path.join('png', '6_of_hearts.png'))

seven_clubs = pygame.image.load(os.path.join('png', '7_of_clubs.png'))
seven_spades = pygame.image.load(os.path.join('png', '7_of_spades.png'))
seven_diamonds = pygame.image.load(os.path.join('png', '7_of_diamonds.png'))
seven_hearts = pygame.image.load(os.path.join('png', '7_of_hearts.png'))

eight_clubs = pygame.image.load(os.path.join('png', '8_of_clubs.png'))
eight_spades = pygame.image.load(os.path.join('png', '8_of_spades.png'))
eight_diamonds = pygame.image.load(os.path.join('png', '8_of_diamonds.png'))
eight_hearts = pygame.image.load(os.path.join('png', '8_of_hearts.png'))

nine_clubs = pygame.image.load(os.path.join('png', '9_of_clubs.png'))
nine_spades = pygame.image.load(os.path.join('png', '9_of_spades.png'))
nine_diamonds = pygame.image.load(os.path.join('png', '9_of_diamonds.png'))
nine_hearts = pygame.image.load(os.path.join('png', '9_of_hearts.png'))

ten_clubs = pygame.image.load(os.path.join('png', '10_of_clubs.png'))
ten_spades = pygame.image.load(os.path.join('png', '10_of_diamonds.png'))
ten_diamonds = pygame.image.load(os.path.join('png', '10_of_hearts.png'))
ten_hearts = pygame.image.load(os.path.join('png', '10_of_spades.png'))

jack_clubs = pygame.image.load(os.path.join('png', 'jack_of_clubs.png'))
jack_spades = pygame.image.load(os.path.join('png', 'jack_of_spades.png'))
jack_diamonds = pygame.image.load(os.path.join('png', 'jack_of_diamonds.png'))
jack_hearts = pygame.image.load(os.path.join('png', 'jack_of_hearts.png'))

queen_clubs = pygame.image.load(os.path.join('png', 'queen_of_clubs.png'))
queen_spades = pygame.image.load(os.path.join('png', 'queen_of_spades.png'))
queen_diamonds = pygame.image.load(os.path.join('png', 'queen_of_diamonds.png'))
queen_hearts = pygame.image.load(os.path.join('png', 'queen_of_hearts.png'))

king_clubs = pygame.image.load(os.path.join('png', 'king_of_clubs.png'))
king_spades = pygame.image.load(os.path.join('png', 'king_of_spades.png'))
king_diamonds = pygame.image.load(os.path.join('png', 'king_of_diamonds.png'))
king_hearts = pygame.image.load(os.path.join('png', 'king_of_hearts.png'))

ace_clubs = pygame.image.load(os.path.join('png', 'ace_of_clubs.png'))
ace_spades = pygame.image.load(os.path.join('png', 'ace_of_spades.png'))
ace_diamonds = pygame.image.load(os.path.join('png', 'ace_of_diamonds.png'))
ace_hearts = pygame.image.load(os.path.join('png', 'ace_of_hearts.png'))

cardImg.append([ace_clubs, ace_diamonds, ace_hearts, ace_spades])
cardImg.append([two_clubs, two_diamonds, two_hearts, two_spades])
cardImg.append([three_clubs, three_diamonds, three_hearts, three_spades])
cardImg.append([four_clubs, four_diamonds, four_hearts, four_spades])
cardImg.append([five_clubs, five_diamonds, five_hearts, five_spades])
cardImg.append([six_clubs, six_diamonds, six_hearts, six_spades])
cardImg.append([seven_clubs, seven_diamonds, seven_hearts, seven_spades])
cardImg.append([eight_clubs, eight_diamonds, eight_hearts, eight_spades])
cardImg.append([nine_clubs, nine_diamonds, nine_hearts, nine_spades])
cardImg.append([ten_clubs, ten_diamonds, ten_hearts, ten_spades])
cardImg.append([jack_clubs, jack_diamonds, jack_hearts, jack_spades])
cardImg.append([queen_clubs, queen_diamonds, queen_hearts, queen_spades])
cardImg.append([king_clubs, king_diamonds, king_hearts, king_spades])

one = pygame.image.load(os.path.join('chips', '1.png'))
two = pygame.image.load(os.path.join('chips', '2.png'))
five = pygame.image.load(os.path.join('chips', '5.png'))
ten = pygame.image.load(os.path.join('chips', '10.png'))
twenty = pygame.image.load(os.path.join('chips', '20.png'))

didBet = False
betChips = 0
chips = []
betArray = []
playerChips = 50

chips.append([one, 20, 225, 1])
chips.append([two, 20, 300, 2])
chips.append([five, 20, 375, 5])
chips.append([ten, 20, 450, 10])
chips.append([twenty, 20, 525, 20])


def lost():
    screen.fill((0,128,0))
    label = myfont.render('Press any key to play again', 1, (255,255,255))
    label2 = myfont.render('Out of Chips...', 1,(255,255,255))
    screen.blit(label, (100, 450))
    screen.blit(label2, (350, 350))
    pygame.display.update()
    while True:
        ev = pygame.event.poll()
        if ev.type == pygame.KEYDOWN:
            firstStart()
            break
        if ev.type == pygame.QUIT:
            pygame.quit()
    

def bet():
    global betChips
