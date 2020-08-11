import random
import os

from CardDeck import *
from PlayerClass import *
from GameTable import *

clear = lambda: os.system('cls')

def SelectPlayerNumber():
    playerNumber = 0
    while playerNumber < 3 or playerNumber > 6:
        print("Select number of Players (between 3 and 6)")
        playerNumber = int(input())
        if playerNumber < 3 | playerNumber > 6:
            print("Playernumber must be between 3 and 6!")

    return playerNumber

def FillPlayerList(playerNumber):
    playerList = []
    for i in range(1, playerNumber + 1):
        playerList.append(PlayerClass("Player" + str(i)))
    return playerList

def GetCardHand(pList, gameDeck):
    for player in pList:
        emptyList = []
        cardHand = []
        player.SetPlayerCards(emptyList)

        for x in range(4):
            cardHand.append(gameDeck[len(gameDeck)-1])
            del gameDeck[len(gameDeck)-1]
        
        player.SetPlayerCards(cardHand)
        # evtl noch sortieren
    return pList

def RoundIntroducer(r):
    print("Round: " + str(r))
    print("===========================================")

def ShowCards(p):
    print(p.GetPlayerName() + " cards: ")
    print(str(p.GetPlayerCards()) + '\n')

def GameProcess(player, r, move, t, weiter, pNumber):
    SelectCard(player, t)
    return ShowTable(t, pNumber)

def SelectCard(p, t):
    ShowCards(p)
    print("Select a Card by Index (1 - " + str(len(p.GetPlayerCards())) + ")")
    playCard = -1

    while playCard > len(p.GetPlayerCards()) - 1 or playCard == - 1:
        playCard = int(input())
        playCard = playCard - 1

    t.SetTableCards(p.GetPlayerCards()[playCard])
    del p._playerCards[playCard]

    clear()

def ShowTable(t, pNumber):
    print("Played Cards: ")
    print(t.GetTableCards())

    t.SetTableSum(t.GetTableCards()[len(t.GetTableCards()) - 1])
    print("Table Sum: " + str(t.GetTableSum()) + "/" + str(pNumber * pNumber))

    if t.GetTableSum() > pNumber * pNumber:
        return False
    else:
        return True

def Round(pList, gameDeck, pNumber):
    for r in range(1, 4):
        weiter = True
        move = 0

        table1 = GameTable()
        clear()

        pList = GetCardHand(pList, gameDeck)

        RoundIntroducer(r)

        #bet coins

        while weiter:
            n = len(pList) - 1
            if len(pList[n].GetPlayerCards()) == 0:
                pList = GetCardHand(pList, gameDeck)

            for p in pList:
                weiter = GameProcess(p, r, move, table1, weiter, pNumber)
                if weiter == False:
                    p.SetPlayerLooses()
                    print(p.GetPlayerName() + " lost, next Screen: ")
                    input()
                    break
                move += 1
        
        for p in pList:
            print(p.GetPlayerName() + str(p.GetPlayerLooses()) + " looses | ")


cardDeck = CardDeck()
gameDeck = cardDeck.GetDeck()

playerNumber = SelectPlayerNumber()
playerList = FillPlayerList(playerNumber)

Round(playerList, gameDeck, playerNumber)
