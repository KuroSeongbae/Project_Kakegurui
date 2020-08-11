class PlayerClass():

    def __init__(self, name):
        self.SetPlayerName(name)
        self._playerCards = []
        self._looses = 0

    def SetPlayerName(self, playerName):
        self._playerName = playerName

    def GetPlayerName(self):
        return self._playerName

    def GetPlayerCards(self) :
        return self._playerCards

    def SetPlayerCards(self, playerCards):
        if len(playerCards) == 0:
            self._playerCards = []
        else:
            self._playerCards = playerCards

    def SetPlayerLooses(self):
        self._looses += 1

    def GetPlayerLooses(self):
        return self._looses