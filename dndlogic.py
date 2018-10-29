import random

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
# More importantly, it will "roll" a character with race, subrace, class, and appropriate ability scores.
#
def rollCharacter():
    raceList = ['Aarakocra', 'Aasimar', 'Bugbear', 'Centaur', 'Changeling',
                'Dragonborn', 'Dwarf', 'Elf', 'Firbolg', 'Genasi',
                'Gith', 'Gnome', 'Goblin', 'Goliath', 'Half-Elf', 'Halfling', 'Half-Orc',
                'Hobgoblin', 'Human', 'Kalashtar', 'Kenku', 'Kobold', 'Lizardfolk', 'Loxodon',
                'Minotaur', 'Orc', 'Shifter', 'Simic Hybrid', 'Tabaxi', 'Tiefling', 'Tortle',
                'Triton', 'Vedalken', 'Viashino', 'Warforged', 'Yuan-ti Pureblood'] #This contains a list of race names as strings
    classList = ['Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Monk', 'Paladin',
                 'Ranger', 'Rogue', 'Sorcerer', 'Warlock', 'Wizard', 'Bloodhunter'] #This contains a list of class names as strings

    charRace = random.choice(raceList)
    charClass = random.choice(classList)

    return constructCharacter(charRace, charClass)


def rollCharacterInput(raceInput, classInput):
    raceList = ['Aarakocra', 'Aasimar', 'Bugbear', 'Centaur', 'Changeling',
                'Dragonborn', 'Dwarf', 'Elf', 'Firbolg', 'Genasi',
                'Gith', 'Gnome', 'Goblin', 'Goliath', 'Half-Elf', 'Halfling', 'Half-Orc',
                'Hobgoblin', 'Human', 'Kalashtar', 'Kenku', 'Kobold', 'Lizardfolk', 'Loxodon',
                'Minotaur', 'Orc', 'Shifter', 'Simic Hybrid', 'Tabaxi', 'Tiefling', 'Tortle',
                'Triton', 'Vedalken', 'Viashino', 'Warforged', 'Yuan-ti Pureblood'] #This contains a list of race names as strings
    classList = ['Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Monk', 'Paladin',
                 'Ranger', 'Rogue', 'Sorcerer', 'Warlock', 'Wizard', 'Bloodhunter'] #This contains a list of class names as strings

    raceFound = False
    if raceInput.casefold() == 'any':
        charRace = random.choice(raceList)
        raceFound = True
    elif raceInput.casefold() != 'any':
        for x in raceList:
            if x.casefold() == raceInput.casefold():
                raceFound = True
                charRace = x
                break

    if not raceFound:
        return "I don't recognize that race, sorry!\nTry '!rollcharacter <race> <class>'"

    classFound = False
    if classInput.casefold() == 'any':
        charClass = random.choice(classList)
        classFound = True
    elif classInput.casefold() != 'any':
        for x in classList:
            if x.casefold() == classInput.casefold():
                classFound = True
                charClass = x
                break

    if not classFound:
        return "I don't recognize that class, sorry!\nTry '!rollcharacter <race> <class>'"

    return constructCharacter(charRace, charClass)


def constructCharacter(charRace, charClass):

    #############################################################
    # From here until the next block is code for race modifiers.#
    #############################################################

    feralTraits = ["Devil's Tongue", "Hellfire", "Winged"] #A dictionary of bonuses for Feral Tieflings.
    races = {
        'Aarakocra': {'str': 0, 'dex': 2, 'con': 0, 'int': 0, 'wis': 1, 'cha': 0,
                      'traits': {'Flight, Talons'},
                      'actions': {},
                      'languages': {'Common', 'Aarakocra', 'Auran'},
                      'subraces': {}
                      },
        'Aasimar': {'str': 0, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0, 'cha': 2,
                    'traits': {'Darkvision, Celestial Resistance, Light Bearer'},
                    'actions': {'Healing Hands'},
                    'languages': {'Common', 'Celestial'},
                    'subraces': {
                        'Protector': {
                            'modifiers': {'str': 0, 'dex': 0, 'con': 0, 'int': 0, 'wis': 1, 'cha': 0},
                            'features': ['Radiant Soul'],
                            'languages': []
                        },
                        'Scourge': {
                            'modifiers': {'str': 0, 'dex': 0, 'con': 1, 'int': 0, 'wis': 0, 'cha': 0},
                            'features': ['Radiant Consumption'],
                            'languages': []
                        },
                        'Fallen': {
                            'modifiers': {'str': 1, 'dex': 0, 'con': 1, 'int': 0, 'wis': 0, 'cha': 0},
                            'features': ['Necrotic Shroud'],
                            'languages': []
                        }
                    }
                    },
        'Bugbear': {'str': 2, 'dex': 1, 'con': 0, 'int': 0, 'wis': 0, 'cha': 0,
                    'traits': {'Darkvision', 'Long-Limbed', 'Powerful Build', 'Sneaky'},
                    'actions': {'Surprise Attack'},
                    'languages': {'Common', 'Goblin'},
                    'subraces': {}
                    },
        'Centaur': {'str': 2, 'dex': 0, 'con': 0, 'wis': 1, 'cha': 0,
                    'traits': {'Hooves', 'Equine Build', 'Survivor', 'Hybrid Nature'},
                    'actions': {'Charge'},
                    'languages': {'Common', 'Sylvan'},
                    'subraces': {}
                    },
        'Changeling': {'str': 0, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0, 'cha': 2,
                       'traits': {'Changeling Instincts', 'Divergent Persona'},
                       'actions': {'Change Appearance', 'Unsettling Visage'},
                       'languages': {'Common', 'Choice', 'Choice'},
                       'subraces': {}
                       },
        'Dragonborn': {'str': 2, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0, 'cha': 1,
                       'traits': {'Damage Resistance'},
                       'actions': {'Breath Weapon'},  # Based on ancestry
                       'languages': {'Common', 'Draconic'},
                       'subraces': {
                           'Black (Acid)': {
                               'modifiers': {'str': 0, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0, 'cha': 0},
                               'features': [],
                               'languages': []
                           },
                           'Blue (Lightning)': {
                               'modifiers': {'str': 0, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0, 'cha': 0},
                               'features': [],
                               'languages': []

                           },
                           'Brass (Fire)': {
                               'modifiers': {'str': 0, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0, 'cha': 0},
                               'features': [],
                               'languages': []
                           },
                           'Bronze (Lightning)': {
                               'modifiers': {'str': 0, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0, 'cha': 0},
                               'features': [],
                               'languages': []
                           },
                           'Copper (Acid)': {
                               'modifiers': {'str': 0, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0, 'cha': 0},
                               'features': [],
                               'languages': []
                           },
                           'Gold (Fire)': {
                               'modifiers': {'str': 0, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0, 'cha': 0},
                               'features': [],
                               'languages': []
                           },
                           'Green (Poison)': {
                               'modifiers': {'str': 0, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0, 'cha': 0},
                               'features': [],
                               'languages': []
                           },
                           'Red (Fire)': {
                               'modifiers': {'str': 0, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0, 'cha': 0},
                               'features': [],
                               'languages:': []
                           },
                           'Silver (Cold)': {
                               'modifiers': {'str': 0, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0, 'cha': 0},
                               'features': [],
                               'languages': []
                           },
                           'White (Cold)': {
                               'modifiers': {'str': 0, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0, 'cha': 0},
                               'features': [],
                               'languages': []
                           }
                       }
                       },
        'Dwarf': {'str': 0, 'dex': 0, 'con': 2, 'int': 0, 'wis': 0, 'cha': 0,
                  'traits': {'Darkvision', 'Dwarven Resilience', 'Dwarven Combat Training', 'Tool Proficiency',
                             'Stonecunning'},
                  'actions': {},
                  'languages': {'Common', 'Dwarvish'},
                  'subraces': {
                      'Duergar': {
                          'modifiers': {'str': 1, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0, 'cha': 0},
                          'features': ['Superior Darkvision', 'Duergar Resilience', 'Duergar Magic',
                                       'Sunlight Sensitivity'],
                          'languages': ['Undercommon'],
                      },
                      'Hill': {
                          'modifiers': {'str': 0, 'dex': 0, 'con': 0, 'int': 0, 'wis': 1, 'cha': 0},
                          'features': ['Dwarven Toughness'],
                          'languages': []
                      },
                      'Mountain': {
                          'modifiers': {'str': 2, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0, 'cha': 0},
                          'features': ['Dwarven Armor Training'],
                          'languages': []
                      }
                  }
                  },
        'Elf': {'str': 0, 'dex': 2, 'con': 0, 'int': 0, 'wis': 0, 'cha': 0,
                'traits': {'Darkvision', 'Keen Senses', 'Fey Ancestry', 'Trance', },
                'actions': {},
                'languages': {'Common', 'Elvish'},
                'subraces': {  # Hold on to your hats ladies and gentlemen, because there is no shortage of subraces.
                    'Avariel': {
                        'modifiers': {'str': 0, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0, 'cha': 1},
                        'features': ['Flight'],
                        'languages': ['Auran']
                    },
                    'Dark': {
                        'modifiers': {'str': 0, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0, 'cha': 1},
                        'features': ['Superior Darkvision', 'Drow Magic', 'Sunlight Sensitivity',
                                     'Drow Weapon Training'],
                        'languages': []
                    },
                    'Eladrin': {
                        'modifiers': {'str': 0, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0, 'cha': 1},
                        'features': ['Seasons', 'Fey Step'],
                        'languages': []
                    },
                    'Grugach': {
                        'modifiers': {'str': 1, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0, 'cha': 0},
                        'features': ['Grugach Weapon Training', 'Cantrip (Druid)'],
                        'languages': ['Sylvan']
                    },
                    'High': {
                        'modifiers': {'str': 0, 'dex': 0, 'con': 0, 'int': 1, 'wis': 0, 'cha': 0},
                        'features': ['Elf Weapon Training', 'Cantrip (Wizard)'],
                        'languages': ['Choice']
                    },
                    'Sea': {
                        'modifiers': {'str': 0, 'dex': 0, 'con': 1, 'int': 0, 'wis': 0, 'cha': 0},
                        'features': ['Sea Elf Weapon Training', 'Child of the Sea', 'Friend of the Sea'],
                        'languages': ['Aquan']
                    },
                    'Shadar-kai': {
                        'modifiers': {'str': 0, 'dex': 0, 'con': 1, 'int': 0, 'wis': 0, 'cha': 0},
                        'features': ['Necrotic Resistance', 'Blessing of the Raven Queen'],
                        'languages': [],
                    },
                    'Wood': {
                        'modifiers': {'str': 0, 'dex': 0, 'con': 0, 'int': 0, 'wis': 1, 'cha': 0},
                        'features': ['Elf Weapon Training', 'Fleet of Foot', 'Mask of the Wild'],
                        'languages': [],
                    },
                }
                },
        'Firbolg': {'str': 1, 'dex': 0, 'con': 0, 'int': 0, 'wis': 2, 'cha': 0,
                    'traits': {'Firbolg Magic', 'Powerful Build', 'Speech of Beast and Leaf'},
                    'actions': {'Hidden Step'},
                    'languages': {'Common', 'Elvish', 'Giant'},
                    'subraces': {}
                    },
        'Genasi': {'str': 0, 'dex': 0, 'con': 2, 'int': 0, 'wis': 0, 'cha': 0,
                   'traits': {},  # Varies based on type.
                   'actions': {},
                   'languages': {'Common', 'Primordial'},
                   'subraces': {
                       'Air': {
                           'modifiers': {'str': 0, 'dex': 1, 'con': 0, 'int': 0, 'wis': 0, 'cha': 0},
                           'features': ['Unending Breath', 'Mingle with the Wind'],
                           'languages': [],
                       },
                       'Earth': {
                           'modifiers': {'str': 1, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0, 'cha': 0},
                           'features': ['Earth Walk', 'Merge with Stone'],
                           'languages': []
                       },
                       'Fire': {
                           'modifiers': {'str': 0, 'dex': 0, 'con': 0, 'int': 1, 'wis': 0, 'cha': 0},
                           'features': ['Darkvision', 'Fire Resistance', 'Reach to the Blaze'],
                           'languages': []
                       },
                       'Water': {
                           'modifiers': {'str': 0, 'dex': 0, 'con': 0, 'int': 0, 'wis': 1, 'cha': 0},
                           'features': ['Acid Resistance', 'Amphibious', 'Swim', 'Call to the Wave'],
                           'languages': []
                       }

                   }
                   },
        'Gith': {'str': 0, 'dex': 0, 'con': 0, 'int': 1, 'wis': 0, 'cha': 0,
                 'traits': {},
                 'actions': {},  # Varies based on type
                 'languages': {'Common', 'Gith'},
                 'subraces': {
                     'Githyanki': {
                         'modifiers': {'str': 2, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0, 'cha': 0},
                         'features': ['Decadent Mastery', 'Martial Prodigy', 'Githyanki Psionics'],
                         'languages': []
                     },
                     'Githzerai': {
                         'modifiers': {'str': 0, 'dex': 0, 'con': 0, 'int': 0, 'wis': 2, 'cha': 0},
                         'features': ['Decadent Mastery', 'Martial Prodigy', 'Githyanki Psionics'],
                         'languages': [],
                     }
                 }
                 },
        'Gnome': {'str': 0, 'dex': 0, 'con': 0, 'int': 2, 'wis': 0, 'cha': 0,
                  'traits': {'Darkvision', 'Gnome Cunning'},
                  'actions': {},  # Varies based on type
                  'languages': {'Common', 'Gnomish'},
                  'subraces': {
                      'Deep': {
                          'modifiers': {'str': 0, 'dex': 1, 'con': 0, 'int': 0, 'wis': 0, 'cha': 0},
                          'features': ['Superior Darkvision', 'Stone Camouflage', 'Svirfneblin Magic'],
                          'languages': ['Undercommon']
                      },
                      'Forest': {
                          'modifiers': {'str': 0, 'dex': 1, 'con': 0, 'int': 0, 'wis': 0, 'cha': 0},
                          'features': ['Natural Illusionist', 'Speak with Small Beasts'],
                          'languages': []
                      },
                      'Rock': {
                          'modifiers': {'str': 0, 'dex': 0, 'con': 1, 'int': 0, 'wis': 0, 'cha': 0},
                          'features': ["Artificer's Lore", "Tinker"],
                          'languages': []
                      }
                  }
                  },
        'Goblin': {'str': 0, 'dex': 2, 'con': 1, 'int': 0, 'wis': 0, 'cha': 0,
                   'traits': {'Darkvision'},
                   'actions': {'Fury of the Small', 'Nimble Escape'},
                   'languages': {'Common', 'Goblin'},
                   'subraces': {}
                   },
        'Goliath': {'str': 2, 'dex': 0, 'con': 1, 'int': 0, 'wis': 0, 'cha': 0,
                    'traits': {'Natural Athlete', 'Powerful Build', 'Mountain Born'},
                    'actions': {"Stone's Endurance"},
                    'languages': {'Common', 'Giant'},
                    'subraces': {}
                    },
        'Half-Elf': {'str': 0, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0, 'cha': 2,
                     'traits': {'Darkvision', 'Fey Ancestry', 'Skill Versatility'},  # Additions based on type
                     'actions': {},
                     'languages': {'Common', 'Elvish', 'Choice'},
                     'subraces': {}
                     },
        'Half-Orc': {'str': 2, 'dex': 0, 'con': 1, 'int': 0, 'wis': 0, 'cha': 0,
                     'traits': {'Darkvision', 'Menacing'},
                     'actions': {'Relentless Endurance', 'Savage Attacks'},
                     'languages': {'Common', 'Orc'},
                     'subraces': {}
                     },
        'Halfling': {'str': 0, 'dex': 2, 'con': 0, 'int': 0, 'wis': 0, 'cha': 0,
                     'traits': {'Lucky', 'Brave', 'Halfling Nimbleness'},
                     'actions': {},
                     'languages': {'Common', 'Halfling'},
                     'subraces': {
                         'Ghostwise': {
                             'modifiers': {'str': 0, 'dex': 0, 'con': 0, 'int': 0, 'wis': 1, 'cha': 0},
                             'features': {'Silent Speech'},
                             'languages': {}
                         },
                         'Lightfoot': {
                             'modifiers': {'str': 0, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0, 'cha': 1},
                             'features': ['Naturally Stealthy'],
                             'languages': []
                         },
                         'Stout': {
                             'modifiers': {'str': 0, 'dex': 0, 'con': 1, 'int': 0, 'wis': 0, 'cha': 0},
                             'features': ['Stout Resilience'],
                             'languages': []
                         }
                     }
                     },
        'Hobgoblin': {'str': 0, 'dex': 0, 'con': 2, 'int': 1, 'wis': 0, 'cha': 0,
                      'traits': {'Darkvision', 'Martial Training'},
                      'actions': {'Saving Faces'},
                      'languages': {'Common', 'Goblin'},
                      'subraces': {}
                      },
        'Human': {'str': 1, 'dex': 1, 'con': 1, 'int': 1, 'wis': 1, 'cha': 1,
                  'traits': {''},
                  'actions': {''},
                  'languages': {'Common', 'Choice'},
                  'subraces': {}
                  },
        'Kalashtar': {'str': 0, 'dex': 0, 'con': 0, 'int': 0, 'wis': 1, 'cha': 1,
                      'traits': {'Dual Mind', 'Mental Discipline', 'Psychic Glamour', 'Severed from Dreams'},
                      'actions': {'Mind Link'},
                      'languages': {'Common', 'Quori', 'Choice'},
                      'subraces': {}
                      },
        'Kenku': {'str': 0, 'dex': 2, 'con': 0, 'int': 0, 'wis': 1, 'cha': 0,
                  'traits': {'Kenku Training'},
                  'actions': {'Expert Forgery', 'Mimicry'},
                  'languages': {'Common', 'Auran'},
                  'subraces': {}
                  },
        'Kobold': {'str': -2, 'dex': 2, 'con': 0, 'int': 0, 'wis': 0, 'cha': 0,
                   'traits': {'Darkvision', 'Pack Tactics', 'Sunlight Sensitivity'},
                   'actions': {'Grovel, Cower, and Beg'},
                   'languages': {'Common', 'Draconic'},
                   'subraces': {}
                   },
        'Lizardfolk': {'str': 0, 'dex': 0, 'con': 2, 'int': 0, 'wis': 1, 'cha': 0,
                       'traits': {"Hold Breath", "Hunter's Lore", "Natural Armor", },
                       'actions': {'Bite', "Cunning Artisan", "Hungry Jaws"},
                       'languages': {'Common', 'Draconic'},
                       'subraces': {}  # Maybe fill this with different lizard species? More or less for flair only.
                       },
        'Loxodon': {'str': 0, 'dex': 0, 'con': 2, 'int': 0, 'wis': 1, 'cha': 0,
                    'traits': {'Powerful Build', 'Loxodon Bravery', 'Natural Armor', "Mason's Proficiency"
                                                                                     'Stonecunning', 'Keen Smell'
                               },
                    'actions': {},
                    'languages': {'Common'},
                    'subraces': {}
                    },
        'Minotaur': {'str': 2, 'dex': 0, 'con': 1, 'int': 0, 'wis': 0, 'cha': 0,
                     'traits': {'Menacing', 'Hybrid Nature'},
                     'actions': {'Horns', 'Goring Rush', 'Hammering Horns'},
                     'languages': {'Common', 'Minotaur'},
                     'subraces': {}
                     },
        'Orc': {'str': 2, 'dex': 0, 'con': 1, 'int': -1, 'wis': 0, 'cha': 0,
                'traits': {'Darkvision', 'Menacing', 'Powerful Build'},
                'actions': {'Aggressive'},
                'languages': {'Common', 'Orc'},
                'subraces': {}
                },
        'Shifter': {'str': 0, 'dex': 1, 'con': 0, 'int': 0, 'wis': 0, 'cha': 0,
                    'traits': {'Darkvision', 'Keen Senses'},
                    'actions': {'Shifting'},
                    'languages': {'Common'},
                    'subraces': {
                        'Beasthide': {
                            'modifiers': {'str': 0, 'dex': 0, 'con': 2, 'int': 0, 'wis': 0, 'cha': 0},
                            'features': ['Tough' 'Shifting Feature (Beasthide)'],
                            'languages': []
                        },
                        'Longtooth': {
                            'modifiers': {'str': 2, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0, 'cha': 0},
                            'features': ['Fierce', 'Shifting Feature (Longtooth)'],
                            'languages': [],
                        },
                        'Swiftstride': {
                            'modifiers': {'str': 0, 'dex': 1, 'con': 0, 'int': 0, 'wis': 0, 'cha': 1},
                            'features': ['Graceful', 'Swift Stride', 'Shifting Feature (Swiftstride)'],
                            'languages': []
                        },
                        'Wildhunt': {
                            'modifiers': {'str': 0, 'dex': 0, 'con': 0, 'int': 0, 'wis': 2, 'cha': 0},
                            'features': ['Natural Tracker', 'Mark the Scent', 'Shifting Feature (Wildhunt)'],
                            'languages': []
                        }
                    }
                    },
        'Simic Hybrid': {'str': 0, 'dex': 0, 'con': 2, 'int': 0, 'wis': 0, 'cha': 0,
                         'traits': {'Darkvision'},
                         'actions': {},
                         'languages': {'Common', 'Elvish'},
                         'subraces': {}
                         },
        'Tabaxi': {'str': 0, 'dex': 2, 'con': 0, 'int': 0, 'wis': 0, 'cha': 1,
                   'traits': {'Darkvision', "Cat's Talent", "Cat's Claws"},
                   'actions': {'Feline Agility'},
                   'languages': {'Common', 'Choice'},
                   'subraces': {}
                   },
        'Tiefling': {'str': 0, 'dex': 2, 'con': 0, 'int': 1, 'wis': 0, 'cha': 0,
                     'traits': {'Darkvision', 'Hellish Resistance', 'Infernal Legacy'},
                     'actions': {},
                     'languages': {'Common', 'Infernal'},
                     'subraces': {
                         'Abyssal': {
                             'modifiers': {'str': 0, 'dex': -2, 'con': 1, 'int': -1, 'wis': 0, 'cha': 2},
                             'features': ['Abyssal Fortitude', 'Abyssal Arcana'],
                             'languages': ['Abyssal']
                         },
                         'Baalzebul': {
                             'modifiers': {'str': 0, 'dex': -2, 'con': 0, 'int': 0, 'wis': 0, 'cha': 2},
                             'features': ['Legacy of Maladomini'],
                             'languages': []
                         },
                         'Dispater': {
                             'modifiers': {'str': 0, 'dex': -1, 'con': 0, 'int': -1, 'wis': 0, 'cha': 2},
                             'features': ['Legacy of Dis'],
                             'languages': []
                         },
                         'Fierna': {
                             'modifiers': {'str': 0, 'dex': -2, 'con': 0, 'int': -1, 'wis': 1, 'cha': 2},
                             'features': ['Legacy of Phlegethos'],
                             'languages': []
                         },
                         'Glasaya': {
                             'modifiers': {'str': 0, 'dex': -1, 'con': 0, 'int': -1, 'wis': 0, 'cha': 2},
                             'features': ['Legacy of Malbolge'],
                             'languages': []
                         },
                         'Levistus': {
                             'modifiers': {'str': 0, 'dex': -2, 'con': 1, 'int': -1, 'wis': 0, 'cha': 2},
                             'features': ['Legacy of Stygia'],
                             'languages': []
                         },
                         'Mammon': {
                             'modifiers': {'str': 0, 'dex': -2, 'con': 0, 'int': 0, 'wis': 0, 'cha': 2},
                             'features': ['Legacy of Minauros'],
                             'languages': []
                         },
                         'Mephistopheles': {
                             'modifiers': {'str': 0, 'dex': -2, 'con': 0, 'int': 0, 'wis': 0, 'cha': 2},
                             'features': ['Legacy of Cania'],
                             'languages': []
                         },
                         'Feral': {
                             'modifiers': {'str': 0, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0, 'cha': 0},
                             'features': [random.choice(feralTraits)],
                             'languages': []
                         },
                         'Zariel': {
                             'modifiers': {'str': 1, 'dex': -2, 'con': 0, 'int': -1, 'wis': 0, 'cha': 2},
                             'features': ['Legacy of Avernus'],
                             'languages': []
                         }
                     }
                     },
        'Tortle': {'str': 2, 'dex': 0, 'con': 0, 'int': 0, 'wis': 1, 'cha': 0,
                   'traits': {'Natural Armor', 'Survival Instinct'},
                   'actions': {'Hold Breath', 'Shell Defense', 'Claws'},
                   'languages': {'Common', 'Aquan'},
                   'subraces': {
                       'Razorback': {
                           'modifiers': {'str': 1, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0, 'cha': 0},
                           'features': ['Razorback', 'Razor Fist'],
                           'languages': []
                       },
                       'Softshell': {
                           'modifiers': {'str': 0, 'dex': 0, 'con': 0, 'int': 0, 'wis': 1, 'cha': 0},
                           'features': ['Softshell', 'Tortle Agility'],
                           'languages': []
                       },
                       'Desert': {
                           'modifiers': {'str': 0, 'dex': 0, 'con': 1, 'int': 0, 'wis': 0, 'cha': 0},
                           'features': ['Nomad', 'Shell Master'],
                           'languages': []
                       }
                   }
                   },
        'Triton': {'str': 1, 'dex': 0, 'con': 1, 'int': 0, 'wis': 0, 'cha': 1,
                   'traits': {'Amphibious', 'Emissary of the Sea', 'Guardian of the Depths'},
                   'actions': {'Control Air and Water'},
                   'languages': {'Common', 'Primordial'},
                   'subraces': {}
                   },
        'Vedalken': {'str': 0, 'dex': 0, 'con': 0, 'int': 2, 'wis': 1, 'cha': 0,
                     'traits': {'Veldaken Dispassion', 'Tireless Precision'},
                     'actions': {},
                     'languages': {'Common'},
                     'subraces': {}
                     },
        'Viashino': {'str': 1, 'dex': 2, 'con': 0, 'int': 0, 'wis': 0, 'cha': 0,
                     'traits': {'Wiry Frame'},
                     'actions': {'Bite', 'Lashing Tail'},
                     'languages': {'Common', 'Draconic'},
                     'subraces': {}
                     },
        'Warforged': {'str': 0, 'dex': 0, 'con': 1, 'int': 0, 'wis': 0, 'cha': 0,
                      'traits': {'Warforged Resilience', "Sentry's Rest", 'Integrated Protection'},
                      'actions': {},
                      'languages': {'Common'},
                      'subraces': {
                          'Envoy': {
                              'modifiers': {'str': 0, 'dex': 2, 'con': 0, 'int': 0, 'wis': 0, 'cha': 0},
                              'features': ['Specialized Design', 'Integrated Tool'],
                              'languages': []
                          },
                          'Juggernaut': {
                              'modifiers': {'str': 2, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0, 'cha': 0},
                              'features': ['Iron Fists', 'Powerful Build'],
                              'languages': []
                          },
                          'Skirmisher': {
                              'modifiers': {'str': 0, 'dex': 2, 'con': 0, 'int': 0, 'wis': 0, 'cha': 0},
                              'features': ['Swift', 'Light Step'],
                              'languages': []
                          }
                      }
                      },
        'Yuan-ti Pureblood': {'str': 0, 'dex': 0, 'con': 0, 'int': 1, 'wis': 0, 'cha': 2,
                              'traits': {'Darkvision', 'Innate Spellcasting', 'Magic Resistance', 'Poison Immunity'},
                              'actions': {},
                              'languages': {'Common', 'Abyssal', 'Draconic'},
                              'subraces': {}
                              }
    }  # A dictionary of races, with their racial bonuses, traits, actions, and languages.
    classes = {
        'Barbarian': {'primary': 'str', 'secondary': 'con',
                      'traits': {'Rage', 'Unarmored Defense'}
                      },
        'Bard': {'primary': 'cha', 'secondary': 'dex',
                 'traits': {'Spellcasting', 'Bardic Inspiration' 'Cantrips (2)', 'Spells (4) (1st Level)'}
                 },
        'Cleric': {'primary': 'wis', 'secondary': 'str',
                   'traits': {'Spellcasting', 'Divine Domain', 'Cantrips (3)', 'Spells (2) (1st Level'}
                   },
        'Druid': {'primary': 'wis', 'secondary': 'con',
                  'traits': {'Druidic', 'Spellcasting', 'Cantrips (2)', 'Spells (2) (1st Level)'}
                  },
        'Fighter': {'primary': 'str', 'secondary': 'con',
                    'traits': {'Fighting Style', 'Second Wind'}
                    },
        'Monk': {'primary': 'dex', 'secondary': 'wis',
                 'traits': {'Unarmored Defense', 'Martial Arts'}
                 },
        'Paladin': {'primary': 'str', 'secondary': 'cha',
                    'traits': {'Divine Sense', 'Lay on Hands'}
                    },
        'Ranger': {'primary': 'dex', 'secondary': 'wis',
                   'traits': {'Favored Enemy', 'Natural Explorer'}
                   },
        'Rogue': {'primary': 'dex', 'secondary': 'wis',
                  'traits': {'Expertise', 'Sneak Attack', "Thieve's Cant"}
                  },
        'Sorcerer': {'primary': 'cha', 'secondary': 'con',
                     'traits': {'Spellcasting', 'Sorcerous Origin', 'Cantrips (4)', 'Spells (2) (1st Level)'}
                     },
        'Warlock': {'primary': 'cha', 'secondary': 'con',
                    'traits': {'Otherworldly Patron', 'Pact Magic', 'Cantrips (2)', 'Spells (2) (1st Level)'}
                    },
        'Wizard': {'primary': 'int', 'secondary': 'con',
                   'traits': {'Spellcasting', 'Arcane Recovery', 'Cantrips (3)'}
                   },
        'Bloodhunter': {'primary': 'str', 'secondary': 'dex',
                         'traits': {"Hunter's Bane", 'Crimson Rite'}
                         },
    }  # A dictionary of classes, with their "preferred" stats.

    statList = [] #Declaring a list to add stat rolls to.

    for x in range(6): #Do this 6 times, for each ability score available.
        statList.append(rollStats())
    statList.sort(reverse = True) #Sort it in reverse so that the greatest values are first.

    stats = ['str', 'dex', 'con', 'int', 'wis', 'cha']  # A list of each stat possible
    stats.remove(classes[charClass]['primary'])  # Remove the first and second from the list so that
    stats.remove(classes[charClass]['secondary'])  # We can randomize the "unpreferred" stats
    random.shuffle(stats)  # Randomize the leftover stats.

    prefStats = []  # creating a list with the preferred stats at the beginning
    prefStats.append(classes[charClass]['primary'])
    prefStats.append(classes[charClass]['secondary'])
    for x in range(4):  # Add the rest of the stats to the preferred list. Order does not matter here.
        prefStats.append(stats[x])

    # Thanks to Matt for this code
    statMatch = {}
    for x in range(6):
        statMatch.update({prefStats[x]: statList[x]})  # Updating a dictionary with the corresponding index values.

    charStr = statMatch['str']
    charDex = statMatch['dex']
    charCon = statMatch['con']
    charInt = statMatch['int']
    charWis = statMatch['wis']
    charCha = statMatch['cha']

    if charRace == 'Changeling':
        choice = random.randint(1, 2)
        if choice == 1:
            charDex += 1
        else:
            charInt += 1
    elif charRace == 'Half-Elf':
        for x in range(2):  # There are two points to assign, so the loop iterates twice
            choice = random.randint(1, 5)  # Randomly assigns an ability to increment
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

    ########################################################
    #  Below, we pick a subrace of the race, if applicable #
    ########################################################

    subRaces = races[charRace]['subraces'] #Choose a subrace

    if len(subRaces) != 0: #Check to see if subraces actually exist for this race.
        charSub = random.choice(list(subRaces))
    else:
        charSub = None #If the race has no subraces, there is no subrace applied (duh).

    #############################
    #Subrace selection ends here#
    #############################

    ##################################################################
    # These add the base features from the race, subrace not included#
    ##################################################################

    charFeatures = []
    for x in races[charRace]['traits']:
        charFeatures.append(x)

    for x in races[charRace]['actions']:
        charFeatures.append(x)

    charLanguages = []

    for x in races[charRace]['languages']:
        charLanguages.append(x)

    if charSub != None:
        rtnSub = '**Subrace: **' + str(charSub) + '\n'
    else:
        rtnSub = ''

    ################################################################
    # From here down, the subrace modifiers are added, if applicable#
    ################################################################
    print(charSub)
    if charSub != None:
        for x in races[charRace]['subraces'][charSub]['features']:
            charFeatures.append(x)
        for x in races[charRace]['subraces'][charSub]['languages']:
            charLanguages.append(x)

        charStr += races[charRace]['subraces'][charSub]['modifiers']['str']
        charDex += races[charRace]['subraces'][charSub]['modifiers']['dex']
        charCon += races[charRace]['subraces'][charSub]['modifiers']['con']
        charInt += races[charRace]['subraces'][charSub]['modifiers']['int']
        charWis += races[charRace]['subraces'][charSub]['modifiers']['wis']
        charCha += races[charRace]['subraces'][charSub]['modifiers']['cha']

    for x in classes[charClass]['traits']:
        charFeatures.append(x)

    #######################################################################
    # Subrace modifiers end here. Ability score bonus modifiers begin here.#
    #######################################################################

    ##############################
    # Bonus Modifiers begin here.#
    ##############################
    strBonus = (charStr - 10) // 2
    if strBonus >= 0:
        strBonus = '+' + str(strBonus)
    dexBonus = (charDex - 10) // 2
    if dexBonus >= 0:
        dexBonus = '+' + str(dexBonus)
    conBonus = (charCon - 10) // 2
    if conBonus >= 0:
        conBonus = '+' + str(conBonus)
    intBonus = (charInt - 10) // 2
    if intBonus >= 0:
        intBonus = '+' + str(intBonus)
    wisBonus = (charWis - 10) // 2
    if wisBonus >= 0:
        wisBonus = '+' + str(wisBonus)
    chaBonus = (charCha - 10) // 2
    if chaBonus >= 0:
        chaBonus = '+' + str(chaBonus)

    ############################
    # Bonus modifiers end here.#
    ############################

    ########################################################################
    # Converting the features and languages from arrays into strings below.#
    ########################################################################

    charFeatures.sort()
    charLanguages.sort()

    charFeatStr = ''
    charLangStr = ''

    for x in charFeatures:
        charFeatStr += x
        charFeatStr += ', '
    if charFeatStr.endswith(', '):
        charFeatStr = charFeatStr[:-2]

    for y in charLanguages:
        charLangStr += y
        charLangStr += ', '
    if charLangStr.endswith(', '):
        charLangStr = charLangStr[:-2]

    ##########################################
    # Feature and language tidying ends here.#
    ##########################################

    ##########################
    # Alignments logic below #
    ##########################

    charAlignment = str  # Create a string to append later

    moralList = ['Lawful', 'Neutral', 'Chaotic']
    alignList = ['Good', 'Neutral', 'Evil']

    charMoral = random.choice(moralList)
    charAlign = random.choice(alignList)

    if charMoral == charAlign:
        charAlignment = 'True Neutral'
    else:
        charAlignment = charMoral + " " + charAlign

    ##############################
    # Alignments logic ends here.#
    ##############################

    ##############################################################################################
    # The following code gives the character a gender, which is simply for extra character flair.#
    ##############################################################################################

    charGender = random.choice(['Male', 'Female'])

    #######################################################
    # The following code gives the character an age range #
    #######################################################

    charAge = random.choice(['Adolescent', 'Young Adult', 'Adult', 'Elderly'])

    #####################################################################################
    # Organize and return all of the character information in a Discord-friendly format.#
    #####################################################################################


    rtn = '**Race: **' + str(charRace) + '\n' + \
          rtnSub + \
          '**Class: **' + str(charClass) + '\n' + \
          '**Alignment: **' + charAlignment + '\n\n' \
          '**Strength: **' + str(charStr) + '   (' + str(strBonus) + ')''\n' + \
          '**Dexterity: **' + str(charDex) + '   (' + str(dexBonus) + ')''\n' + \
          '**Constitution: **' + str(charCon) + '   (' + str(conBonus) + ')''\n' + \
          '**Intelligence: **' + str(charInt) + '   (' + str(intBonus) + ')''\n' + \
          '**Wisdom: **' + str(charWis) + '   (' + str(wisBonus) + ')''\n' + \
          '**Charisma: **' + str(charCha) + '   (' + str(chaBonus) + ')''\n' + \
          '**Features and Traits: **' + str(charFeatStr) + '\n' + \
          '**Languages: **' + str(charLangStr)+'\n' + \
          '***---------------------------------------------***'+'\n'+\
          '*The following properties are for flair only*'+'\n'+\
          '***---------------------------------------------***'+'\n'+\
          '**Gender: **' + str(charGender)+ '\n'+\
          '**Age Range **'+ str(charAge) + '\n'
    return rtn

