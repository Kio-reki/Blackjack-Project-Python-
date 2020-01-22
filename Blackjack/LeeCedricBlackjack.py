#Blackjack refactor
from graphics import *
import random as ran

win = GraphWin("Blackjack", 1300, 700)

# SECTION Buttons
def drawButtonDeal():
    dealBtnBase = Circle(Point(1050, 200), 50)
    dealBtnBase.setFill("black")
    dealBtnBase.setOutline("dark green")
    dealBtnBase.setWidth(8)

    dealBtnIconA = Oval(Point(1025, 200), Point(1075, 200))
    dealBtnIconB = Oval(Point(1050, 175), Point(1050, 225))
    dealBtnIconA.setOutline("dark green")
    dealBtnIconB.setOutline("dark green")
    dealBtnIconA.setWidth(4)
    dealBtnIconB.setWidth(4)

    dealBtnBase.draw(win)
    dealBtnIconA.draw(win)
    dealBtnIconB.draw(win)

def drawButtonHold():
    holdBtnBase = Circle(Point(1200, 200), 50)
    holdBtnBase.setFill("black")
    holdBtnBase.setOutline("dark red")
    holdBtnBase.setWidth(8)

    holdBtnIcon = Rectangle(Point(1175, 175), Point(1225, 225))
    holdBtnIcon.setFill("dark red")

    holdBtnBase.draw(win)
    holdBtnIcon.draw(win)

def drawButtonExit():

    exitBtnBase = Rectangle(Point(800, 600), Point(900, 650))
    exitBtnBase.setFill("white")
    exitBtnBase.setOutline("dark red")
    exitBtnBase.setWidth(8)

    textExit = Text(Point(850, 625), "Exit")
    textExit.setTextColor("black")
    textExit.setSize(20)

    exitBtnBase.draw(win)
    textExit.draw(win)

def drawButtonConfirmBet():

    confirmBtnBase = Rectangle(Point(1175 ,330), Point(1275, 350))
    confirmBtnBase.setFill("green")
    confirmBtnBase.setOutline("dark red")
    confirmBtnBase.setWidth(1)

    textConfirm = Text(Point(1225, 340), "Confirm")
    textConfirm.setTextColor("white")
    textConfirm.setSize(10)

    confirmBtnBase.draw(win)
    textConfirm.draw(win)

def Buttons():
    drawButtonDeal()
    drawButtonHold()
    drawButtonConfirmBet()
    drawButtonExit()
# !SECTION Buttons

# SECTION UI
def drawGameText():

    textTitle = Text(Point(1125, 50), "Blackjack")
    textTitle.setFace("courier")
    textTitle.setSize(35)
    textTitle.setTextColor("white")

    textBet = Text(Point(1050, 340), "Bet")
    textBet.setSize(20)
    textBet.setTextColor("white")

    textCurrentRoundBet = Text(Point(1050, 440), "Current Bet")
    textCurrentRoundBet.setSize(20)
    textCurrentRoundBet.setTextColor("white")

    textCash = Text(Point(1125, 520), "Cash")
    textCash.setSize(20)
    textCash.setTextColor("white")

    textPlayerScore = Text(Point(170,430), "Your Score:")
    textPlayerScore.setSize(28)
    textPlayerScore.setTextColor("white")

    textDealerScore = Text(Point(180,270), "Dealer Score:")
    textDealerScore.setSize(28)
    textDealerScore.setTextColor("white")

    textPlayerScore.draw(win)
    textDealerScore.draw(win)
    textTitle.draw(win)
    textCash.draw(win)
    textBet.draw(win)
    textCurrentRoundBet.draw(win)


def drawGameTable():

    playerWindow = Rectangle(Point(950,0), Point(1300, 700))
    playerWindow.setFill(color_rgb(24,24,24))
    playerWindow.setOutline(color_rgb(75,14,14))
    playerWindow.setWidth(10)

    playerWindowDivider = Line(Point(950, 125), Point(1300, 125))
    playerWindowDivider.setFill(color_rgb(75,14,14))
    playerWindowDivider.setWidth(8)

    otherDivider = playerWindowDivider.clone()
    otherDivider.move(0, 150)

    playSpace = Rectangle(Point(0,0), Point(950, 700))
    playSpace.setFill(color_rgb(0,95,8))

    playSpace.draw(win)
    playerWindow.draw(win)
    playerWindowDivider.draw(win)
    otherDivider.draw(win)
# !SECTION UI

# Full UI function
def gameUI():
    drawGameTable()
    drawGameText()
    Buttons()

# SECTION Card Dealing
def dealCard(intCenterX, side, strValue):
    if side.lower() == "player":
        intYPointCard = 460
        intYPointText = 475
    elif side.lower() == "dealer":
        intYPointCard = 40
        intYPointText = 55

    cardBase = Rectangle(Point(intCenterX + 75, intYPointCard), Point(intCenterX - 75, intYPointCard + 200))
    cardBase.setFill("white")

    cardText = Text(Point(intCenterX - 62, intYPointText), strValue)
    cardText.setSize(20)
    cardText2 = cardText.clone()
    cardText2.move(124, 170)

    cardBase.draw(win)
    cardText.draw(win)
    cardText2.draw(win)

def dealersHiddenCard(intCenterX):
    cardBase = Rectangle(Point(intCenterX + 65, 45), Point(intCenterX - 65, 235))
    cardBase.setFill("dark blue")
    cardBase.setOutline("white")
    cardBase.setWidth(8)

    cardBase.draw(win)
# !SECTION Card Dealing

# SECTION Drawing Card values
def drawPlayerScore(intTotal):

    rectCover = Rectangle(Point(270,380), Point(320,455))
    rectCover.setOutline(color_rgb(0,95,8))
    rectCover.setFill(color_rgb(0,95,8))
    
    textDiceTotal = Text(Point(300, 430), intTotal)
    textDiceTotal.setSize(28)
    textDiceTotal.setTextColor("white")

    rectCover.draw(win)
    textDiceTotal.draw(win)

def drawDealerScore(intTotal):
    
    rectCover = Rectangle(Point(300, 250), Point(340, 290))
    rectCover.setOutline(color_rgb(0,95,8))
    rectCover.setFill(color_rgb(0,95,8))
    
    textDiceTotal = Text(Point(320, 270), intTotal)
    textDiceTotal.setSize(28)
    textDiceTotal.setTextColor("white")

    rectCover.draw(win)
    textDiceTotal.draw(win)
# !SECTION Drawing Card values

# SECTION  Drawing Money
def drawPlayerCash(intAmount):
    rectCover = Rectangle(Point(1000,530), Point(1250,600))
    rectCover.setFill(color_rgb(24,24,24))

    textCashAmount = Text(Point(1125, 570), "$" + str(intAmount))
    textCashAmount.setFill("green")
    textCashAmount.setSize(20)

    rectCover.draw(win)
    textCashAmount.draw(win)

def drawCurrentBet(intBet):
    #1050, 440
    rectCover = Rectangle(Point(1150,400), Point(1250,480))
    rectCover.setFill("black")

    textBetAmount = Text(Point(1200, 440), "$" + str(intBet))
    textBetAmount.setFill("green")
    textBetAmount.setSize(15)

    textBetAmount.draw(win)
# !SECTION Drawing Money


def preRoundBet(intCash):
    intCash = intCash
    try:
        boolBetConfirmed = False

        while not boolBetConfirmed:
            rectOverlay = Rectangle(Point(225,200), Point(875, 500))
            rectOverlay.setFill("black")
            rectOverlay.setOutline(color_rgb(75,14,14))
            rectOverlay.setWidth(10)
            
            alertMessage = Text(Point(550, 350), "Please enter bet amount in the box\n and click 'Confirm")
            alertMessage.setTextColor("white")
            alertMessage.setSize(30)

            arrow = Line(Point(300,450), Point(800, 450))
            arrow.setArrow("last")
            arrow.setOutline("white")
            arrow.setWidth(4)

            rectOverlay.draw(win)
            alertMessage.draw(win)
            arrow.draw(win)

            entrBet = Entry(Point(1150, 340), 4)
            entrBet.draw(win)

            fltClickPoint = win.getMouse()
            fltClickPointX = fltClickPoint.getX()
            fltClickPointY = fltClickPoint.getY()

            if fltClickPointX >= 1175 and fltClickPointX <= 1275 and fltClickPointY >= 330 and fltClickPointY <= 350:
                strBetEntry = entrBet.getText()
                if strBetEntry != "":
                    fltBetAmount = float(strBetEntry)
                    if fltBetAmount > intCash:
                        pass
                    elif fltBetAmount <= intCash:

                        intBetAmount = int(fltBetAmount // 1)
                        drawCurrentBet(intBetAmount)
                        
                        rectOverlay.undraw()
                        alertMessage.undraw()
                        arrow.undraw()

                        boolBetConfirmed = True
                        return intBetAmount

            elif fltClickPointX >= 800 and fltClickPointX <= 900 and fltClickPointY >= 600 and fltClickPointY <= 650:
                win.close()
                break
                quit()
            
            rectOverlay.undraw()
            alertMessage.undraw()
            arrow.undraw()
    except:
        rectOverlay.undraw()
        alertMessage.undraw()
        arrow.undraw()
        preRoundBet(intCash)

# SECTION End Round Message and bet conversion
def endGame(intScoreDealer, intScorePlayer):

    def endMessage(strResult): 
        textMessage = Text(Point(600, 350), strResult)
        textMessage.setTextColor("white")
        textMessage.setSize(30)

        textMessage.draw(win)

    if intScorePlayer > 21:
        strResult = "Player Busts!\n\nDealer Wins!"
        endMessage(strResult)
        return "dealer"
    elif intScoreDealer == intScorePlayer:
        strResult = "Card value match\n\nDraw Game"
        endMessage(strResult)
        return "draw"
    elif intScoreDealer < intScorePlayer:
        strResult = "Player cards beat Dealer's\n\nPlayer Wins!"
        endMessage(strResult)
        return "player"
    elif intScoreDealer > 21:
        strResult = "Dealer Busts!\n\nPlayer Wins!"
        endMessage(strResult)
        return "player"
    elif intScoreDealer > intScorePlayer:
        strResult = "Dealer's cards beat Player's\n\nDealer Wins!"
        endMessage(strResult)
        return "dealer"

def endRoundWinnings(intBet, side):

    if side == "player":
        return intBet
    elif side == "draw":
        return 0
    elif side == "dealer":
        return -intBet

def drawContinueMsg(condition):
    if condition == "game over":
        strMessage = "Insufficient funds to continue. Game Over"
    else:
        strMessage = "Click anywhere to continue to the next round"
    msgOverlay = Rectangle(Point(100, 590), Point(900, 690))
    msgOverlay.setFill("black")
    msgOverlay.setOutline("red")
    msgOverlay.setWidth(10)

    textMsg = Text(Point(500, 640), strMessage)
    textMsg.setFill("white")
    textMsg.setSize(15)

    msgOverlay.draw(win)
    textMsg.draw(win)

    win.getMouse()

    msgOverlay.undraw()
    textMsg.undraw()
# !SECTION End Round Message and bet conversion


# SECTION BlackJack 
def gameStart(intStartingAmount):
    intCash = intStartingAmount
    gameUI()
    drawPlayerCash(intCash)

    intBet = preRoundBet(intCash)

    intCenterX = 150
    intCardsDealt = 0

    lstPlayerHand = []
    lstDealerHand = []

    for i in range(2):
        lstPlayerHand.append(ran.randint(1,10))
        lstDealerHand.append(ran.randint(1,10))

    dealersHiddenCard(intCenterX)
    dealCard(intCenterX + 80, "dealer", lstDealerHand[1])
    drawDealerScore(lstDealerHand[1])

    for card in lstPlayerHand:
        dealCard(intCenterX, "player", card)
        drawPlayerScore(sum(lstPlayerHand))
        intCenterX += 80
        intCardsDealt += 1

    dealCard(intCenterX - 80, "dealer", lstDealerHand[1])
    drawDealerScore(lstDealerHand[1])

    while sum(lstPlayerHand) < 21:
        intClickPoint = win.getMouse()
        fltClickPointX = intClickPoint.getX()
        fltClickPointY = intClickPoint.getY()

        if fltClickPointX >= 1005 and fltClickPointX <= 1095 and fltClickPointY >= 155 and fltClickPointY <= 245:

            intRandom = ran.randint(1,13)

            if intRandom >=10:
                intRandom = ran.randint(1,10)
            elif intRandom < 10:
                intRandom = ran.randint(1,9)

            lstPlayerHand.append(intRandom)
            dealCard(intCenterX, "player", intRandom)
            drawPlayerScore(sum(lstPlayerHand))
            intCenterX += 80
            intCardsDealt += 1

        elif fltClickPointX >= 1180 and fltClickPointX <= 1220 and fltClickPointY >= 155 and fltClickPointY <= 245:
            break

        elif fltClickPointX >= 800 and fltClickPointX <= 900 and fltClickPointY >= 600 and fltClickPointY <= 650:
            quit()
    
    intCenterX -= (80 * intCardsDealt)

    if sum(lstPlayerHand) <= 21:

        while sum(lstDealerHand) <= 17:
            intRandom = ran.randint(1,10)
            lstDealerHand.append(intRandom)

        for card in lstDealerHand:
            dealCard(intCenterX, "dealer", card)
            intCenterX += 80
    else:
        
        for card in lstDealerHand:
            dealCard(intCenterX, "dealer", card)
            intCenterX += 80

    drawDealerScore(sum(lstDealerHand))

    strWinner = endGame(sum(lstDealerHand), sum(lstPlayerHand))

    intCash += endRoundWinnings(intBet, strWinner)

    drawPlayerCash(intCash)

    if intCash <= 0:
        drawContinueMsg("game over")
        quit()
    else:
        drawContinueMsg("")
        gameStart(intCash)
# !SECTION Blackjack

gameStart(1000)

# TODO 
# More accurate card drawing chance/formula and restriction to 4 of each card
# Draw Letter/Face Card labels
# Allow and display Aces to have soft values of 1 and 11
# Chip betting rather than numeric input (May need to expand UI)
