import random

class CardDeck():
    
    def GetDeck(self):
        cardsList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
        cardsDeck = []
        for i in range(len(cardsList)-1):
            r = random.randint(0, len(cardsList)-1)
            cardsDeck.append(cardsList[r])
            del cardsList[r]

        return cardsDeck