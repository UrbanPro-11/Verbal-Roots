import random

print("""Hello!
Use this to work on SSAT synonyms and the verbal section.
You should memorize these roots as they will most likely
appear on the SSAT.""")

# List of roots
roots = [
    "aqua", "aud", "bene", "bio", "chrono", "corp", "cred", "dict", "geo", "graph",
    "junct", "log/logy", "lumin", "man/manu", "mater/matr", "mort", "multi", "omni", 
    "pater/patr", "port", "rupt", "scrib/script", "sect", "spec", "struct", "terra", 
    "therm", "ven/vent", "vid/vis", "viv/vit", "voc/voke", "bene", "mal", "philo", 
    "phobia", "phon", "photo", "polis/polit", "psych", "scope", "tele", "zo", "ante", 
    "anti", "auto", "bene", "circum", "contra", "de", "dis", "equi", "ex", "hyper", 
    "hypo", "inter", "intra", "macro", "micro", "mono", "multi", "poly", "post", 
    "pre", "pro", "retro", "sub", "super", "trans", "uni", "ambi/amphi", "arch", 
    "cede/ceed/cess", "fid", "fin", "flu", "form", "gen", "grad/gress", "jur/jus", 
    "leg", "liber", "luc", "medi", "migr", "miss/mit", "mov/mot/mobil", "onym", "ped", 
    "pel/puls", "pend", "phil", "plac", "pon/pos", "poten", "prim", "rect", "sequ", 
    "sol", "ten/tain/tin", "vac"
]

# List of definitions
definitions = [
    ["water"], ["hear"], ["good"], ["life"], ["time"], ["body"], ["believe"], ["say"], ["earth"], ["write"],
    ["join"], ["word", "study"], ["light"], ["hand"], ["mother"], ["death"], ["many"], ["all"], 
    ["father"], ["carry"], ["break"], ["write"], ["cut"], ["see", "look"], ["build"], ["earth"], 
    ["heat"], ["come"], ["see"], ["life"], ["call"], ["good"], ["bad"], ["love"], ["fear"], ["sound"], 
    ["light"], ["city"], ["mind"], ["see"], ["far"], ["animal"], ["before"], ["against"], ["self"], 
    ["good"], ["around"], ["against"], ["down", "away"], ["apart", "away"], ["equal"], ["out", "out of", "from"], 
    ["over"], ["under"], ["between"], ["within"], ["large"], ["small"], ["one"], ["many"], ["many"], 
    ["after"], ["before"], ["forward"], ["backward"], ["under"], ["above"], ["across"], ["one"], 
    ["both"], ["chief", "ruler"], ["go", "yield"], ["trust", "faith"], ["end"], ["flow"], ["shape"], 
    ["birth", "race"], ["step"], ["law"], ["law"], ["free"], ["light"], ["middle"], ["move"], ["send"], 
    ["move"], ["name"], ["foot"], ["drive", "push"], ["hang"], ["love"], ["please"], ["place", "put"], 
    ["power"], ["first"], ["straight", "right"], ["follow"], ["alone", "sun"], ["hold"], ["empty"]
]

# Setting up some stuff
practice = 'yes'

wordsToPractice = []
definitionsToRemember = []

correct = 0
incorrect = 0

# Function for working out the guess
def attempt(trys, rootWord, definitionWord, mode):
    global wordsToPractice, definitionsToRemember, correct, incorrect
    if trys.lower() in definitionWord:
        print('Correct!')
        correct += 1
        if mode == False:
            incorrect -= 1
            index = wordsToPractice.index(rootWord)  # Get the index of rootWord
            wordsToPractice.pop(index)
            definitionsToRemember.pop(index)

    else:
        print(f'Incorrect. The answer was {definitionWord}')
        if mode == True:
            incorrect += 1
            wordsToPractice.append(rootWord)
            definitionsToRemember.append(definitionWord)

# Main while loop
while practice.lower() in ['yes', 'y']:

    try: total = int(input('Enter how many roots you would like to practice: '))
    except ValueError:
        print('It will default to 10.')
        total = 10
    
    for _ in range(total):
        x = random.randint(0, 99)
        root = roots[x]
        definition = definitions[x]

        guess = input(f'Enter the definition for {root}: ')
        attempt(guess, root, definition, mode=True)
    
    practice = input('Would you like to continue practicing? ')
    if practice.lower() in ['yes', 'y']:  
        review = input('Would you like to practice your incorrect words? ')

        if review.lower() in ['yes', 'y']:
            z = len(wordsToPractice)

            for word in range(z - 1, -1, -1):
                guess = input(f'Enter the definition for {wordsToPractice[word]}: ')
                attempt(guess, wordsToPractice[word], definitionsToRemember[word], mode=False)

        else: continue

    else:
        print(f'You got {correct} out of {correct + incorrect}.')
        if len(wordsToPractice) > 1: print(f'You need to practice the roots {wordsToPractice}.')
        print('Bye!')
        break
