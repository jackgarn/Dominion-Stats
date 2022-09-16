cards = ['Copper', 'Silver', 'old', 'curse', 'estate', 'duchy', 'province', 'artisan', 'bandit', 'bureaucrat', 'cellar', 'chapel', 'councilroom', 'festival', 'gardens', 'harbinger', 'laboratory', 'library', 'market', 'merchant', 'militia', 'mine', 'moat', 'moneylender', 'poacher', 'remodel', 'sentry', 'smithy', 'throneroom', 'vassal', 'village', 'witch', 'workshop']

file = open('easier-than-typing.txt', 'w')

for char in cards:
    string = "        if self."+char+" > 0:\n"
    file.write(string)
    string = "            print(self."+char+",' "+char+"s')\n"
    file.write(string)





