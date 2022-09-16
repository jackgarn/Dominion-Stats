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

    def empty(self):
        self.copper  = 0
        self.silver  = 0
        self.gold  = 0
        self.curse  = 0
        self.estate  = 0
        self.duchy  = 0
        self.province  = 0
        self.artisan  = 0
        self.bandit  = 0
        self.bureaucrat  = 0
        self.cellar  = 0
        self.chapel  = 0
        self.councilroom  = 0
        self.festival  = 0
        self.gardens  = 0
        self.harbinger  = 0
        self.laboratory  = 0
        self.library  = 0
        self.market  = 0
        self.merchant  = 0
        self.militia  = 0
        self.mine  = 0
        self.moat  = 0
        self.moneylender  = 0
        self.poacher  = 0
        self.remodel  = 0
        self.sentry  = 0
        self.smithy  = 0
        self.throneroom  = 0
        self.vassal  = 0
        self.village  = 0
        self.witch  = 0
        self.workshop  = 0

    def gain(self, char):
        if char == 'Copper':
            self.copper += 1
        if char == 'Silver':
            self.silver += 1
        if char == 'Gold':
            self.gold += 1
        if char == 'Curse':
            self.curse += 1
        if char == 'Estate':
            self.estate += 1
        if char == 'Duchy':
            self.duchy += 1
        if char == 'Province':
            self.province += 1
        if char == 'Artisan':
            self.artisan += 1
        if char == 'Bandit':
            self.bandit += 1
        if char == 'Bureaucrat':
            self.bureaucrat += 1
        if char == 'Cellar':
            self.cellar += 1
        if char == 'Chapel':
            self.chapel += 1
        if char == 'Councilroom':
            self.councilroom += 1
        if char == 'Festival':
            self.festival += 1
        if char == 'Gardens':
            self.gardens += 1
        if char == 'Harbinger':
            self.harbinger += 1
        if char == 'Laboratory':
            self.laboratory += 1
        if char == 'Library':
            self.library += 1
        if char == 'Market':
            self.market += 1
        if char == 'Merchant':
            self.merchant += 1
        if char == 'Militia':
            self.militia += 1
        if char == 'Mine':
            self.mine += 1
        if char == 'Moat':
            self.moat += 1
        if char == 'Moneylender':
            self.moneylender += 1
        if char == 'Poacher':
            self.poacher += 1
        if char == 'Remodel':
            self.remodel += 1
        if char == 'Sentry':
            self.sentry += 1
        if char == 'Smithy':
            self.smithy += 1
        if char == 'Throneroom':
            self.throneroom += 1
        if char == 'Vassal':
            self.vassal += 1
        if char == 'Village':
            self.village += 1
        if char == 'Witch':
            self.witch += 1
        if char == 'Workshop':
            self.workshop += 1

    def display(self):
        if self.Copper > 0:
            print(self.copper,' Coppers')
        if self.Silver > 0:
            print(self.silver,' Silvers')
        if self.old > 0:
            print(self.gold,' Golds')
        if self.curse > 0:
            print(self.curse,' Curses')
        if self.estate > 0:
            print(self.estate,' Estates')
        if self.duchy > 0:
            print(self.duchy,' Duchies')
        if self.province > 0:
            print(self.province,' Provinces')
        if self.artisan > 0:
            print(self.artisan,' Artisans')
        if self.bandit > 0:
            print(self.bandit,' Bandits')
        if self.bureaucrat > 0:
            print(self.bureaucrat,' Bureaucrats')
        if self.cellar > 0:
            print(self.cellar,' Cellars')
        if self.chapel > 0:
            print(self.chapel,' Chapels')
        if self.councilroom > 0:
            print(self.councilroom,' Councilrooms')
        if self.festival > 0:
            print(self.festival,' Festivals')
        if self.gardens > 0:
            print(self.gardens,' Gardenss')
        if self.harbinger > 0:
            print(self.harbinger,' Harbingers')
        if self.laboratory > 0:
            print(self.laboratory,' Laboratories')
        if self.library > 0:
            print(self.library,' Libraries')
        if self.market > 0:
            print(self.market,' Markets')
        if self.merchant > 0:
            print(self.merchant,' Merchants')
        if self.militia > 0:
            print(self.militia,' Militias')
        if self.mine > 0:
            print(self.mine,' Mines')
        if self.moat > 0:
            print(self.moat,' Moats')
        if self.moneylender > 0:
            print(self.moneylender,' Moneylenders')
        if self.poacher > 0:
            print(self.poacher,' Poachers')
        if self.remodel > 0:
            print(self.remodel,' Remodels')
        if self.sentry > 0:
            print(self.sentry,' Sentries')
        if self.smithy > 0:
            print(self.smithy,' Smithies')
        if self.throneroom > 0:
            print(self.throneroom,' Thronerooms')
        if self.vassal > 0:
            print(self.vassal,' Vassals')
        if self.village > 0:
            print(self.village,' Villages')
        if self.witch > 0:
            print(self.witch,' Witches')
        if self.workshop > 0:
            print(self.workshop,' Workshops')



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
#makes decks
    deckarr = []
    for player in playerArray:
        deck = Deck
        deckarr.append(deck)

    #sets deck values to zero
    for deck in deckarr:
        deck.empty(deck)

    return deckarr

def UpdateDecks(deckArr,gameArr,playerArr):
    #time to get down to business
    #I think we should just look through the game for gains
    for line in gameArr:#look at each line
        for i in range(len(line)):#check words
            if line[i] == 'gains':#if a player gained something
                #we need to do a bunch of things: check who, check what, check how many
                #should be ez due to sick structure
                for player in playerArr:
                    if player == line[0]:
                        if line[i+1] == 'a' or line[i+1] == 'an':
                            deckArr[player].gain(deckArr[player],line[i+2])
                        else:
                            for num in range(int(line[i+1])):
                                deckArr[player].gain(deckArr[player],line[i+2])

    return deckArr




filename = 'fullgame.txt'
#filename = GetFile()
MakeLegible(filename)

game = MakeGameArray(filename)
players = MakePlayerArray(game)
print('players: ',players)

game = FixGameArray(game,players)
#DisplayGameArray(game)

decks = MakeDecks(game,players)

decks = UpdateDecks(decks,game,players)

for player in decks:
    decks[player].display(decks[player])