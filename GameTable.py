class GameTable():

    def __init__(self):
        self._tableCards = []
        self._tableSum = 0

    def SetTableCards(self, addedCard):
        self._tableCards.append(addedCard)

    def GetTableCards(self):
        return self._tableCards

    def SetTableSum(self, value):
        self._tableSum += value

    def GetTableSum(self):
        return self._tableSum