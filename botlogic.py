
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


#
# This function rolls 4d6, and picks the highest 3.
#
def rollStats():
    dice = []
    for n in range(4):
        dice.append(random.randint(1,6))

    sorted_dice = sorted(dice, reverse=True)

    d1 = sorted_dice[0]
    d2 = sorted_dice[1]
    d3 = sorted_dice[2]

    return d1+d2+d3


#
# This function contains a list of D&D 5th Edition Races and Classes
# More importantly, it will "roll" a character with race, class, and appropriate statistic scores.
#
def rollCharacter():
    raceList = ['Aarakocra', 'Aasimar', 'Bugbear', 'Centaur', 'Changeling',
                'Dragonborn', 'Dwarf', 'Elf', 'Feral Tiefling', 'Firbolg', 'Genasi',
                'Gith', 'Gnome', 'Goblin', 'Goliath', 'Half-Elf', 'Halfling', 'Half-Orc',
                'Hobgoblin', 'Human', 'Kalashtar', 'Kenku', 'Kobold', 'Lizardfolk', 'Loxodon',
                'Minotaur', 'Orc', 'Shifter', 'Simic Hybrid', 'Tabaxi', 'Tiefling', 'Tortle',
                'Triton', 'Vedalken', 'Viashino', 'Warforged', 'Yuan-ti Pureblood']

    classList = ['Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Monk', 'Paladin',
                 'Ranger', 'Rogue', 'Sorcerer', 'Warlock', 'Wizard', 'Blood Hunter']

    charAlignment = str

    moralList = ['Lawful', 'Neutral', 'Chaotic']
    alignList= ['Good', 'Neutral', 'Evil']

    charMoral = random.choice(moralList)
    charAlign = random.choice(alignList)

    if charMoral == charAlign:
        charAlignment = 'True Neutral'
    else:
        charAlignment = charMoral+" "+charAlign



    charStr = rollStats()
    charDex = rollStats()
    charCon = rollStats()
    charInt = rollStats()
    charWis = rollStats()
    charCha = rollStats()


    charRace = random.choice(raceList)
    charClass = random.choice(classList)


    #############################################################
    # From here until the next block is code for race modifiers.#
    #############################################################

    races = {
    	'Aarakocra':{'str': 0,'dex': 2,'con': 0, 'int': 0, 'wis': 1, 'cha': 0,
                     'traits':{'Flight, Talons'},
                     'actions': {},
                     'languages': {'Common', 'Aarakocra'}
                    },
        'Aasimar':{'str': 0, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0, 'cha': 2,
                   'traits':{'Darkvision, Celestial Resistance, Light Bearer'},
                   'actions':{'Healing Hands'},
                   'languages': {'Common', 'Celestial'}
                   },
        'Bugbear':{'str': 2, 'dex': 1, 'con': 0, 'int': 0, 'wis': 0, 'cha': 0,
                   'traits':{'Darkvision', 'Long-Limbed', 'Powerful Build', 'Sneaky'},
                   'actions':{'Surprise Attack'},
                   'languages':{'Common', 'Goblin'}
                   },
        'Centaur':{'str': 2, 'dex': 0, 'con': 0, 'wis': 1, 'cha': 0,
                   'traits':{'Hooves','Equine Build', 'Survivor', 'Hybrid Nature'},
                   'actions':{'Charge'},
                   'languages':{'Common', 'Sylvan'}
                   },
        'Changeling':{'str': 0, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0, 'cha': 2,
                      'traits':{'Changeling Instincts', 'Divergent Persona'},
                      'actions':{'Change Appearance', 'Unsettling Visage'},
                      'languages':{'Common'} #Choice of more
                      },
        'Dragonborn':{'str': 2, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0, 'cha': 1,
                      'traits':{'Damage Resistance'},
                      'actions':{'Breath Weapon'}, #Based on ancestry
                      'languages':{'Common', 'Draconic'}
                      },
        'Dwarf':{'str': 0, 'dex': 0, 'con': 2, 'wis': 0, 'cha': 0,
                 'traits':{'Darkvision', 'Dwarven Resilience', 'Dwarven Combat Training', 'Tool Proficiency', 'Stonecunning'},
                 'actions':{},
                 'languages':{'Common', 'Dwarvish'}
                 },
        'Elf':{'str': 0, 'dex': 2, 'con': 0, 'int': 0, 'wis': 0, 'cha': 0,
               'traits':{'Darkvision', 'Keen Senses', 'Fey Ancestry', 'Trance',},
               'actions':{},
               'languages':{'Common', 'Elvish'}
               },
        'Feral Tiefling':{'str': 0, 'dex': 2, 'con': 0, 'int': 1, 'wis': 0, 'cha': 0,
                          'traits':{'Darkvision', 'Hellish Resistance', 'Infernal Legacy'},
                          'actions':{},
                          'languages':{'Common', 'Infernal'}
                          },
        'Firbolg':{'str': 1, 'dex': 0, 'con': 0, 'int': 0, 'wis': 2, 'cha': 0,
                   'traits':{'Firbolg Magic', 'Powerful Build', 'Speech of Beast and Leaf'},
                   'actions':{'Hidden Step'},
                   'languages':{'Common', 'Elvish', 'Giant'}
                   },
        'Genasi':{'str': 0, 'dex': 0, 'con': 2, 'int': 0, 'wis': 0, 'cha': 0,
                  'traits':{}, #Varies based on type.
                  'actions':{},
                  'languages':{'Common', 'Primordial'}
                  },
        'Gith':{'str': 0, 'dex': 0, 'con': 0, 'int': 1, 'wis': 0, 'cha': 0,
                'traits':{},
                'actions':{}, #Varies based on type
                'languages':{'Common', 'Gith'}
                },
        'Gnome':{'str': 0, 'dex': 0, 'con': 0, 'int': 2, 'wis': 0, 'cha': 0,
                 'traits':{'Darkvision', 'Gnome Cunning'},
                 'actions':{}, #Varies based on type
                 'languages':{'Common', 'Gnomish'}
                 },
        'Goblin':{'str': 0, 'dex': 2, 'con': 1, 'int': 0, 'wis': 0, 'cha': 0,
                  'traits':{'Darkvision'},
                  'actions':{'Fury of the Small', 'Nimble Escape'},
                  'languages':{'Common', 'Goblin'}
                  },
        'Goliath':{'str': 2, 'dex': 0, 'con': 1, 'int': 0, 'wis': 0, 'cha': 0,
                   'traits':{'Natural Athlete', 'Powerful Build', 'Mountain Born'},
                   'actions':{"Stone's Endurance"},
                   'languages':{'Common', 'Giant'}
                   },
        'Half-Elf':{'str': 0, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0, 'cha': 2,
                    'traits':{'Darkvision', 'Fey Ancestry', 'Skill Versatility'}, #Additions based on type
                    'actions':{},
                    'languages':{'Common', 'Elvish', 'Choice'}
                    },
        'Half-Orc':{'str': 2, 'dex': 0, 'con': 1, 'int': 0, 'wis': 0, 'cha': 0},
        'Halfling':{'str': 0, 'dex': 2, 'con': 0, 'int': 0, 'wis': 0, 'cha': 0},
        'Hobgoblin':{'str': 0, 'dex': 0, 'con': 2, 'int': 1, 'wis': 0, 'cha': 0},
        'Human':{'str': 1, 'dex': 1, 'con': 1, 'int': 1, 'wis': 1, 'cha': 1},
        'Kalashtar':{'str': 0, 'dex': 0, 'con': 0, 'int': 0, 'wis': 1, 'cha': 1},
        'Kenku':{'str': 0, 'dex': 2, 'con': 0, 'int': 0, 'wis': 1, 'cha': 0},
        'Kobold':{'str': -2, 'dex': 2, 'con': 0, 'int': 0, 'wis': 0, 'cha': 0},
        'Lizardfolk':{'str': 0, 'dex': 0, 'con': 2, 'int': 0, 'wis': 1, 'cha': 0},
        'Loxodon':{'str': 0, 'dex': 0, 'con': 2, 'int': 0, 'wis': 1, 'cha': 0},
        'Minotaur':{'str': 2, 'dex': 0, 'con': 1, 'int': 0, 'wis': 0, 'cha': 0},
        'Orc':{'str': 2, 'dex': 0, 'con': 1, 'int': -1, 'wis': 0, 'cha': 0},
        'Shifter':{'str': 0, 'dex': 1, 'con': 0, 'int': 0, 'wis': 0, 'cha': 0},
        'Simic Hybrid':{'str': 0, 'dex': 0, 'con': 2, 'int': 0, 'wis': 0, 'cha': 0},
        'Tabaxi':{'str': 0, 'dex': 2, 'con': 0, 'int': 0, 'wis': 0, 'cha': 1},
        'Tiefling':{'str': 0, 'dex': 2, 'con': 0, 'int': 1, 'wis': 0, 'cha': 0},
        'Tortle':{'str': 2, 'dex': 0, 'con': 0, 'int': 0, 'wis': 1, 'cha': 0},
        'Triton':{'str': 1, 'dex': 0, 'con': 1, 'int': 0, 'wis': 0, 'cha': 1},
        'Vedalken':{'str': 0, 'dex': 0, 'con': 0, 'int': 2, 'wis': 1, 'cha': 0},
        'Viashino':{'str': 1, 'dex': 2, 'con': 0, 'int': 0, 'wis': 0, 'cha': 0},
        'Warforged':{'str': 0, 'dex': 0, 'con': 1, 'int': 0, 'wis': 0, 'cha': 0},
        'Yuan-ti Pureblood':{'str': 0, 'dex': 0, 'con': 0, 'int': 1, 'wis': 0, 'cha': 2}
	}

    charStr += races[charRace]['str']
    charDex += races[charRace]['dex']
    charCon += races[charRace]['con']
    charWis += races[charRace]['wis']
    charCha += races[charRace]['cha']

    if charRace == 'Changeling':
        choice = random.randint(1,2)
        if choice == 1:
            charDex += 1
        else:
            charInt += 1
    elif charRace == 'Half-Elf':
        for x in range(2): #There are two points to assign, so the loop iterates twice
            choice = random.randint(1,5) #Randomly assigns an ability to increment
            if choice == 1:
                charStr += 1
            if choice == 2:
                charDex += 1
            if choice == 3:
                charCon += 1
            if choice == 4:
                charInt += 1
            if choice == 5:
                charDex += 1
    elif charRace == 'Kalashtar':
        choice = random.randint(1, 6)  # Randomly assigns an ability to increment
        if choice == 1:
            charStr += 1
        if choice == 2:
            charDex += 1
        if choice == 3:
            charCon += 1
        if choice == 4:
            charInt += 1
        if choice == 5:
            charDex += 1
        if choice == 6:
            charCha += 1
    elif charRace == 'Simic Hybrid':
        choice = random.randint(1, 5)  # Randomly assigns an ability to increment
        if choice == 1:
            charStr += 1
        if choice == 2:
            charDex += 1
        if choice == 3:
            charCha += 1
        if choice == 4:
            charInt += 1
        if choice == 5:
            charDex += 1

    ###########################
    # Race modifiers end here.#
    ###########################

	#Str, Dex, Con, Int, Wis, Cha

    rtn = 'Race: '+str(charRace)+'\n' +\
          'Class: '+str(charClass)+'\n\n' +\
          'Strength: '+str(charStr)+'\n' +\
          'Dexterity: '+str(charDex)+'\n' +\
          'Constitution: '+str(charCon)+'\n' +\
          'Intelligence: '+str(charInt)+'\n' +\
          'Wisdom: '+str(charWis)+'\n' +\
          'Charisma: '+str(charCha)+'\n\n'+\
          'Alignment: '+charAlignment

    return rtn



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

