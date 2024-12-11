import random
import json

print("""Hello!
Use this to work on SSAT synonyms and the verbal section.
You should memorize these roots as they will most likely
appear on the SSAT.
Good luck!
Credits to UrbanPro11 for creating this :)
""")

# Load data, or get default of nothing
try:
    with open('ssatVerbal.json', 'r') as file:
        loaded = json.load(file)
except FileNotFoundError:
    print("File not found. Initializing default data.")
    loaded = {}

# Retrieving data
wordsToPractice = loaded.get("words", [])
definitionsToRemember = loaded.get("definitions", [])

# Roots and definitions setup
rootsAndDefinitions = {
    'aqua': ['water'], 'aud': ['hear'], 'bene': ['good'], 'bio': ['life'], 'chrono': ['time'],
    'corp': ['body'], 'cred': ['believe'], 'dict': ['say'], 'geo': ['earth'], 'graph': ['write'],
    'junct': ['join'], 'log/logy': ['word', 'study'], 'lumin': ['light'], 'man/manu': ['hand'],
    'mater/matr': ['mother'], 'mort': ['death'], 'multi': ['many'], 'omni': ['all'],
    'pater/patr': ['father'], 'port': ['carry'], 'rupt': ['break'], 'scrib/script': ['write'],
    'sect': ['cut'], 'spec': ['see', 'look'], 'struct': ['build'], 'terra': ['earth'],
    'therm': ['heat'], 'ven/vent': ['come'], 'vid/vis': ['see'], 'viv/vit': ['life'],
    'voc/voke': ['call'], 'mal': ['bad'], 'philo': ['love'], 'phobia': ['fear'],
    'phon': ['sound'], 'photo': ['light'], 'polis/polit': ['city'], 'psych': ['mind'],
    'scope': ['see'], 'tele': ['far'], 'zo': ['animal'], 'ante': ['before'], 'anti': ['against'],
    'auto': ['self'], 'circum': ['around'], 'contra': ['against'], 'de': ['down', 'away'],
    'dis': ['apart', 'away'], 'equi': ['equal'], 'ex': ['out of', 'from'], 'hyper': ['over'],
    'hypo': ['under'], 'inter': ['between'], 'intra': ['within'], 'macro': ['large'],
    'micro': ['small'], 'mono': ['one'], 'poly': ['many'], 'post': ['after'], 'pre': ['before'],
    'pro': ['forward'], 'retro': ['backward'], 'sub': ['under'], 'super': ['above'],
    'trans': ['across'], 'uni': ['one'], 'ambi/amphi': ['both'], 'arch': ['chief', 'ruler'],
    'cede/ceed/cess': ['go', 'yield'], 'fid': ['trust', 'faith'], 'fin': ['end'], 'flu': ['flow'],
    'form': ['shape'], 'gen': ['birth', 'race'], 'grad/gress': ['step'], 'jur/jus': ['law'],
    'leg': ['law'], 'liber': ['free'], 'luc': ['light'], 'medi': ['middle'], 'migr': ['move'],
    'miss/mit': ['send'], 'mov/mot/mobil': ['move'], 'onym': ['name'], 'ped': ['foot'],
    'pel/puls': ['drive', 'push'], 'pend': ['hang'], 'phil': ['love'], 'plac': ['please'],
    'pon/pos': ['place', 'put'], 'poten': ['power'], 'prim': ['first'], 'rect': ['straight'],
    'sequ': ['follow'], 'sol': ['alone'], 'ten/tain/tin': ['hold'], 'vac': ['empty']
}

# Prepare root and definition lists
roots = [root for root in rootsAndDefinitions]
definitions = [definition for definition in rootsAndDefinitions.values()]

# Practice setup
practice = 'yes'
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
            index = wordsToPractice.index(rootWord)
            wordsToPractice.pop(index)
            definitionsToRemember.pop(index)
    else:
        print(f'Incorrect. The answer was {definitionWord}')
        if mode == True:
            incorrect += 1
            wordsToPractice.append(rootWord)
            definitionsToRemember.append(definitionWord)

# Main loop
while practice.lower() in ['yes', 'y']:
    try: 
        total = int(input('Enter how many roots you would like to practice: '))
    except ValueError:
        print('It will default to 10.')
        total = 10

    for _ in range(total):
        x = random.randint(0, len(rootsAndDefinitions)-1)
        root = roots[x]
        definition = definitions[x]

        guess = input(f'Enter the definition for {root}: ')
        attempt(guess, root, definition, mode=True)

    practice = input('Would you like to continue practicing? ')
    if practice.lower() in ['yes', 'y']:
        review = input('Would you like to practice your incorrect words? ')
        if review.lower() in ['yes', 'y']:
            for word in range(len(wordsToPractice)-1, -1, -1):
                guess = input(f'Enter the definition for {wordsToPractice[word]}: ')
                attempt(guess, wordsToPractice[word], definitionsToRemember[word], mode=False)

        else: continue

    else:
        print(f'You got {correct} out of {correct + incorrect}.')
        if len(wordsToPractice) > 1:
            print(f'You need to practice the roots {wordsToPractice}.')
        
        practicePlease = {"words": wordsToPractice, "definitions": definitionsToRemember}
        
        with open('ssatVerbal.json', 'w') as file:
            json.dump(practicePlease, file, indent=4)
        print('Bye!')
        break
