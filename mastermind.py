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

colorList = ['red', 'yellow', 'green', 'blue', 'purple', 'pink']

class Move:
    def __init__(self, color1, color2, color3, color4):
        self.order = []
        self.order.append(color1)
        self.order.append(color2)
        self.order.append(color3)
        self.order.append(color4)


class Game:
    def __init__(self):
        self.ongoing = True
        self.start = datetime.datetime.now()
        self.turnCount = 0
        self.answer = Move(random.choice(colorList), random.choice(colorList),
                           random.choice(colorList), random.choice(colorList))
        print(self.answer.order)

    def guess(self, color1, color2, color3, color4):
        if self.ongoing:
            blackpegs = 0
            whitepegs = 0
            move = Move(color1, color2, color3, color4)
            if move.order[0] == self.answer.order[0]:
                blackpegs += 1
            if move.order[1] == self.answer.order[1]:
                blackpegs += 1
            if move.order[2] == self.answer.order[2]:
                blackpegs += 1
            if move.order[3] == self.answer.order[3]:
                blackpegs += 1
            for x in self.answer.order:
                if move.order[0] == x and x != 0:
                    whitepegs += 1
                    break
            for x in self.answer.order:
                if move.order[1] == x and x != 1:
                    whitepegs += 1
                    break
            for x in self.answer.order:
                if move.order[2] == x and x != 2:
                    whitepegs += 1
                    break
            for x in self.answer.order:
                if move.order[3] == x and x != 3:
                    whitepegs += 1
                    break

            playerMove = '***Your move:  ***'
            answer = '***Correct answer:   ***'

            for x in move.order:
                playerMove += colors[x]['emoji'] + ' '

            for x in self.answer.order:
                answer += colors[x]['emoji']+' '

            if self.answer.order == move.order:
                self.ongoing = False
                return playerMove + '\n' + '***You Win!***   :smile:'

            self.turnCount += 1

            if self.turnCount >= 12:
                self.ongoing = False
                return playerMove + '\n' + '***You Lose!***   :cry: ' + \
                                    '\n'+ answer

            else:
                return playerMove + '\n' + \
                       '*White Pegs:* ' + str(whitepegs - blackpegs) + '\n' + \
                       '*Black Pegs:* ' + str(blackpegs) + '\n' + \
                       '*Turns left:* ' + str(12 - self.turnCount)
        else:
            return "*This game has ended! Please use '!mm start' to begin a new game!*"




