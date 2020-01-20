#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      stevb6686
#
# Created:     13/01/2017
# Copyright:   (c) stevb6686 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from graphics import *
from random import *
import time
class Button:  #Creating button class

    """A button is a labeled rectangle in a window.
    It is activated or deactivated with the activate()
    and deactivate() methods. The clicked(p) method
    returns true if the button is active and p is inside it."""

    def __init__(self, win, center, width, height, label):
        """ Creates a rectangular button, eg:
        qb = Button(myWin, centerPoint, width, height, 'Quit') """

        w,h = width/2.0, height/2.5
        x,y = center.getX(), center.getY()
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1,p2)
        self.rect.setFill('lightgray')
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.deactivate()

    def clicked(self, p):
        "Returns true if button active and p is inside"
        return (self.active and
                self.xmin <= p.getX() <= self.xmax and
                self.ymin <= p.getY() <= self.ymax)

    def getLabel(self):
        "Returns the label string of this button."
        return self.label.getText()

    def activate(self):
        "Sets this button to 'active'."
        self.label.setFill('black')
        self.rect.setWidth(2)
        self.active = True

    def deactivate(self):
        "Sets this button to 'inactive'."
        self.label.setFill('darkgrey')
        self.rect.setWidth(1)
        self.active = False
    def setColour(self):
        "Sets the colour"


# Main **********************************************************************
# Main **********************************************************************

def main():
    wscore = 0 # resets winning scores on quit
    lscore = 0 # resets losing scores on quit
    while True:
        hskip = False # variable to let it skip the hangman
        run = 0
        win = GraphWin('Hangman',1020,700)
        win.setCoords(0,0,1020,700)
        win.setBackground('lightblue')

    # ********* Title with Box **************************

        hblock = Rectangle(Point(282,575),Point(718,625))
        hblock.setFill("white")
        hblock.draw(win)

        heading = Text(Point(500,600), 'THE HANGMAN GAME')
        heading.setSize(30)
        heading.setTextColor('black')
        heading.draw(win)

    # ********** Categories *******************************

        categoryanimals = Button(win,Point(200, 600),150,125,"Animals")
        animals = ["dog","cat","pig","rhinoceros","giraffe","cow","chicken","hippopotamus","duck","rabbit","octopus","goldfish","eagle","falcon","bat","panda","lizard","seagull","turkey","toad","lion","cheetah","deer","moose","owl","raccoon","flyingsquirrel","snake","shark","hammerhead","dolphin","spermwhale","orangutan","bonobo","chimpanzee"]
        canimals = choice(animals)
        categoryanimals.activate()
        categorycharacters = Button(win,Point(200, 400),150,125,"LoL Characters")
        characters = ["aatrox","annie","ahri","ashe","azir","bard","blitzcrank","brand","caitlyn","camille","cassiopeia","corki","darius","diana","drmundo","draven","ekko","ezreal","fiddlesticks","fiora","gangplank","galio","gangplank","garen","gragas","graves","hecarim","heimerdinger","illaoi","ivern","janna","jarvan","jhin","karthus","kled","leesin","lucian","masteryi","mordekaiser","riven","twitch","vi","udyr","viktor","yasuo","zed","vayne"]
        ccharacters = choice(characters)
        categorycharacters.activate()
        categorymweapons = Button(win,Point(200, 200),150,125,"Medieval Weapons")
        weapons = ["dagger","mace","axe","bowandarrow","lance","broadsword","katana","claymore","falchion","longsword","rapier","shortsword","shuriken","catapult","trebuchet","cannon","mortar","galleon","battleaxe","morningstar","flail","bludgeon","scythe","halberd","glaive","crossbow","spear","ballista","batterningram"]
        cweapons = choice(weapons)
        categorymweapons.activate()
        categorytransport = Button(win,Point(800, 600),150,125,"Transport")
        transport = ["horse","car","airplane","train","subway","babycarriage","bicycle","bus","broomstick","blimp","bomber","canoe","cruise","donkey","dogsled","ferry","freight","helicopter","jet","jetski","kayak","limo","magiccarpet","monorail","moped","motorcycle","motorhome","atv","parachute","rocket","rv","sailboat","scooter","ship","sled","snowmobile","spaceship","suv","tank","taxi","toboggan","tractor","tugboat","unicycle","yacht","zamboni","zeppelin"]
        ctransport = choice(transport)
        categorytransport.activate()
        categorycountries = Button(win,Point(800, 400),150,125,"Countries")
        countries = ["canada","unitedstates","mexico","england","brazil","china","japan","germany","unitedkingdom","france","india","italy","korea","russia","australia","spain","indonesia","netherlands","turkey","switzerland","saudiarabia","argentina","switzerland","taiwan","sweden","belgium","poland","nigeria","iran","thailand","austria","norway","egypt","venezuela","israel","philippines","ireland","malaysia","denmark","singapore","pakistan","southafrica","colombia","finland","chile","bangladesh","portugal","vietnam","greece","czechrepublic","romania","peru","newzealand","algeria","qatar"]
        ccountries = choice(countries)
        categorycountries.activate()
        quitButton = Button(win,Point(800,200),150,125,"Quit")
        quitButton.rect.setFill('firebrick')
        quitButton.activate()
        helpButton = Button(win,Point(500,200),150,125,"Help")
        helpButton.rect.setFill("lightgreen")
        helpButton.activate()
        word = "filler"

        while True:

            pt= win.getMouse()
            if quitButton.clicked(pt):
                win.close()
                exit()

            if categoryanimals.clicked(pt): #If run == 1, hangman will run, also assigns the random word to variable word
                word = canimals
                run = 1
                break
            if categorycharacters.clicked(pt):
                word = ccharacters
                run = 1
                break
            if categorymweapons.clicked(pt):
                word = cweapons
                run = 1
                break
            if categorytransport.clicked(pt):
                word = ctransport
                run = 1
                break
            if categorycountries.clicked(pt):
                word = ccountries
                run = 1
                break

        # *************Help window****************

            if helpButton.clicked(pt):
                helpButton.deactivate()
                quitButton.deactivate()
                categoryanimals.deactivate()
                categorycharacters.deactivate()
                categorymweapons.deactivate()
                categorytransport.deactivate()
                categorycountries.deactivate()

                win.close()
                win = GraphWin('Hangman',1020,700)
                win.setCoords(0,0,1020,700)
                win.setBackground('lightblue')
                hblock = Rectangle(Point(350,575),Point(650,625))
                hblock.setFill("white")
                hblock.draw(win)
                tblock = Rectangle(Point(130,565),Point(870,265))
                tblock.setFill("white")
                tblock.draw(win)
                helptitle = Text(Point(500,600),"How To Play")
                helptitle.setSize(30)
                helptitle.setTextColor("black")
                helptitle.draw(win)

                helpText1 = Text(Point(500,550),"To start, click a category of words on the main menu.")
                helpText2 = Text(Point(500,520),"The word you will be guessing will be of that theme.")
                helpText3 = Text(Point(500,490),"Click on the keyboard buttons to guess letters.")
                helpText4 = Text(Point(500,460),"You only have 6 wrong guesses until you're hanged!")
                helpText5 = Text(Point(500,430),"You can use the help button once to uncover a letter.")
                helpText6 = Text(Point(500,400),"You can keep playing from the ending screen or quit.")
                helpText7 = Text(Point(500,370),"To go back to playing now, click back.")
                helpText8 = Text(Point(500,340),"To exit now, click exit.")
                helpText9 = Text(Point(500,310),"<=== Easy          (Difficulty Levels)          Harder ===>")
                helpText10 = Text(Point(500,280),"Transport <Animals <Characters <Countries <Medieval Weapons")

                helpText1.setFace("courier")
                helpText2.setFace("courier")
                helpText3.setFace("courier")
                helpText4.setFace("courier")
                helpText5.setFace("courier")
                helpText6.setFace("courier")
                helpText7.setFace("courier")
                helpText8.setFace("courier")
                helpText9.setFace("courier")
                helpText10.setFace("courier")

                helpText1.setSize(15)
                helpText2.setSize(15)
                helpText3.setSize(15)
                helpText4.setSize(15)
                helpText5.setSize(15)
                helpText6.setSize(15)
                helpText7.setSize(15)
                helpText8.setSize(15)
                helpText9.setSize(15)
                helpText10.setSize(15)

                helpText1.draw(win)
                helpText2.draw(win)
                helpText3.draw(win)
                helpText4.draw(win)
                helpText5.draw(win)
                helpText6.draw(win)
                helpText7.draw(win)
                helpText8.draw(win)
                helpText9.draw(win)
                helpText10.draw(win)

                backButton = Button(win,Point(200,200),150,125,"Back")
                backButton.rect.setFill("lightgreen")
                backButton.activate()
                quitButton = Button(win,Point(800,200),150,125,"Quit")
                quitButton.rect.setFill('firebrick')
                quitButton.activate()

                while not backButton.clicked(pt):
                    pt = win.getMouse()
                    if quitButton.clicked(pt):
                        win.close()
                        exit()
                    if backButton.clicked(pt):
                        win.close()
                break

    # *******Setting variables************

        num = 0
        for ch in word:
            num=num + 1 #sets the number length to num
            pos1 = 0
            pos2 = 0
            pos3 = 0
            pos4 = 0
            pos5 = 0
            pos6 = 0
            pos7 = 0
            pos8 = 0
            pos9 = 0
            pos10 = 0
            pos11 = 0
            pos12 = 0
            pos13 = 0
            pos14 = 0


    # ********Setting word Length*************

        if num > 0:  #Checks the word length to set a position
            pos1 = word[0] #Assigns positions to each letter
        if num > 1:
            pos2 = word[1]
        if num > 2:
          pos3 = word[2]
        if num > 3:
            pos4 = word[3]
        if num > 4:
            pos5 = word[4]
        if num > 5:
            pos6 = word[5]
        if num > 6:
            pos7 = word[6]
        if num > 7:
            pos8 = word[7]
        if num > 8:
            pos9 = word[8]
        if num > 9:
            pos10 = word[9]
        if num > 10:
            pos11 = word[10]
        if num > 11:
            pos12 = word[11]
        if num > 12:
            pos13 = word[12]
        if num > 13:
            pos14 = word[13]


        # ********** Hangman Window **************************

        if run == 1:
            win.close()
            win = GraphWin("Hangman",1020,700)
            win.setCoords(0,0,1020,700)
            win.setBackground("lightblue")

        # ********** Letter Buttons ***************************

            quitButton = Button(win,Point(900,635),100,75,'Quit')
            quitButton.rect.setFill("firebrick")
            quitButton.activate()
            aButton = Button(win, Point(70,165), 75, 75,'A')
            aButton.activate()
            bButton = Button(win, Point(170,165), 75, 75,'B')
            bButton.activate()
            cButton = Button(win, Point(270,165), 75, 75,'C')
            cButton.activate()
            dButton = Button(win, Point(370,165), 75, 75,'D')
            dButton.activate()
            eButton = Button(win, Point(470,165), 75, 75,'E')
            eButton.activate()
            fButton = Button(win, Point(570,165), 75, 75,'F')
            fButton.activate()
            gButton = Button(win, Point(670,165), 75, 75,'G')
            gButton.activate()
            hButton = Button(win, Point(770,165), 75, 75,'H')
            hButton.activate()
            iButton = Button(win, Point(870,165), 75, 75,'I')
            iButton.activate()
            jButton = Button(win, Point(970,165), 75, 75,'J')
            jButton.activate()
        # second row of letters
            kButton = Button(win, Point(70,100), 75, 75,'K')
            kButton.activate()
            lButton = Button(win, Point(170,100), 75, 75,'L')
            lButton.activate()
            mButton = Button(win, Point(270,100), 75, 75,'M')
            mButton.activate()
            nButton = Button(win, Point(370,100), 75, 75,'N')
            nButton.activate()
            oButton = Button(win, Point(470,100), 75, 75,'O')
            oButton.activate()
            pButton = Button(win, Point(570,100), 75, 75,'P')
            pButton.activate()
            qButton = Button(win, Point(670,100), 75, 75,'Q')
            qButton.activate()
            rButton = Button(win, Point(770,100), 75, 75,'R')
            rButton.activate()
            sButton = Button(win, Point(870,100), 75, 75,'S')
            sButton.activate()
            tButton = Button(win, Point(970,100), 75, 75,'T')
            tButton.activate()
        # third row of letters
            uButton = Button(win, Point(70,35), 75, 75,'U')
            uButton.activate()
            vButton = Button(win, Point(170,35), 75, 75,'V')
            vButton.activate()
            wButton = Button(win, Point(270,35), 75, 75,'W')
            wButton.activate()
            xButton = Button(win, Point(370,35), 75, 75,'X')
            xButton.activate()
            yButton = Button(win, Point(470,35), 75, 75,'Y')
            yButton.activate()
            zButton = Button(win, Point(570,35), 75, 75,'Z')
            zButton.activate()
            hintButton = Button(win, Point(970,35), 75, 75, "Hint")
            hintButton.rect.setFill("steelblue")
            hintButton.activate()

        # *********** Hangman Platform *************

            platform = Rectangle(Point(50,250),Point(400,300))
            platform.setFill("brown")
            platform.draw(win)
            standingleg = Line(Point(380,300),Point(380,650))
            standingleg.draw(win)
            topleg = Line(Point(380,650),Point(200,650))
            topleg.draw(win)
            noose = Line(Point(200,650),Point(200,615))
            noose.draw(win)

        # ******** Drawing Word *********

            hints = 0
            guess = 6  #Guesses allowed
            won = 0  #Letters correctly guessed
            letterpos = 0  #Position of letter in word
            lpointx = 410 #Coordinates of the letter
            lpointy = 495

            for ch in word:
                lpointx = lpointx + 75   #Move point over to draw next letter
                letter1 = Text(Point(lpointx,lpointy), word[letterpos])   #Draw each letter to the coordinate
                underscore = Line(Point(lpointx - 25,lpointy - 21), Point(lpointx + 25,lpointy - 21))  #Draw underscore
                letter1.setSize(18)
                letter1.setFace("courier")
                letter1.draw(win)
                letterpos = letterpos + 1  #Move to next letter
                underscore.draw(win)
                if lpointx> 900:     #When the letters reach the end of the screen, return to origianl x coordinate except with a lower y coordinate, to create a second line
                    lpointx = 410
                    lpointy = lpointy - 75

        # *******Letter Covers************

            rect1 = Rectangle(Point(460, 475), Point(510, 525))
            rect1.setFill("lightblue")
            rect1.setOutline("lightblue")

            rect2 = Rectangle(Point(535, 475), Point(585,525))
            rect2.setFill("lightblue")
            rect2.setOutline("lightblue")

            rect3 = Rectangle(Point(610, 475), Point(660,525))
            rect3.setFill("lightblue")
            rect3.setOutline("lightblue")

            rect4 = Rectangle(Point(685, 475), Point(735,525))
            rect4.setFill("lightblue")
            rect4.setOutline("lightblue")

            rect5 = Rectangle(Point(760, 475), Point(810,525))
            rect5.setFill("lightblue")
            rect5.setOutline("lightblue")

            rect6 = Rectangle(Point(835, 475), Point(885,525))
            rect6.setFill("lightblue")
            rect6.setOutline("lightblue")

            rect7 = Rectangle(Point(910, 475), Point(960,525))
            rect7.setFill("lightblue")
            rect7.setOutline("lightblue")

        # *********Second Row************

            rect8 = Rectangle(Point(460, 400), Point(510, 450))
            rect8.setFill("lightblue")
            rect8.setOutline("lightblue")

            rect9 = Rectangle(Point(535, 400), Point(585, 450))
            rect9.setFill("lightblue")
            rect9.setOutline("lightblue")

            rect10 = Rectangle(Point(610, 400), Point(660, 450))
            rect10.setFill("lightblue")
            rect10.setOutline("lightblue")

            rect11 = Rectangle(Point(685, 400), Point(735, 450))
            rect11.setFill("lightblue")
            rect11.setOutline("lightblue")

            rect12 = Rectangle(Point(760, 400), Point(810, 450))
            rect12.setFill("lightblue")
            rect12.setOutline("lightblue")

            rect13 = Rectangle(Point(835, 400), Point(885, 450))
            rect13.setFill("lightblue")
            rect13.setOutline("lightblue")

            rect14 = Rectangle(Point(910, 400), Point(960, 450))
            rect14.setFill("lightblue")
            rect14.setOutline("lightblue")

        # ************Draw them all***************************

            rect1.draw(win)
            rect2.draw(win)
            rect3.draw(win)
            rect4.draw(win)
            rect5.draw(win)
            rect6.draw(win)
            rect7.draw(win)
            rect8.draw(win)
            rect9.draw(win)
            rect10.draw(win)
            rect11.draw(win)
            rect12.draw(win)
            rect13.draw(win)
            rect14.draw(win)

        # ************Bar with guesses left*******************

            textGuess = Text(Point(550,600),"Guesses Left:")
            textGuess.setSize(20)
            textGuess.draw(win)
            guess1 = Rectangle(Point(645,580),Point(655,620))
            guess1.setFill("brown")
            guess1.draw(win)
            guess2 = Rectangle(Point(660,580),Point(670,620))
            guess2.setFill("brown")
            guess2.draw(win)
            guess3 = Rectangle(Point(675,580),Point(685,620))
            guess3.setFill("brown")
            guess3.draw(win)
            guess4 = Rectangle(Point(690,580),Point(700,620))
            guess4.setFill("brown")
            guess4.draw(win)
            guess5 = Rectangle(Point(705,580),Point(715,620))
            guess5.setFill("brown")
            guess5.draw(win)
            guess6 = Rectangle(Point(720,580),Point(730,620))
            guess6.setFill("brown")
            guess6.draw(win)

         # ********Event loop***********

            while guess > 0 and won != len(word) and hskip == False: #If guesses run out, or the word is guessed, or the loop is skipped with back button, the while loop will be terminated
                if guess == 5:
                    center = Point(200,585) #Remove one from guess bar on wrong guess, draw parts of the hangman
                    head = Circle(center,30)
                    head.setFill("black")
                    head.draw(win)
                    guess6.undraw()
                if guess == 4:
                    body = Line(Point(200,555),Point(200,450))
                    body.draw(win)
                    guess5.undraw()
                if guess == 3:
                    leftleg = Line(Point(200,450),Point(160,350))
                    leftleg.draw(win)
                    guess4.undraw()
                if guess == 2:
                    rightleg = Line(Point(200,450),Point(240,350))
                    rightleg.draw(win)
                    guess3.undraw()
                if guess == 1:
                    leftarm = Line(Point(200,540),Point(160,500))
                    leftarm.draw(win)
                    guess2.undraw()
                pt = win.getMouse()
                if quitButton.clicked(pt):
                    win.close()
                    exit()
                lhint = 0  #Resets hint so that buttons cannot add to win count on consecutive clicks

            # ****************** Hint Button ***************

                if hintButton.clicked(pt) and hints != 1:
                    rletter = randint(1,num)  #Find a random position within the length of the word
                    if rletter == 1: #Assign lhint to the letter
                        lhint = pos1
                    if rletter == 2:
                        lhint = pos2
                    if rletter == 3:
                        lhint = pos3
                    if rletter == 4:
                        lhint = pos4
                    if rletter == 5:
                        lhint = pos5
                    if rletter == 6:
                        lhint = pos6
                    if rletter == 7:
                        lhint = pos7
                    if rletter == 8:
                        lhint = pos8
                    if rletter == 9:
                        lhint = pos9
                    if rletter == 10:
                        lhint = pos10
                    if rletter == 11:
                        lhint = pos11
                    if rletter == 12:
                        lhint = pos12
                    if rletter == 13:
                        lhint = pos13
                    if rletter == 14:
                        lhint = pos14
                    hintButton = Button(win, Point(970,35), 75, 75, "No Hints")  #Deactivate, only one hint
                    hintButton.deactivate()
                    hints = hints + 1

            # ********************* Buttons ********************

                if aButton.clicked(pt) or lhint == "a": #on pressing a, check if each position is equal to a, if so, undraw the box over the position to reveal the letter(s)
                #lhint check allows an "a" button click to be triggered by the hint button
                #This allows the hint button to uncover one type of letter in the word
                #Acts like a normal button press would, with the button being deactivated.

                    aButton.deactivate()
                    if pos1 or pos2 or pos3 or pos4 or pos5 or pos6 or pos7 or pos8 or po9 or pos10 or pos11 or pos12 or pos13 or pos14 == "a":
                        won = won + word.count("a")
                    if pos1 != "a" and pos2 != "a" and pos3 != "a" and pos4 != "a" and pos5 != "a" and pos6 != "a" and pos7 != "a" and pos8 != "a" and pos9 != "a" and pos10 != "a" and pos11 != "a" and pos12 != "a" and pos13 !="a" and pos14 != "a":
                        guess = guess - 1
                    if pos1 == "a":
                        rect1.undraw()
                    if pos2 == "a":
                        rect2.undraw()
                    if pos3 == "a":
                        rect3.undraw()
                    if pos4 == "a":
                        rect4.undraw()
                    if pos5 == "a":
                        rect5.undraw()
                    if pos6 == "a":
                        rect6.undraw()
                    if pos7 == "a":
                        rect7.undraw()
                    if pos8 == "a":
                        rect8.undraw()
                    if pos9 == "a":
                        rect9.undraw()
                    if pos10 == "a":
                        rect10.undraw()
                    if pos11 == "a":
                        rect11.undraw()
                    if pos12 == "a":
                        rect12.undraw()
                    if pos13 == "a":
                        rect13.undraw()
                    if pos14 == "a":
                        rect14.undraw()
                if bButton.clicked(pt) or lhint == "b":
                    bButton.deactivate()
                    if pos1 or pos2 or pos3 or pos4 or pos5 or pos6 or pos7 or pos8 or pos9 or pos10 or pos11 or pos12 or pos13 or pos14 == "b":
                        won = won + word.count("b")
                    if pos1 != "b" and pos2 != "b" and pos3 != "b" and pos4 != "b" and pos5 != "b" and pos6 != "b" and pos7 != "b" and pos8 != "b" and pos9 != "b" and pos10 != "b" and pos11 != "b" and pos12 != "b" and pos13 != "b" and pos14 != "b":
                        guess = guess - 1
                    if pos1 == "b":
                        rect1.undraw()
                    if pos2 == "b":
                        rect2.undraw()
                    if pos3 == "b":
                        rect3.undraw()
                    if pos4 == "b":
                        rect4.undraw()
                    if pos5 == "b":
                        rect5.undraw()
                    if pos6 == "b":
                        rect6.undraw()
                    if pos7 == "b":
                        rect7.undraw()
                    if pos8 == "b":
                        rect8.undraw()
                    if pos9 == "b":
                        rect9.undraw()
                    if pos10 == "b":
                        rect10.undraw()
                    if pos11 == "b":
                        rect11.undraw()
                    if pos12 == "b":
                        rect12.undraw()
                    if pos13 == "b":
                        rect13.undraw()
                    if pos14 == "b":
                        rect14.undraw()
                if cButton.clicked(pt) or lhint == "c":
                    cButton.deactivate()
                    if pos1 or pos2 or pos3 or pos4 or pos5 or pos6 or pos7 or pos8 or pos9 or pos10 or pos11 or pos12 or pos13 or pos14 == "c":
                        won = won + word.count("c")
                    if pos1 != "c" and pos2 != "c" and pos3 != "c" and pos4 != "c" and pos5 != "c" and pos6 != "c" and pos7 != "c" and pos8 != "c" and pos9 != "c" and pos10 != "c" and pos11 != "c" and pos12 != "c" and pos13 != "c" and pos14 != "c":
                        guess = guess - 1
                    if pos1 == "c":
                        rect1.undraw()
                    if pos2 == "c":
                        rect2.undraw()
                    if pos3 == "c":
                        rect3.undraw()
                    if pos4 == "c":
                        rect4.undraw()
                    if pos5 == "c":
                        rect5.undraw()
                    if pos6 == "c":
                        rect6.undraw()
                    if pos7 == "c":
                        rect7.undraw()
                    if pos8 == "c":
                        rect8.undraw()
                    if pos9 == "c":
                        rect9.undraw()
                    if pos10 == "c":
                        rect10.undraw()
                    if pos11 == "c":
                        rect11.undraw()
                    if pos12 == "c":
                        rect12.undraw()
                    if pos13 == "c":
                        rect13.undraw()
                    if pos14 == "c":
                        rect14.undraw()
                if dButton.clicked(pt) or lhint == "d":
                    dButton.deactivate()
                    if pos1 or pos2 or pos3 or pos4 or pos5 or pos6 or pos7 or pos8 or pos9 or pos10 or pos11 or pos12 or pos13 or pos14 == "d":
                        won = won + word.count("d")
                    if pos1 != "d" and pos2 != "d" and pos3 != "d" and pos4 != "d" and pos5 != "d" and pos6 != "d" and pos7 != "d" and pos8 != "d" and pos9 != "d" and pos10 != "d" and pos11 != "d" and pos12 != "d" and pos13 != "d" and pos14 != "d":
                        guess = guess - 1
                    if pos1 ==  "d":
                        rect1.undraw()
                    if pos2 == "d":
                        rect2.undraw()
                    if pos3 == "d":
                        rect3.undraw()
                    if pos4 == "d":
                        rect4.undraw()
                    if pos5 == "d":
                        rect5.undraw()
                    if pos6 == "d":
                        rect6.undraw()
                    if pos7 == "d":
                        rect7.undraw()
                    if pos8 == "d":
                        rect8.undraw()
                    if pos9 == "d":
                        rect9.undraw()
                    if pos10 == "d":
                        rect10.undraw()
                    if pos11 == "d":
                        rect11.undraw()
                    if pos12 == "d":
                        rect12.undraw()
                    if pos13 == "d":
                        rect13.undraw()
                    if pos14 == "d":
                        rect14.undraw()
                if eButton.clicked(pt) or lhint == "e":
                    eButton.deactivate()
                    if pos1 or pos2 or pos3 or pos4 or pos5 or pos6 or pos7 or pos8 or pos9 or pos10 or pos11 or pos12 or pos13 or pos14 == "e":
                        won = won + word.count("e")
                    if pos1 != "e" and pos2 != "e" and pos3 != "e" and pos4 != "e" and pos5 != "e" and pos6 != "e" and pos7 != "e" and pos8 != "e" and pos9 != "e" and pos10 != "e" and pos11 != "e" and pos12 != "e" and pos13 != "e" and pos14 != "e":
                        guess = guess - 1
                    if pos1 == "e":
                        rect1.undraw()
                    if pos2 == "e":
                        rect2.undraw()
                    if pos3 == "e":
                        rect3.undraw()
                    if pos4 == "e":
                        rect4.undraw()
                    if pos5 == "e":
                        rect5.undraw()
                    if pos6 == "e":
                        rect6.undraw()
                    if pos7 == "e":
                        rect7.undraw()
                    if pos8 == "e":
                        rect8.undraw()
                    if pos9 == "e":
                        rect9.undraw()
                    if pos10 == "e":
                        rect10.undraw()
                    if pos11 == "e":
                        rect11.undraw()
                    if pos12 == "e":
                        rect12.undraw()
                    if pos13 == "e":
                        rect13.undraw()
                    if pos14 == "e":
                        rect14.undraw()
                if fButton.clicked(pt) or lhint == "f":
                    fButton.deactivate()
                    if pos1 or pos2 or pos3 or pos4 or pos5 or pos6 or pos7 or pos8 or pos9 or pos10 or pos11 or pos12 or pos13 or pos14 == "f":
                        won = won + word.count("f")
                    if pos1 != "f" and pos2 != "f" and pos3 != "f" and pos4 != "f" and pos5 != "f" and pos6 != "f" and pos7 != "f" and pos8 != "f" and pos9 != "f" and pos10 != "f" and pos11 != "f" and pos12 != "f" and pos13 != "f" and pos14 != "f":
                        guess = guess - 1
                    if pos1 == "f":
                        rect1.undraw()
                    if pos2 == "f":
                        rect2.undraw()
                    if pos3 == "f":
                        rect3.undraw()
                    if pos4 == "f":
                        rect4.undraw()
                    if pos5 == "f":
                        rect5.undraw()
                    if pos6 == "f":
                        rect6.undraw()
                    if pos7 == "f":
                        rect7.undraw()
                    if pos8 == "f":
                        rect8.undraw()
                    if pos9 == "f":
                        rect9.undraw()
                    if pos10 == "f":
                        rect10.undraw()
                    if pos11 == "f":
                        rect11.undraw()
                    if pos12 == "f":
                        rect12.undraw()
                    if pos13 == "f":
                        rect13.undraw()
                    if pos14 == "f":
                        rect14.undraw()
                if gButton.clicked(pt) or lhint == "g":
                    gButton.deactivate()
                    if pos1 or pos2 or pos3 or pos4 or pos5 or pos6 or pos7 or pos8 or pos9 or pos10 or pos11 or pos12 or pos13 or pos14 == "g":
                        won = won + word.count("g")
                    if pos1 != "g" and pos2 != "g" and pos3 != "g" and pos4 != "g" and pos5 != "g" and pos6 != "g" and pos7 != "g" and pos8 != "g" and pos9 != "g" and pos10 != "g" and pos11 != "g" and pos12 != "g" and pos13 != "g" and pos14 != "g":
                        guess = guess - 1
                    if pos1 == "g":
                        rect1.undraw()
                    if pos2 == "g":
                        rect2.undraw()
                    if pos3 == "g":
                        rect3.undraw()
                    if pos4 == "g":
                        rect4.undraw()
                    if pos5 == "g":
                        rect5.undraw()
                    if pos6 == "g":
                        rect6.undraw()
                    if pos7 == "g":
                        rect7.undraw()
                    if pos8 == "g":
                        rect8.undraw()
                    if pos9 == "g":
                        rect9.undraw()
                    if pos10 == "g":
                        rect10.undraw()
                    if pos11 == "g":
                        rect11.undraw()
                    if pos12 == "g":
                        rect12.undraw()
                    if pos13 == "g":
                        rect13.undraw()
                    if pos14 == "g":
                        rect14.undraw()
                if hButton.clicked(pt) or lhint == "h":
                    hButton.deactivate()
                    if pos1 or pos2 or pos3 or pos4 or pos5 or pos6 or pos7 or pos8 or pos9 or pos10 or pos11 or pos12 or pos13 or pos14 == "h":
                        won = won + word.count("h")
                    if pos1 != "h" and pos2 != "h" and pos3 != "h" and pos4 != "h" and pos5 != "h" and pos6 != "h" and pos7 != "h" and pos8 != "h" and pos9 != "h" and pos10 != "h" and pos11 != "h" and pos12 != "h" and pos13 != "h" and pos14 != "h":
                        guess = guess - 1
                    if pos1 == "h":
                        rect1.undraw()
                    if pos2 == "h":
                        rect2.undraw()
                    if pos3 == "h":
                        rect3.undraw()
                    if pos4 == "h":
                        rect4.undraw()
                    if pos5 == "h":
                        rect5.undraw()
                    if pos6 == "h":
                        rect6.undraw()
                    if pos7 == "h":
                        rect7.undraw()
                    if pos8 == "h":
                        rect8.undraw()
                    if pos9 == "h":
                        rect9.undraw()
                    if pos10 == "h":
                        rect10.undraw()
                    if pos11 == "h":
                        rect11.undraw()
                    if pos12 == "h":
                        rect12.undraw()
                    if pos13 == "h":
                        rect13.undraw()
                    if pos14 == "h":
                        rect14.undraw()
                if iButton.clicked(pt) or lhint == "i":
                    iButton.deactivate()
                    if pos1 or pos2 or pos3 or pos4 or pos5 or pos6 or pos7 or pos8 or pos9 or pos10 or pos11 or pos12 or pos13 or pos14 == "i":
                        won = won + word.count("i")
                    if pos1 != "i" and pos2 != "i" and pos3 != "i" and pos4 != "i" and pos5 != "i" and pos6 != "i" and pos7 != "i" and pos8 != "i" and pos9 != "i" and pos10 != "i" and pos11 != "i" and pos12 != "i" and pos13 != "i" and pos14 != "i":
                        guess = guess - 1
                    if pos1 == "i":
                        rect1.undraw()
                    if pos2 == "i":
                        rect2.undraw()
                    if pos3 == "i":
                        rect3.undraw()
                    if pos4 == "i":
                        rect4.undraw()
                    if pos5 == "i":
                        rect5.undraw()
                    if pos6 == "i":
                        rect6.undraw()
                    if pos7 == "i":
                        rect7.undraw()
                    if pos8 == "i":
                        rect8.undraw()
                    if pos9 == "i":
                        rect9.undraw()
                    if pos10 == "i":
                        rect10.undraw()
                    if pos11 == "i":
                        rect11.undraw()
                    if pos12 == "i":
                        rect12.undraw()
                    if pos13 == "i":
                        rect13.undraw()
                    if pos14 == "i":
                        rect14.undraw()
                if jButton.clicked(pt) or lhint == "j":
                    jButton.deactivate()
                    if pos1 or pos2 or pos3 or pos4 or pos5 or pos6 or pos7 or pos8 or pos9 or pos10 or pos11 or pos12 or pos13 or pos14 == "j":
                        won = won + word.count("j")
                    if pos1 != "j" and pos2 != "j" and pos3 != "j" and pos4 != "j" and pos5 != "j" and pos6 != "j" and pos7 != "j" and pos8 != "j" and pos9 != "j" and pos10 != "j" and pos11 != "j" and pos12 != "j" and pos13 != "j" and pos14 != "j":
                        guess = guess - 1
                    if pos1 == "j":
                        rect1.undraw()
                    if pos2 == "j":
                        rect2.undraw()
                    if pos3 == "j":
                        rect3.undraw()
                    if pos4 == "j":
                        rect4.undraw()
                    if pos5 == "j":
                        rect5.undraw()
                    if pos6 == "j":
                        rect6.undraw()
                    if pos7 == "j":
                        rect7.undraw()
                    if pos8 == "j":
                        rect8.undraw()
                    if pos9 == "j":
                        rect9.undraw()
                    if pos10 == "j":
                        rect10.undraw()
                    if pos11 == "j":
                        rect11.undraw()
                    if pos12 == "j":
                        rect12.undraw()
                    if pos13 == "j":
                        rect13.undraw()
                    if pos14 == "j":
                        rect14.undraw()
                if kButton.clicked(pt) or lhint == "k":
                    kButton.deactivate()
                    if pos1 or pos2 or pos3 or pos4 or pos5 or pos6 or pos7 or pos8 or pos9 or pos10 or pos11 or pos12 or pos13 or pos14 == "k":
                        won = won + word.count("k")
                    if pos1 != "k" and pos2 != "k" and pos3 != "k" and pos4 != "k" and pos5 != "k" and pos6 != "k" and pos7 != "k" and pos8 != "k" and pos9 != "k" and pos10 != "k" and pos11 != "k" and pos12 != "k" and pos13 != "k" and pos14 != "k":
                        guess = guess - 1
                    if pos1 == "k":
                        rect1.undraw()
                    if pos2 == "k":
                        rect2.undraw()
                    if pos3 == "k":
                        rect3.undraw()
                    if pos4 == "k":
                        rect4.undraw()
                    if pos5 == "k":
                        rect5.undraw()
                    if pos6 == "k":
                        rect6.undraw()
                    if pos7 == "k":
                        rect7.undraw()
                    if pos8 == "k":
                        rect8.undraw()
                    if pos9 == "k":
                        rect9.undraw()
                    if pos10 == "k":
                        rect10.undraw()
                    if pos11 == "k":
                        rect11.undraw()
                    if pos12 == "k":
                        rect12.undraw()
                    if pos13 == "k":
                        rect13.undraw()
                    if pos14 == "k":
                        rect14.undraw()
                if lButton.clicked(pt) or lhint == "l":
                    lButton.deactivate()
                    if pos1 or pos2 or pos3 or pos4 or pos5 or pos6 or pos7 or pos8 or pos9 or pos10 or pos11 or pos12 or pos13 or pos14 == "l":
                        won = won + word.count("l")
                    if pos1 != "l" and pos2 != "l" and pos3 != "l" and pos4 != "l" and pos5 != "l" and pos6 != "l" and pos7 != "l" and pos8 != "l" and pos9 != "l" and pos10 != "l" and pos11 != "l" and pos12 != "l" and pos13 != "l" and pos14 != "l":
                        guess = guess - 1
                    if pos1 == "l":
                        rect1.undraw()
                    if pos2 == "l":
                        rect2.undraw()
                    if pos3 == "l":
                        rect3.undraw()
                    if pos4 == "l":
                        rect4.undraw()
                    if pos5 == "l":
                        rect5.undraw()
                    if pos6 == "l":
                        rect6.undraw()
                    if pos7 == "l":
                        rect7.undraw()
                    if pos8 == "l":
                        rect8.undraw()
                    if pos9 == "l":
                        rect9.undraw()
                    if pos10 == "l":
                        rect10.undraw()
                    if pos11 == "l":
                        rect11.undraw()
                    if pos12 == "l":
                        rect12.undraw()
                    if pos13 == "l":
                        rect13.undraw()
                    if pos14 == "l":
                        rect14.undraw()
                if mButton.clicked(pt) or lhint == "m":
                    mButton.deactivate()
                    if pos1 or pos2 or pos3 or pos4 or pos5 or pos6 or pos7 or pos8 or pos9 or pos10 or pos11 or pos12 or pos13 or pos14 == "m":
                        won = won + word.count("m")
                    if pos1 != "m" and pos2 != "m" and pos3 != "m" and pos4 != "m" and pos5 != "m" and pos6 != "m" and pos7 != "m" and pos8 != "m" and pos9 != "m" and pos10 != "m" and pos11 != "m" and pos12 != "m" and pos13 != "m" and pos14 != "m":
                        guess = guess - 1
                    if pos1 == "m":
                        rect1.undraw()
                    if pos2 == "m":
                        rect2.undraw()
                    if pos3 == "m":
                        rect3.undraw()
                    if pos4 == "m":
                        rect4.undraw()
                    if pos5 == "m":
                        rect5.undraw()
                    if pos6 == "m":
                        rect6.undraw()
                    if pos7 == "m":
                        rect7.undraw()
                    if pos8 == "m":
                        rect8.undraw()
                    if pos9 == "m":
                        rect9.undraw()
                    if pos10 == "m":
                        rect10.undraw()
                    if pos11 == "m":
                        rect11.undraw()
                    if pos12 == "m":
                        rect12.undraw()
                    if pos13 == "m":
                        rect13.undraw()
                    if pos14 == "m":
                        rect14.undraw()
                if nButton.clicked(pt) or lhint == "n":
                    nButton.deactivate()
                    if pos1 or pos2 or pos3 or pos4 or pos5 or pos6 or pos7 or pos8 or pos9 or pos10 or pos11 or pos12 or pos13 or pos14 == "n":
                        won = won + word.count("n")
                    if pos1 != "n" and pos2 != "n" and pos3 != "n" and pos4 != "n" and pos5 != "n" and pos6 != "n" and pos7 != "n" and pos8 != "n" and pos9 != "n" and pos10 != "n" and pos11 != "n" and pos12 != "n" and pos13 != "n" and pos14 != "n":
                        guess = guess - 1
                    if pos1 == "n":
                        rect1.undraw()
                    if pos2 == "n":
                        rect2.undraw()
                    if pos3 == "n":
                        rect3.undraw()
                    if pos4 == "n":
                        rect4.undraw()
                    if pos5 == "n":
                        rect5.undraw()
                    if pos6 == "n":
                        rect6.undraw()
                    if pos7 == "n":
                        rect7.undraw()
                    if pos8 == "n":
                        rect8.undraw()
                    if pos9 == "n":
                        rect9.undraw()
                    if pos10 == "n":
                        rect10.undraw()
                    if pos11 == "n":
                        rect11.undraw()
                    if pos12 == "n":
                        rect12.undraw()
                    if pos13 == "n":
                        rect13.undraw()
                    if pos14 == "n":
                        rect14.undraw()
                if oButton.clicked(pt) or lhint == "o":
                    oButton.deactivate()
                    if pos1 or pos2 or pos3 or pos4 or pos5 or pos6 or pos7 or pos8 or pos9 or pos10 or pos11 or pos12 or pos13 or pos14 == "o":
                        won = won + word.count("o")
                    if pos1 != "o" and pos2 != "o" and pos3 != "o" and pos4 != "o" and pos5 != "o" and pos6 != "o" and pos7 != "o" and pos8 != "o" and pos9 != "o" and pos10 != "o" and pos11 != "o" and pos12 != "o" and pos13 != "o" and pos14 != "o":
                        guess = guess - 1
                    if pos1 == "o":
                        rect1.undraw()
                    if pos2 == "o":
                        rect2.undraw()
                    if pos3 == "o":
                        rect3.undraw()
                    if pos4 == "o":
                        rect4.undraw()
                    if pos5 == "o":
                        rect5.undraw()
                    if pos6 == "o":
                        rect6.undraw()
                    if pos7 == "o":
                        rect7.undraw()
                    if pos8 == "o":
                        rect8.undraw()
                    if pos9 == "o":
                        rect9.undraw()
                    if pos10 == "o":
                        rect10.undraw()
                    if pos11 == "o":
                        rect11.undraw()
                    if pos12 == "o":
                        rect12.undraw()
                    if pos13 == "o":
                        rect13.undraw()
                    if pos14 == "o":
                        rect14.undraw()
                if pButton.clicked(pt) or lhint == "p":
                    pButton.deactivate()
                    if pos1 or pos2 or pos3 or pos4 or pos5 or pos6 or pos7 or pos8 or pos9 or pos10 or pos11 or pos12 or pos13 or pos14 == "p":
                        won = won + word.count("p")
                    if pos1 != "p" and pos2 != "p" and pos3 != "p" and pos4 != "p" and pos5 != "p" and pos6 != "p" and pos7 != "p" and pos8 != "p" and pos9 != "p" and pos10 != "p" and pos11 != "p" and pos12 != "p" and pos13 != "p" and pos14 != "p":
                        guess = guess - 1
                    if pos1 == "p":
                        rect1.undraw()
                    if pos2 == "p":
                        rect2.undraw()
                    if pos3 == "p":
                        rect3.undraw()
                    if pos4 == "p":
                        rect4.undraw()
                    if pos5 == "p":
                        rect5.undraw()
                    if pos6 == "p":
                        rect6.undraw()
                    if pos7 == "p":
                        rect7.undraw()
                    if pos8 == "p":
                        rect8.undraw()
                    if pos9 == "p":
                        rect9.undraw()
                    if pos10 == "p":
                        rect10.undraw()
                    if pos11 == "p":
                        rect11.undraw()
                    if pos12 == "p":
                        rect12.undraw()
                    if pos13 == "p":
                        rect13.undraw()
                    if pos14 == "p":
                        rect14.undraw()
                if qButton.clicked(pt) or lhint == "q":
                    qButton.deactivate()
                    if pos1 or pos2 or pos3 or pos4 or pos5 or pos6 or pos7 or pos8 or pos9 or pos10 or pos11 or pos12 or pos13 or pos14 == "q":
                        won = won + word.count("q")
                    if pos1 != "q" and pos2 != "q" and pos3 != "q" and pos4 != "q" and pos5 != "q" and pos6 != "q" and pos7 != "q" and pos8 != "q" and pos9 != "q" and pos10 != "q" and pos11 != "q" and pos12 != "q" and pos13 != "q" and pos14 != "q":
                        guess = guess - 1
                    if pos1 == "q":
                        rect1.undraw()
                    if pos2 == "q":
                        rect2.undraw()
                    if pos3 == "q":
                        rect3.undraw()
                    if pos4 == "q":
                        rect4.undraw()
                    if pos5 == "q":
                        rect5.undraw()
                    if pos6 == "q":
                        rect6.undraw()
                    if pos7 == "q":
                        rect7.undraw()
                    if pos8 == "q":
                        rect8.undraw()
                    if pos9 == "q":
                        rect9.undraw()
                    if pos10 == "q":
                        rect10.undraw()
                    if pos11 == "q":
                        rect11.undraw()
                    if pos12 == "q":
                        rect12.undraw()
                    if pos13 == "q":
                        rect13.undraw()
                    if pos14 == "q":
                        rect14.undraw()
                if rButton.clicked(pt) or lhint == "r":
                    rButton.deactivate()
                    if pos1 or pos2 or pos3 or pos4 or pos5 or pos6 or pos7 or pos8 or pos9 or pos10 or pos11 or pos12 or pos13 or pos14 == "r":
                        won = won + word.count("r")
                    if pos1 != "r" and pos2 != "r" and pos3 != "r" and pos4 != "r" and pos5 != "r" and pos6 != "r" and pos7 != "r" and pos8 != "r" and pos9 != "r" and pos10 != "r" and pos11 != "r" and pos12 != "r" and pos13 != "r" and pos14 != "r":
                        guess = guess - 1
                    if pos1 == "r":
                        rect1.undraw()
                    if pos2 == "r":
                        rect2.undraw()
                    if pos3 == "r":
                        rect3.undraw()
                    if pos4 == "r":
                        rect4.undraw()
                    if pos5 == "r":
                        rect5.undraw()
                    if pos6 == "r":
                        rect6.undraw()
                    if pos7 == "r":
                        rect7.undraw()
                    if pos8 == "r":
                        rect8.undraw()
                    if pos9 == "r":
                        rect9.undraw()
                    if pos10 == "r":
                        rect10.undraw()
                    if pos11 == "r":
                        rect11.undraw()
                    if pos12 == "r":
                        rect12.undraw()
                    if pos13 == "r":
                        rect13.undraw()
                    if pos14 == "r":
                        rect14.undraw()
                if sButton.clicked(pt) or lhint == "s":
                    sButton.deactivate()
                    if pos1 or pos2 or pos3 or pos4 or pos5 or pos6 or pos7 or pos8 or pos9 or pos10 or pos11 or pos12 or pos13 or pos14 == "s":
                        won = won + word.count("s")
                    if pos1 != "s" and pos2 != "s" and pos3 != "s" and pos4 != "s" and pos5 != "s" and pos6 != "s" and pos7 != "s" and pos8 != "s" and pos9 != "s" and pos10 != "s" and pos11 != "s" and pos12 != "s" and pos13 != "s" and pos14 != "s":
                        guess = guess - 1
                    if pos1 == "s":
                        rect1.undraw()
                    if pos2 == "s":
                        rect2.undraw()
                    if pos3 == "s":
                        rect3.undraw()
                    if pos4 == "s":
                        rect4.undraw()
                    if pos5 == "s":
                        rect5.undraw()
                    if pos6 == "s":
                        rect6.undraw()
                    if pos7 == "s":
                        rect7.undraw()
                    if pos8 == "s":
                        rect8.undraw()
                    if pos9 == "s":
                        rect9.undraw()
                    if pos10 == "s":
                        rect10.undraw()
                    if pos11 == "s":
                        rect11.undraw()
                    if pos12 == "s":
                        rect12.undraw()
                    if pos13 == "s":
                        rect13.undraw()
                    if pos14 == "s":
                        rect14.undraw()
                if tButton.clicked(pt) or lhint == "t":
                    tButton.deactivate()
                    if pos1 or pos2 or pos3 or pos4 or pos5 or pos6 or pos7 or pos8 or pos9 or pos10 or pos11 or pos12 or pos13 or pos14 == "t":
                        won = won + word.count("t")
                    if pos1 != "t" and pos2 != "t" and pos3 != "t" and pos4 != "t" and pos5 != "t" and pos6 != "t" and pos7 != "t" and pos8 != "t" and pos9 != "t" and pos10 != "t" and pos11 != "t" and pos12 != "t" and pos13 != "t" and pos14 != "t":
                        guess = guess - 1
                    if pos1 == "t":
                        rect1.undraw()
                    if pos2 == "t":
                        rect2.undraw()
                    if pos3 == "t":
                        rect3.undraw()
                    if pos4 == "t":
                        rect4.undraw()
                    if pos5 == "t":
                        rect5.undraw()
                    if pos6 == "t":
                        rect6.undraw()
                    if pos7 == "t":
                        rect7.undraw()
                    if pos8 == "t":
                        rect8.undraw()
                    if pos9 == "t":
                        rect9.undraw()
                    if pos10 == "t":
                        rect10.undraw()
                    if pos11 == "t":
                        rect11.undraw()
                    if pos12 == "t":
                        rect12.undraw()
                    if pos13 == "t":
                        rect13.undraw()
                    if pos14 == "t":
                        rect14.undraw()
                if uButton.clicked(pt) or lhint == "u":
                    uButton.deactivate()
                    if pos1 or pos2 or pos3 or pos4 or pos5 or pos6 or pos7 or pos8 or pos9 or pos10 or pos11 or pos12 or pos13 or pos14 == "u":
                        won = won + word.count("u")
                    if pos1 != "u" and pos2 != "u" and pos3 != "u" and pos4 != "u" and pos5 != "u" and pos6 != "u" and pos7 != "u" and pos8 != "u" and pos9 != "u" and pos10 != "u" and pos11 != "u" and pos12 != "u" and pos13 != "u" and pos14 != "u":
                        guess = guess - 1
                    if pos1 == "u":
                        rect1.undraw()
                    if pos2 == "u":
                        rect2.undraw()
                    if pos3 == "u":
                        rect3.undraw()
                    if pos4 == "u":
                        rect4.undraw()
                    if pos5 == "u":
                        rect5.undraw()
                    if pos6 == "u":
                        rect6.undraw()
                    if pos7 == "u":
                        rect7.undraw()
                    if pos8 == "u":
                        rect8.undraw()
                    if pos9 == "u":
                        rect9.undraw()
                    if pos10 == "u":
                        rect10.undraw()
                    if pos11 == "u":
                        rect11.undraw()
                    if pos12 == "u":
                        rect12.undraw()
                    if pos13 == "u":
                        rect13.undraw()
                    if pos14 == "u":
                        rect14.undraw()
                if vButton.clicked(pt) or lhint == "v":
                    vButton.deactivate()
                    if pos1 or pos2 or pos3 or pos4 or pos5 or pos6 or pos7 or pos8 or pos9 or pos10 or pos11 or pos12 or pos13 or pos14 == "v":
                        won = won + word.count("v")
                    if pos1 != "v" and pos2 != "v" and pos3 != "v" and pos4 != "v" and pos5 != "v" and pos6 != "v" and pos7 != "v" and pos8 != "v" and pos9 != "v" and pos10 != "v" and pos11 != "v" and pos12 != "v" and pos13 != "v" and pos14 != "v":
                        guess = guess - 1
                    if pos1 == "v":
                        rect1.undraw()
                    if pos2 == "v":
                        rect2.undraw()
                    if pos3 == "v":
                        rect3.undraw()
                    if pos4 == "v":
                        rect4.undraw()
                    if pos5 == "v":
                        rect5.undraw()
                    if pos6 == "v":
                        rect6.undraw()
                    if pos7 == "v":
                        rect7.undraw()
                    if pos8 == "v":
                        rect8.undraw()
                    if pos9 == "v":
                        rect9.undraw()
                    if pos10 == "v":
                        rect10.undraw()
                    if pos11 == "v":
                        rect11.undraw()
                    if pos12 == "v":
                        rect12.undraw()
                    if pos13 == "v":
                        rect13.undraw()
                    if pos14 == "v":
                        rect14.undraw()
                if wButton.clicked(pt) or lhint == "w":
                    wButton.deactivate()
                    if pos1 or pos2 or pos3 or pos4 or pos5 or pos6 or pos7 or pos8 or pos9 or pos10 or pos11 or pos12 or pos13 or pos14 == "w":
                        won = won + word.count("w")
                    if pos1 != "w" and pos2 != "w" and pos3 != "w" and pos4 != "w" and pos5 != "w" and pos6 != "w" and pos7 != "w" and pos8 != "w" and pos9 != "w" and pos10 != "w" and pos11 != "w" and pos12 != "w" and pos13 != "w" and pos14 != "w":
                        guess = guess - 1
                    if pos1 == "w":
                        rect1.undraw()
                    if pos2 == "w":
                        rect2.undraw()
                    if pos3 == "w":
                        rect3.undraw()
                    if pos4 == "w":
                        rect4.undraw()
                    if pos5 == "w":
                        rect5.undraw()
                    if pos6 == "w":
                        rect6.undraw()
                    if pos7 == "w":
                        rect7.undraw()
                    if pos8 == "w":
                        rect8.undraw()
                    if pos9 == "w":
                        rect9.undraw()
                    if pos10 == "w":
                        rect10.undraw()
                    if pos11 == "w":
                        rect11.undraw()
                    if pos12 == "w":
                        rect12.undraw()
                    if pos13 == "w":
                        rect13.undraw()
                    if pos14 == "w":
                        rect14.undraw()
                if xButton.clicked(pt) or lhint == "x":
                    xButton.deactivate()
                    if pos1 or pos2 or pos3 or pos4 or pos5 or pos6 or pos7 or pos8 or pos9 or pos10 or pos11 or pos12 or pos13 or pos14 == "x":
                        won = won + word.count("x")
                    if pos1 != "x" and pos2 != "x" and pos3 != "x" and pos4 != "x" and pos5 != "x" and pos6 != "x" and pos7 != "x" and pos8 != "x" and pos9 != "x" and pos10 != "x" and pos11 != "x" and pos12 != "x" and pos13 != "x" and pos14 != "x":
                        guess = guess - 1
                    if pos1 == "x":
                        rect1.undraw()
                    if pos2 == "x":
                        rect2.undraw()
                    if pos3 == "x":
                        rect3.undraw()
                    if pos4 == "x":
                        rect4.undraw()
                    if pos5 == "x":
                        rect5.undraw()
                    if pos6 == "x":
                        rect6.undraw()
                    if pos7 == "x":
                        rect7.undraw()
                    if pos8 == "x":
                        rect8.undraw()
                    if pos9 == "x":
                        rect9.undraw()
                    if pos10 == "x":
                        rect10.undraw()
                    if pos11 == "x":
                        rect11.undraw()
                    if pos12 == "x":
                        rect12.undraw()
                    if pos13 == "x":
                        rect13.undraw()
                    if pos14 == "x":
                        rect14.undraw()
                if yButton.clicked(pt) or lhint == "y":
                    yButton.deactivate()
                    if pos1 or pos2 or pos3 or pos4 or pos5 or pos6 or pos7 or pos8 or pos9 or pos10 or pos11 or pos12 or pos13 or pos14 == "y":
                        won = won + word.count("y")
                    if pos1 != "y" and pos2 != "y" and pos3 != "y" and pos4 != "y" and pos5 != "y" and pos6 != "y" and pos7 != "y" and pos8 != "y" and pos9 != "y" and pos10 != "y" and pos11 != "y" and pos12 != "y" and pos13 != "y" and pos14 != "y":
                        guess = guess - 1
                    if pos1 == "y":
                        rect1.undraw()
                    if pos2 == "y":
                        rect2.undraw()
                    if pos3 == "y":
                        rect3.undraw()
                    if pos4 == "y":
                        rect4.undraw()
                    if pos5 == "y":
                        rect5.undraw()
                    if pos6 == "y":
                        rect6.undraw()
                    if pos7 == "y":
                        rect7.undraw()
                    if pos8 == "y":
                        rect8.undraw()
                    if pos9 == "y":
                        rect9.undraw()
                    if pos10 == "y":
                        rect10.undraw()
                    if pos11 == "y":
                        rect11.undraw()
                    if pos12 == "y":
                        rect12.undraw()
                    if pos13 == "y":
                        rect13.undraw()
                    if pos14 == "y":
                        rect14.undraw()
                if zButton.clicked(pt) or lhint == "z":
                    zButton.deactivate()
                    if pos1 or pos2 or pos3 or pos4 or pos5 or pos6 or pos7 or pos8 or pos9 or pos10 or pos11 or pos12 or pos13 or pos14 == "z":
                        won = won + word.count("z")
                    if pos1 != "z" and pos2 != "z" and pos3 != "z" and pos4 != "z" and pos5 != "z" and pos6 != "z" and pos7 != "z" and pos8 != "z" and pos9 != "z" and pos10 != "z" and pos11 != "z" and pos12 != "z" and pos13 != "z" and pos14 != "z":
                        guess = guess - 1
                    if pos1 == "z":
                        rect1.undraw()
                    if pos2 == "z":
                        rect2.undraw()
                    if pos3 == "z":
                        rect3.undraw()
                    if pos4 == "z":
                        rect4.undraw()
                    if pos5 == "z":
                        rect5.undraw()
                    if pos6 == "z":
                        rect6.undraw()
                    if pos7 == "z":
                        rect7.undraw()
                    if pos8 == "z":
                        rect8.undraw()
                    if pos9 == "z":
                        rect9.undraw()
                    if pos10 == "z":
                        rect10.undraw()
                    if pos11 == "z":
                        rect11.undraw()
                    if pos12 == "z":
                        rect12.undraw()
                    if pos13 == "z":
                        rect13.undraw()
                    if pos14 == "z":
                        rect14.undraw()

        #**************WINNING TEXT*****************************************************************

            if won == len(word):
                wscore = wscore + 1
                ctext = Text(Point(550,300),"Correct!")
                ctext.setSize(30)
                ctext.draw(win)
                time.sleep(2.5)
                win.close()

        #*************WINNING SCREEN**************

                win = GraphWin("Winner!",1020,700)
                win.setCoords(0,0,1020,700)
                win.setBackground("lightblue")
                youwon = Text(Point(500,510),"You win!")
                youwon.setSize(36)
                youwon.draw(win)

         # *************WIN COUNTS AND BAR**************

                wtext = Text(Point(175, 410),"Wins:")
                wtext.setSize(15)
                wtext.draw(win)
                winbox = Rectangle(Point(150, 180),Point(200, 395))
                winbox.setFill("white")
                winbox.draw(win)
                wbar1 = Rectangle(Point(155, 185),Point(195, 195))
                wbar1.setFill("brown")
                wbar2 = Rectangle(Point(155, 200),Point(195, 210))
                wbar2.setFill("brown")
                wbar3 = Rectangle(Point(155, 215),Point(195, 225))
                wbar3.setFill("brown")
                wbar4 = Rectangle(Point(155, 230),Point(195, 240))
                wbar4.setFill("brown")
                wbar5 = Rectangle(Point(155, 245),Point(195, 255))
                wbar5.setFill("brown")
                wbar6 = Rectangle(Point(155, 260),Point(195, 270))
                wbar6.setFill("brown")
                wbar7 = Rectangle(Point(155, 275),Point(195, 285))
                wbar7.setFill("brown")
                wbar8 = Rectangle(Point(155, 290),Point(195, 300))
                wbar8.setFill("brown")
                wbar9 = Rectangle(Point(155, 305),Point(195, 315))
                wbar9.setFill("brown")
                wbar10 = Rectangle(Point(155, 320),Point(195, 330))
                wbar10.setFill("brown")
                wbar11 = Rectangle(Point(155, 335),Point(195, 345))
                wbar11.setFill("brown")
                wbar12 = Rectangle(Point(155, 350),Point(195, 360))
                wbar12.setFill("brown")
                wbar13 = Rectangle(Point(155, 365),Point(195, 375))
                wbar13.setFill("brown")
                wbar14 = Rectangle(Point(155, 380),Point(195, 390))
                wbar14.setFill("brown")
                if wscore == 1:  #Draws a bar that fills up the white box with every win, repeated with losses and on the opposing losing screen
                    wbar1.draw(win),
                if wscore == 2:
                    wbar2.draw(win),wbar1.draw(win)
                if wscore == 3:
                    wbar3.draw(win),wbar1.draw(win),wbar2.draw(win),
                if wscore == 4:
                    wbar4.draw(win),wbar1.draw(win),wbar2.draw(win),wbar3.draw(win),
                if wscore == 5:
                    wbar5.draw(win),wbar1.draw(win),wbar2.draw(win),wbar3.draw(win),wbar4.draw(win),
                if wscore == 6:
                    wbar6.draw(win),wbar1.draw(win),wbar2.draw(win),wbar3.draw(win),wbar4.draw(win),wbar5.draw(win),
                if wscore == 7:
                    wbar7.draw(win),wbar1.draw(win),wbar2.draw(win),wbar3.draw(win),wbar4.draw(win),wbar5.draw(win),wbar6.draw(win),
                if wscore == 8:
                    wbar8.draw(win),wbar1.draw(win),wbar2.draw(win),wbar3.draw(win),wbar4.draw(win),wbar5.draw(win),wbar6.draw(win),wbar7.draw(win),
                if wscore == 9:
                    wbar9.draw(win),wbar1.draw(win),wbar2.draw(win),wbar3.draw(win),wbar4.draw(win),wbar5.draw(win),wbar6.draw(win),wbar7.draw(win),wbar8.draw(win),
                if wscore == 10:
                    wbar10.draw(win),wbar1.draw(win),wbar2.draw(win),wbar3.draw(win),wbar4.draw(win),wbar5.draw(win),wbar6.draw(win),wbar7.draw(win),wbar8.draw(win),wbar9.draw(win),
                if wscore == 11:
                    wbar11.draw(win),wbar1.draw(win),wbar2.draw(win),wbar3.draw(win),wbar4.draw(win),wbar5.draw(win),wbar6.draw(win),wbar7.draw(win),wbar8.draw(win),wbar9.draw(win),wbar10.draw(win),
                if wscore == 12:
                    wbar12.draw(win),wbar1.draw(win),wbar2.draw(win),wbar3.draw(win),wbar4.draw(win),wbar5.draw(win),wbar6.draw(win),wbar7.draw(win),wbar8.draw(win),wbar9.draw(win),wbar10.draw(win),wbar11.draw(win),
                if wscore == 13:
                    wbar13.draw(win),wbar1.draw(win),wbar2.draw(win),wbar3.draw(win),wbar4.draw(win),wbar5.draw(win),wbar6.draw(win),wbar7.draw(win),wbar8.draw(win),wbar9.draw(win),wbar10.draw(win),wbar11.draw(win),wbar12.draw(win),
                if wscore == 14:
                    wbar14.draw(win),wbar1.draw(win),wbar2.draw(win),wbar3.draw(win),wbar4.draw(win),wbar5.draw(win),wbar6.draw(win),wbar7.draw(win),wbar8.draw(win),wbar9.draw(win),wbar10.draw(win),wbar11.draw(win),wbar12.draw(win),wbar13.draw(win)

         # *************LOSS COUNTS AND BAR**************

                ltext = Text(Point(825, 410),"Losses:")
                ltext.setSize(15)
                ltext.draw(win)
                lossbox = Rectangle(Point(800, 180),Point(850, 395))
                lossbox.setFill("white")
                lossbox.draw(win)
                lbar1 = Rectangle(Point(805, 185),Point(845, 195))
                lbar1.setFill("brown")
                lbar2 = Rectangle(Point(805, 200),Point(845, 210))
                lbar2.setFill("brown")
                lbar3 = Rectangle(Point(805, 215),Point(845, 225))
                lbar3.setFill("brown")
                lbar4 = Rectangle(Point(805, 230),Point(845, 240))
                lbar4.setFill("brown")
                lbar5 = Rectangle(Point(805, 245),Point(845, 255))
                lbar5.setFill("brown")
                lbar6 = Rectangle(Point(805, 260),Point(845, 270))
                lbar6.setFill("brown")
                lbar7 = Rectangle(Point(805, 275),Point(845, 285))
                lbar7.setFill("brown")
                lbar8 = Rectangle(Point(805, 290),Point(845, 300))
                lbar8.setFill("brown")
                lbar9 = Rectangle(Point(805, 305),Point(845, 315))
                lbar9.setFill("brown")
                lbar10 = Rectangle(Point(805, 320),Point(845, 330))
                lbar10.setFill("brown")
                lbar11 = Rectangle(Point(805, 335),Point(845, 345))
                lbar11.setFill("brown")
                lbar12 = Rectangle(Point(805, 350),Point(845, 360))
                lbar12.setFill("brown")
                lbar13 = Rectangle(Point(805, 365),Point(845, 375))
                lbar13.setFill("brown")
                lbar14 = Rectangle(Point(805, 380),Point(845, 390))
                lbar14.setFill("brown")
                if lscore == 1:
                    lbar1.draw(win),
                if lscore == 2:
                    lbar2.draw(win),lbar1.draw(win)
                if lscore == 3:
                    lbar3.draw(win),lbar1.draw(win),lbar2.draw(win),
                if lscore == 4:
                    lbar4.draw(win),lbar1.draw(win),lbar2.draw(win),lbar3.draw(win),
                if lscore == 5:
                    lbar5.draw(win),lbar1.draw(win),lbar2.draw(win),lbar3.draw(win),lbar4.draw(win),
                if lscore == 6:
                    lbar6.draw(win),lbar1.draw(win),lbar2.draw(win),lbar3.draw(win),lbar4.draw(win),lbar5.draw(win),
                if lscore == 7:
                    lbar7.draw(win),lbar1.draw(win),lbar2.draw(win),lbar3.draw(win),lbar4.draw(win),lbar5.draw(win),lbar6.draw(win),
                if lscore == 8:
                    lbar8.draw(win),lbar1.draw(win),lbar2.draw(win),lbar3.draw(win),lbar4.draw(win),lbar5.draw(win),lbar6.draw(win),lbar7.draw(win),
                if lscore == 9:
                    lbar9.draw(win),lbar1.draw(win),lbar2.draw(win),lbar3.draw(win),lbar4.draw(win),lbar5.draw(win),lbar6.draw(win),lbar7.draw(win),lbar8.draw(win),
                if lscore == 10:
                    lbar10.draw(win),lbar1.draw(win),lbar2.draw(win),lbar3.draw(win),lbar4.draw(win),lbar5.draw(win),lbar6.draw(win),lbar7.draw(win),lbar8.draw(win),lbar9.draw(win),
                if lscore == 11:
                    lbar11.draw(win),lbar1.draw(win),lbar2.draw(win),lbar3.draw(win),lbar4.draw(win),lbar5.draw(win),lbar6.draw(win),lbar7.draw(win),lbar8.draw(win),lbar9.draw(win),lbar10.draw(win),
                if lscore == 12:
                    lbar12.draw(win),lbar1.draw(win),lbar2.draw(win),lbar3.draw(win),lbar4.draw(win),lbar5.draw(win),lbar6.draw(win),lbar7.draw(win),lbar8.draw(win),lbar9.draw(win),lbar10.draw(win),lbar11.draw(win),
                if lscore == 13:
                    lbar13.draw(win),lbar1.draw(win),lbar2.draw(win),lbar3.draw(win),lbar4.draw(win),lbar5.draw(win),lbar6.draw(win),lbar7.draw(win),lbar8.draw(win),lbar9.draw(win),lbar10.draw(win),lbar11.draw(win),lbar12.draw(win),
                if lscore == 14:
                    lbar14.draw(win),lbar1.draw(win),lbar2.draw(win),lbar3.draw(win),lbar4.draw(win),lbar5.draw(win),lbar6.draw(win),lbar7.draw(win),lbar8.draw(win),lbar9.draw(win),lbar10.draw(win),lbar11.draw(win),lbar12.draw(win),lbar13.draw(win)

                if wscore >= 14:  #At 14 wins (when the bar is full), display special win text and reset progress
                    twin = Text(Point(500, 430),"WINNING SPREE") #The real win, resets progress
                    twin.setFace("courier")
                    twin.setStyle("italic")
                    twin.setSize(18)
                    twin.draw(win)
                    wscore = 0
                    lscore = 0

                #Quit or play again

                playagain = Button(win, Point(400,250), 175, 175,'Play Again')
                playagain.rect.setFill("lightgreen")
                playagain.activate()
                quitButton = Button(win,Point(600,250), 175, 175,'Quit')
                quitButton.rect.setFill("firebrick")
                quitButton.activate()
                while True:
                    pt = win.getMouse()
                    if playagain.clicked(pt):
                        win.close()
                        hskip = True
                        break
                    elif quitButton.clicked(pt):
                        win.close()
                        exit()

        #*************LOSING TEXT****************************************************************

            if hskip == False:
                lscore = lscore + 1
                rightarm = Line(Point(200,540),Point(240,500))
                rightarm.draw(win)
                guess1.undraw()
                cwordtext = Text(Point(600,560),"Correct word was:")
                cwordtext.setSize(20)
                cwordtext.setFace("courier")
                cwordtext.draw(win)
                rect1.undraw()
                rect2.undraw()
                rect3.undraw()
                rect4.undraw()
                rect5.undraw()
                rect6.undraw()
                rect7.undraw()
                rect8.undraw()
                rect9.undraw()
                rect10.undraw()
                rect11.undraw()
                rect12.undraw()
                rect13.undraw()
                rect14.undraw()
                ctext = Text(Point(550,300),"Hanged!")
                ctext.setSize(30)
                ctext.draw(win)
                time.sleep(2.5)
                win.close()

        #*************LOSING SCREEN***************

                win = GraphWin("Loser",1020,700)
                win.setCoords(0,0,1020,700)
                win.setBackground("lightblue")
                youlost = Text(Point(500,510),"You lost!")
                youlost.setSize(36)
                youlost.draw(win)

        # *************WIN COUNTS AND BAR**************

                wtext = Text(Point(175, 410),"Wins:")
                wtext.setSize(15)
                wtext.draw(win)
                winbox = Rectangle(Point(150, 180),Point(200, 395))
                winbox.setFill("white")
                winbox.draw(win)
                wbar1 = Rectangle(Point(155, 185),Point(195, 195))
                wbar1.setFill("brown")
                wbar2 = Rectangle(Point(155, 200),Point(195, 210))
                wbar2.setFill("brown")
                wbar3 = Rectangle(Point(155, 215),Point(195, 225))
                wbar3.setFill("brown")
                wbar4 = Rectangle(Point(155, 230),Point(195, 240))
                wbar4.setFill("brown")
                wbar5 = Rectangle(Point(155, 245),Point(195, 255))
                wbar5.setFill("brown")
                wbar6 = Rectangle(Point(155, 260),Point(195, 270))
                wbar6.setFill("brown")
                wbar7 = Rectangle(Point(155, 275),Point(195, 285))
                wbar7.setFill("brown")
                wbar8 = Rectangle(Point(155, 290),Point(195, 300))
                wbar8.setFill("brown")
                wbar9 = Rectangle(Point(155, 305),Point(195, 315))
                wbar9.setFill("brown")
                wbar10 = Rectangle(Point(155, 320),Point(195, 330))
                wbar10.setFill("brown")
                wbar11 = Rectangle(Point(155, 335),Point(195, 345))
                wbar11.setFill("brown")
                wbar12 = Rectangle(Point(155, 350),Point(195, 360))
                wbar12.setFill("brown")
                wbar13 = Rectangle(Point(155, 365),Point(195, 375))
                wbar13.setFill("brown")
                wbar14 = Rectangle(Point(155, 380),Point(195, 390))
                wbar14.setFill("brown")
                if wscore == 1:
                    wbar1.draw(win),
                if wscore == 2:
                    wbar2.draw(win),wbar1.draw(win)
                if wscore == 3:
                    wbar3.draw(win),wbar1.draw(win),wbar2.draw(win),
                if wscore == 4:
                    wbar4.draw(win),wbar1.draw(win),wbar2.draw(win),wbar3.draw(win),
                if wscore == 5:
                    wbar5.draw(win),wbar1.draw(win),wbar2.draw(win),wbar3.draw(win),wbar4.draw(win),
                if wscore == 6:
                    wbar6.draw(win),wbar1.draw(win),wbar2.draw(win),wbar3.draw(win),wbar4.draw(win),wbar5.draw(win),
                if wscore == 7:
                    wbar7.draw(win),wbar1.draw(win),wbar2.draw(win),wbar3.draw(win),wbar4.draw(win),wbar5.draw(win),wbar6.draw(win),
                if wscore == 8:
                    wbar8.draw(win),wbar1.draw(win),wbar2.draw(win),wbar3.draw(win),wbar4.draw(win),wbar5.draw(win),wbar6.draw(win),wbar7.draw(win),
                if wscore == 9:
                    wbar9.draw(win),wbar1.draw(win),wbar2.draw(win),wbar3.draw(win),wbar4.draw(win),wbar5.draw(win),wbar6.draw(win),wbar7.draw(win),wbar8.draw(win),
                if wscore == 10:
                    wbar10.draw(win),wbar1.draw(win),wbar2.draw(win),wbar3.draw(win),wbar4.draw(win),wbar5.draw(win),wbar6.draw(win),wbar7.draw(win),wbar8.draw(win),wbar9.draw(win),
                if wscore == 11:
                    wbar11.draw(win),wbar1.draw(win),wbar2.draw(win),wbar3.draw(win),wbar4.draw(win),wbar5.draw(win),wbar6.draw(win),wbar7.draw(win),wbar8.draw(win),wbar9.draw(win),wbar10.draw(win),
                if wscore == 12:
                    wbar12.draw(win),wbar1.draw(win),wbar2.draw(win),wbar3.draw(win),wbar4.draw(win),wbar5.draw(win),wbar6.draw(win),wbar7.draw(win),wbar8.draw(win),wbar9.draw(win),wbar10.draw(win),wbar11.draw(win),
                if wscore == 13:
                    wbar13.draw(win),wbar1.draw(win),wbar2.draw(win),wbar3.draw(win),wbar4.draw(win),wbar5.draw(win),wbar6.draw(win),wbar7.draw(win),wbar8.draw(win),wbar9.draw(win),wbar10.draw(win),wbar11.draw(win),wbar12.draw(win),
                if wscore == 14:
                    wbar14.draw(win),wbar1.draw(win),wbar2.draw(win),wbar3.draw(win),wbar4.draw(win),wbar5.draw(win),wbar6.draw(win),wbar7.draw(win),wbar8.draw(win),wbar9.draw(win),wbar10.draw(win),wbar11.draw(win),wbar12.draw(win),wbar13.draw(win)

        # *************LOSS COUNTS AND BAR**************

                ltext = Text(Point(825, 410),"Losses:")
                ltext.setSize(15)
                ltext.draw(win)
                lossbox = Rectangle(Point(800, 180),Point(850, 395))
                lossbox.setFill("white")
                lossbox.draw(win)
                lbar1 = Rectangle(Point(805, 185),Point(845, 195))
                lbar1.setFill("brown")
                lbar2 = Rectangle(Point(805, 200),Point(845, 210))
                lbar2.setFill("brown")
                lbar3 = Rectangle(Point(805, 215),Point(845, 225))
                lbar3.setFill("brown")
                lbar4 = Rectangle(Point(805, 230),Point(845, 240))
                lbar4.setFill("brown")
                lbar5 = Rectangle(Point(805, 245),Point(845, 255))
                lbar5.setFill("brown")
                lbar6 = Rectangle(Point(805, 260),Point(845, 270))
                lbar6.setFill("brown")
                lbar7 = Rectangle(Point(805, 275),Point(845, 285))
                lbar7.setFill("brown")
                lbar8 = Rectangle(Point(805, 290),Point(845, 300))
                lbar8.setFill("brown")
                lbar9 = Rectangle(Point(805, 305),Point(845, 315))
                lbar9.setFill("brown")
                lbar10 = Rectangle(Point(805, 320),Point(845, 330))
                lbar10.setFill("brown")
                lbar11 = Rectangle(Point(805, 335),Point(845, 345))
                lbar11.setFill("brown")
                lbar12 = Rectangle(Point(805, 350),Point(845, 360))
                lbar12.setFill("brown")
                lbar13 = Rectangle(Point(805, 365),Point(845, 375))
                lbar13.setFill("brown")
                lbar14 = Rectangle(Point(805, 380),Point(845, 390))
                lbar14.setFill("brown")
                if lscore == 1:
                    lbar1.draw(win),
                if lscore == 2:
                    lbar2.draw(win),lbar1.draw(win)
                if lscore == 3:
                    lbar3.draw(win),lbar1.draw(win),lbar2.draw(win),
                if lscore == 4:
                    lbar4.draw(win),lbar1.draw(win),lbar2.draw(win),lbar3.draw(win),
                if lscore == 5:
                    lbar5.draw(win),lbar1.draw(win),lbar2.draw(win),lbar3.draw(win),lbar4.draw(win),
                if lscore == 6:
                    lbar6.draw(win),lbar1.draw(win),lbar2.draw(win),lbar3.draw(win),lbar4.draw(win),lbar5.draw(win),
                if lscore == 7:
                    lbar7.draw(win),lbar1.draw(win),lbar2.draw(win),lbar3.draw(win),lbar4.draw(win),lbar5.draw(win),lbar6.draw(win),
                if lscore == 8:
                    lbar8.draw(win),lbar1.draw(win),lbar2.draw(win),lbar3.draw(win),lbar4.draw(win),lbar5.draw(win),lbar6.draw(win),lbar7.draw(win),
                if lscore == 9:
                    lbar9.draw(win),lbar1.draw(win),lbar2.draw(win),lbar3.draw(win),lbar4.draw(win),lbar5.draw(win),lbar6.draw(win),lbar7.draw(win),lbar8.draw(win),
                if lscore == 10:
                    lbar10.draw(win),lbar1.draw(win),lbar2.draw(win),lbar3.draw(win),lbar4.draw(win),lbar5.draw(win),lbar6.draw(win),lbar7.draw(win),lbar8.draw(win),lbar9.draw(win),
                if lscore == 11:
                    lbar11.draw(win),lbar1.draw(win),lbar2.draw(win),lbar3.draw(win),lbar4.draw(win),lbar5.draw(win),lbar6.draw(win),lbar7.draw(win),lbar8.draw(win),lbar9.draw(win),lbar10.draw(win),
                if lscore == 12:
                    lbar12.draw(win),lbar1.draw(win),lbar2.draw(win),lbar3.draw(win),lbar4.draw(win),lbar5.draw(win),lbar6.draw(win),lbar7.draw(win),lbar8.draw(win),lbar9.draw(win),lbar10.draw(win),lbar11.draw(win),
                if lscore == 13:
                    lbar13.draw(win),lbar1.draw(win),lbar2.draw(win),lbar3.draw(win),lbar4.draw(win),lbar5.draw(win),lbar6.draw(win),lbar7.draw(win),lbar8.draw(win),lbar9.draw(win),lbar10.draw(win),lbar11.draw(win),lbar12.draw(win),
                if lscore == 14:
                    lbar14.draw(win),lbar1.draw(win),lbar2.draw(win),lbar3.draw(win),lbar4.draw(win),lbar5.draw(win),lbar6.draw(win),lbar7.draw(win),lbar8.draw(win),lbar9.draw(win),lbar10.draw(win),lbar11.draw(win),lbar12.draw(win),lbar13.draw(win)

                if lscore >= 14:  #At 14 losses (when the bar is full), display special losing text and reset progress
                    twin = Text(Point(500, 430),"Losing Spree...")  #The real loss, resets progress
                    twin.setFace("courier")
                    twin.setStyle("italic")
                    twin.setSize(18)
                    twin.draw(win)
                    wscore = 0
                    lscore = 0

                #Quit or play again

                playagain = Button(win, Point(400,250), 175, 175,'Play Again')
                playagain.rect.setFill("lightgreen")
                playagain.activate()
                quitButton = Button(win,Point(600,250), 175, 175,'Quit')
                quitButton.rect.setFill("firebrick")
                quitButton.activate()
                while True:
                    pt = win.getMouse()
                    if playagain.clicked(pt):
                        win.close()
                        break
                    elif quitButton.clicked(pt):
                        win.close()
                        exit()
main()
