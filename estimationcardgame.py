import itertools, random

deck = list(itertools.product(list(range(2,15))   ,  ['S','H','D','C']))


random.shuffle(deck)

player1 = deck[:13]
player2 = deck[13:26]
player3 = deck[26:39]
player4 = deck[39:]

player1 = [(4, 'C'), (14, 'C'), (8, 'C'), (9, 'C'), (13, 'C'), (3, 'D'), (14, 'D'), (11, 'H'), (4, 'H'), (9, 'H'), (12, 'H'), (10, 'H'), (10, 'S')]
player2 = [(7, 'C'), (6, 'C'), (5, 'C'), (12, 'C'), (11, 'C'), (9, 'D'), (6, 'D), (12, 'D'), (7, 'D'), (13, 'H'), (2, 'H'), (5, 'H'), (6, 'H')]
player3 = [(13, 'D'), (8, 'D'), (2, 'D'), (5, 'D'), (11, 'D'), (10, 'D'), (7, 'H'), (8, 'H'), (3, 'H'), (13, 'S'), (7, 'S'), (5, 'S'), (12, 'S')]
player4 = [(3, 'C'), (10, 'C'), (2, 'C'), (4, 'D'), (14, 'H'), (3, 'S'), (4, 'S'), (6, 'S'), (14, 'S'), (8, 'S'), (2, 'S'), (9, 'S'), (11, 'S')]


def playerchoosecard(requiredsuits, cards):
    random.shuffle(player1)
    random.shuffle(player2)
    random.shuffle(player3)
    random.shuffle(player4)
    canbeplayedthistrick = []
    for card in cards:
             if card[1] == requiredsuits:
                  canbeplayedthistrick.append(card)
    if len(canbeplayedthistrick) != 0:
             cards.remove(canbeplayedthistrick[0])
             return canbeplayedthistrick[0], cards
    else:
             return  cards.pop(), cards




def who_got_that_trick(playedcards,trumpsuit,requiredsuit):
         trumpcardsplayed = []
         listofwiningsuitplayed = []
         for card in playedcards:
            if card[1] == trumpsuit:
                   trumpcardsplayed.append(card)
            elif card[1] == requiredsuit:
                 listofwiningsuitplayed.append(card)
         if len(trumpcardsplayed) !=0:
              
              sortedround = sorted(trumpcardsplayed, key = lambda x: x[0])
              #print("trump suit played: ", trumpcardsplayed )
         else:
              sortedround = sorted(listofwiningsuitplayed, key = lambda x: x[0])
              #print("wining suit  played: ", listofwiningsuitplayed )
         winingcard = sortedround[-1]
         #print("wining card is: ", winingcard)
         return playedcards.index(winingcard)  , winingcard


def doatrick(whowonlasttrick):
     global player1, player2, player3, player4


     if whowonlasttrick == 0:
          firstplayerscard, player1 = playerchoosecard(False, player1)
          thesuit= firstplayerscard[1]
          secondplayedcard, player2 = playerchoosecard(thesuit, player2)
          thirdplayedcard,player3 = playerchoosecard(thesuit, player3)
          forthplayedcard, player4= playerchoosecard(thesuit, player4)

     elif whowonlasttrick == 1:
          secondplayedcard,player2 = playerchoosecard(False, player2)
          thesuit= secondplayedcard[1]
          thirdplayedcard,player3 = playerchoosecard(thesuit, player3)
          forthplayedcard , player4= playerchoosecard(thesuit, player4)
          firstplayerscard , player1= playerchoosecard(thesuit, player1)
     elif whowonlasttrick == 2:
          thirdplayedcard , player3= playerchoosecard(False, player3)
          thesuit= thirdplayedcard[1]
          forthplayedcard,player4 = playerchoosecard(thesuit, player4)
          firstplayerscard ,player1= playerchoosecard(thesuit, player1)
          secondplayedcard,player2 = playerchoosecard(thesuit, player2)
     elif whowonlasttrick == 3:
          forthplayedcard , player4= playerchoosecard(False, player4)
          thesuit= forthplayedcard[1]
          firstplayerscard , player1= playerchoosecard(thesuit, player1)
          secondplayedcard, player2 = playerchoosecard(thesuit, player2)
          thirdplayedcard, player3 = playerchoosecard(thesuit, player3)
     playedcards = [firstplayerscard,secondplayedcard, thirdplayedcard, forthplayedcard]
     return playedcards, thesuit




playersscores= [0,0,0,0]

def gameflow():
     global playersscores
     trumpsuit = deck[0][1]
     #print("trump suit is: ",trumpsuit)
     whowonlasttrick = 0
     
     for i in range(13):
          playedcards, thesuit = doatrick(whowonlasttrick)
          #print("cards played this round: ", playedcards)
          whowonlasttrick, winingcard = who_got_that_trick(playedcards,trumpsuit,thesuit)
          #print("the winner is: ",whowonlasttrick+1 , " using: " , winingcard)
          playersscores[whowonlasttrick] +=1 
     return playersscores




playersscores= [0,0,0,0]

for i in range (100000):

    player1 = deck[:13]
    player2 = deck[13:26]
    player3 = deck[26:39]
    player4 = deck[39:]

    gameflow()

print(playersscores)
