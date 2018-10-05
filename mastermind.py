import random
import datetime

colors = {
    'red':{'emoji': ':heart:'},
    'yellow':{'emoji': ':yellow_heart:'},
    'green':{'emoji': ':green_heart:'},
    'blue':{'emoji': ':blue_heart:'},
    'purple':{'emoji': ':purple_heart:'},
    'pink':{'emoji': ':sparkling_heart:'}
}

class Move:
    def __init__(self, color1, color2, color3, color4):
        self.order = []
        self.order[0] = color1
        self.order[1] = color2
        self.order[2] = color3
        self.order[3] = color4


class Game:
    def __init__(self):
        self.ongoing = False
        self.start = datetime.datetime.now()
        self.turnCount = 0
        self.answer = Move(random.choice(colors), random.choice(colors),
                           random.choice(colors), random.choice(colors))

    def guess(self, color1, color2, color3, color4):
        blackpegs = 0
        whitepegs = 0
        move = Move(color1, color2, color3, color4)
        if move.order[0] == color1:
            blackpegs += 1
        if move.order[1] == color2:
            blackpegs += 1
        if move.order[2] == color3:
            blackpegs += 1
        if move.order[3] == color4:
            blackpegs += 1
        for x in self.answer.order:
            if move.order[0] == x and x != 0:
                whitepegs += 1
        for x in self.answer.order:
            if move.order[1] == x and x != 1:
                whitepegs += 1
        for x in self.answer.order:
            if move.order[2] == x and x != 2:
                whitepegs += 1
        for x in self.answer.order:
            if move.order[3] == x and x != 3:
                whitepegs += 1

        playerMove = '*Your move: *'

        for x in move.order:
            playerMove += colors[x]['emoji']+' '

        if self.answer.order == move.order:
            self.ongoing = False
            return playerMove + '\n'+' ***You Win!*** :smile:'

        self.turnCount += 1

        if self.turnCount >= 12:
            self.ongoing = False
            return playerMove + '\n'+' ***You Lose!*** :cry: '

        else:
            return playerMove +'\n'+\
            '*White Pegs:* '+str(whitepegs)+'\n'+\
            '*Black Pegs:* '+str(blackpegs)+'\n'+\
            '*Turns left:* '+(12-self.turnCount)




