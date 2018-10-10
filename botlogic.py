
import datetime
import decimal
import random
#TODO: Make this a class instead and keep everything in one file. One for all the content and one for running


#
# This function returns how much time remains in the Fall 2018 semester.
# In terms of format, this should be applicable to any start/end date.
#
def percentFall2018():

    start = datetime.datetime(2018, 8, 27, 0, 0, 0, 0) #Start of Fall 2018, being 8/27/2018
    now = datetime.datetime.now() #Now
    end = datetime.datetime(2018, 12, 8, 0, 0 , 0 , 0) #End of Fall 2018, being 12/8/2018

    total = end-start
    daysSpent = now-start

    percentDone = (daysSpent/total) * 100
    decimalDone = decimal.Decimal(percentDone) #Converting from float to decimal

    return str(round(decimalDone, 4)) #Converting from decimal to string

def rockPaperScissors(hand):

    hand = str.lower(hand)
    moveList = ['rock', 'paper', 'scissors']

    botHand = random.choice(moveList)

    if botHand == 'rock':
        if hand == 'paper':
            return 'I chose rock! You won against me with '
        if hand == 'scissors':
            return 'I chose rock! You lost to me with '
        if hand == 'rock':
            return 'I chose rock! You tied with me using '

    if botHand == 'paper':
        if hand == 'paper':
            return 'I chose paper! You tied with me using '
        if hand == 'scissors':
            return 'I chose paper! You won against me with '
        if hand == 'rock':
            return 'I chose paper! You lost to me with '

    if botHand == 'scissors':
        if hand == 'paper':
            return 'I chose scissors! You lost to me with '
        if hand == 'scissors':
            return 'I chose scissors! You tied with me using '
        if hand == 'rock':
            return 'I chose scissors! You won against me with '

    if hand != 'scissors' or 'paper' or 'rock':
        return "¯\_(ツ)_/¯ I'm not familiar with the hand shape: "
def checkDay():
    return datetime.datetime.today().weekday()

