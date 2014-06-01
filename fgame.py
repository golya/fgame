class Game:
    def __init__(self):
        self.players = {}
    def addPlayer(self, Player):
        self.players[Player.getName()] = Player
    def getNumberOfLivingPlayers(self):
        i = 0
        for name, player in self.players.iteritems():
            if player.isAlive():
                i += 1
        return i
    def getPlayerByName(self, Name):
        return self.players[Name]
