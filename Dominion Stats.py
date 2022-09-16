from http.client import LineTooLong

#not sure about this yet
class Deck:
    #is there a way to do this without it being a nuisance? I think this will be the worst part of diong it like this
    def __init__(self, copper, silver, gold, curse, estate, duchy, province, artisan, bandit, bureaucrat, cellar, chapel, councilroom, festival, gardens, harbinger, laboratory, library, market, merchant, militia, mine, moat, moneylender, poacher, remodel, sentry, smithy, throneroom, vassal, village, witch, workshop):
        self.copper = copper 
        self.silver = silver
        self.gold = gold 
        self.curse = curse
        self.estate = estate 
        self.duchy = duchy
        self.province = province
        self.artisan = artisan
        self.bandit = bandit
        self.bureaucrat = bureaucrat
        self.cellar = cellar
        self.chapel = chapel
        self.councilroom = councilroom
        self.festival = festival
        self.gardens = gardens
        self.harbinger = harbinger
        self.laboratory = laboratory
        self.library = library
        self.market = market
        self.merchant = merchant
        self.militia = militia
        self.mine = mine
        self.moat = moat
        self.moneylender = moneylender
        self.poacher = poacher
        self.remodel = remodel
        self.sentry = sentry
        self.smithy = smithy 
        self.throneroom = throneroom 
        self.vassal = vassal 
        self.village = village
        self.witch = witch
        self.workshop = workshop

def GetFile():
    return input('Enter file name: ')

def MakeLegible(filename):
#this function takes the god forsaken format that dominion uses (no /n) and makes it humanly readable
#also outputs the inputted text if it has already been reformatted by itself :D epic
    file = open(filename,'r') #open me
    plaintext = file.read() #read me
    file.close() #close me

    #it would probably be good to write these to a new file eventually and name them usefully
    #I'm not there yet
    file = open(filename,'w')#these two lines erase everthing from the file, ready to be rewritten 
    file.close()
    #rewrites the file's text in the desired format
    #words are separated by spaces, lines by \n, makes working with the format easy
    lastChar = ''
    position = 0
    position2 = 0
    charScan = ''
    file = open(filename, 'w')
    for char in plaintext:
        #make newlines not periods
        if (char == '.'):
            file.write('\n')
        #deal with the '. ' at the end of each 'line' of the dominion format
        elif char == ' ':
            if lastChar != '.':
                file.write(char)
        else:
            file.write(char)
        lastChar = char

    file.close()

def MakeGameArray(filename):
#turns the text from the sanitized file into a useful array, removing unneccesary items
    file = open(filename,'r')
    text = file.read()#grab text and declare needed variables and arrays
    lineArray = []
    gameArray = []
    word = ''

    #makes each line into an element of gameArray, and each word in to an element of 
    for char in text:
        if (char != ' ') and (char != '\n'):
            word += char
        elif char == ' ':
            lineArray.append(word)
            word = ''
        elif char == '\n' :
            lineArray.append(word)
            gameArray.append(lineArray)
            lineArray = []
            word = ''

    #removes unneccessary words
    for line in gameArray:
        for word in line:
            if word[:1] == '(' or word[:1] == '-':
                line.remove(word)
            
    file.close()

    return(gameArray)

def MakePlayerArray(gameArray):

    playerArray = []

    for line in gameArray:
        #using the 'starts' element even though it repeats, as other options are less consistent
        if line[1] == 'starts':
            if line[0] not in playerArray:#deals with aforementioned repetitions
                playerArray.append(line[0])

    return playerArray

def FixGameArray(gameArray, playerArray):
#I hate to do things in this order, but the way we want to remove the 'Turn n - player name'
#from the array is far easier to do if we can use the single-element player indicators to
#know what to chop (otherwise identifying what to cut is a nightmare)
    for line in gameArray:
        if line[0] == 'Turn':
            i = 0
            while line[i] not in playerArray:
                i += 1
            del line[0:i]

    return gameArray

def DisplayGameArray(arr):
    for line in arr:
        print(line)

def MakeDecks(gameArray,playerArray):

    deckarr = []
    for player in playerArray:
        deck = Deck
        deckarr.append(deck)

    return deckarr



filename = 'fullgame.txt'
#filename = GetFile()
MakeLegible(filename)

game = MakeGameArray(filename)
players = MakePlayerArray(game)
print('players: ',players)

game = FixGameArray(game,players)
DisplayGameArray(game)

decks = MakeDecks(game,players)

