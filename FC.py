def FC_startPages(self):
    
    def pagesPress():
        pages(self)

    def skipPress():
        skipAll(self)

    def backPress():
        backToTheMainPage(self)

    self.AI_Button.destroy()
    self.SE_Button.destroy()
    self.FC_Button.destroy()

    self.AI_logo.destroy()
    self.SE_logo.destroy()
    self.FC_logo.destroy()
    
    self.startlabel.destroy()

    self.firstPageLabel = self.label1("Mark the completed courses",20,120)
    self.nextButton = self.button1("Next",pagesPress)
    self.skipButton = self.button1("Skip all", skipPress, relx=0.67)
    self.backButton = self.button1("Back" , backPress, relx=0.15)

    pages(self)

def pages(self):
    if self.pageNum == 0:
        page1(self)
        self.pageNum += 1
    
    elif self.pageNum == 1:
        destroyPage1(self)
        page2(self)
        self.pageNum += 1
    
    elif self.pageNum == 2:
        destroyPage2(self)
        page3(self)
        self.pageNum += 1
    
    elif self.pageNum == 3:
        destroyPage3(self)
        page4(self)
        self.pageNum += 1
    
    elif self.pageNum == 4:
        destroyPage4(self)
        page5(self)
        self.pageNum += 1
    
    elif self.pageNum == 5:
        destroyPage5(self)
        page6(self)
        self.pageNum += 1
    
    elif self.pageNum == 6:
        destroyPage6(self)
        page7(self)
        self.pageNum += 1
    
    elif self.pageNum == 7:
        destroyPage7(self)
        page8(self)
        self.pageNum += 1
    
    elif self.pageNum == 8:
        destroyPage8(self)
        finalPage(self)

def skipAll(self):
    destroyPagesTuple = (destroyPage1,
                        destroyPage2,
                        destroyPage3,
                        destroyPage4,
                        destroyPage5,
                        destroyPage6,
                        destroyPage7,
                        destroyPage8,
                        finalPage)

    PagesTuple=(page1,
                page2,
                page3,
                page4,
                page5,
                page6,
                page7,
                page8)

    for function in range(len(destroyPagesTuple)):
        try:
            destroyPagesTuple[function](self)
        except:
            PagesTuple[function](self)
            try:
                destroyPagesTuple[function](self)
            except:
                pass

def backToTheMainPage(self):
    destroyPagesTuple = (destroyPage1,
                        destroyPage2,
                        destroyPage3,
                        destroyPage4,
                        destroyPage5,
                        destroyPage6,
                        destroyPage7,
                        destroyPage8)

    for function in range(len(destroyPagesTuple)):
        try:
            destroyPagesTuple[function](self)
        except:
            pass
    
    self.firstPageLabel.destroy()
    self.nextButton.destroy()
    self.skipButton.destroy()
    self.backButton.destroy()

    self.pageNum = 0
    try:
        self.finalPageLabel.destroy()
        self.quitButton1.destroy()

        for label in self.labelsList:
            label.destroy()
    except:
        pass

    self.firstPage()

def page1(self):
    self.MATH101 = self.checkbutton1("MATH 101", 30, 160)
    self.PHYS101 = self.checkbutton1("PHYS 101", 30, 185)
    self.CS111   = self.checkbutton1("CS 111"  , 30, 210)
    self.ENGL101 = self.checkbutton1("ENGL 101", 30, 235)
    
def destroyPage1(self):
    self.MATH101[0].destroy()
    self.PHYS101[0].destroy()
    self.CS111[0].destroy()
    self.ENGL101[0].destroy()

def page2(self):
    self.MATH102 = self.checkbutton1("MATH 102", 30, 160)
    self.PHYS102 = self.checkbutton1("PHYS 102", 30, 185)
    self.CS112   = self.checkbutton1("CS 112"  , 30, 210)
    self.ENGL102 = self.checkbutton1("ENGL 102", 30, 235)

def destroyPage2(self):
    self.MATH102[0].destroy()
    self.PHYS102[0].destroy()
    self.CS112[0].destroy()
    self.ENGL102[0].destroy()

def page3(self):
    self.CS201 = self.checkbutton1("CS 201", 30, 160)
    self.CS211   = self.checkbutton1("CS 211", 30, 185)
    self.CS221   = self.checkbutton1("CS 221", 30, 210)
    self.CS351   = self.checkbutton1("CS 351", 30, 235)

def destroyPage3(self):
    self.CS201[0].destroy()
    self.CS211[0].destroy()
    self.CS221[0].destroy()
    self.CS351[0].destroy()

def page4(self):
    self.STAT232 = self.checkbutton1("STAT 232", 30, 160)
    self.CS262 = self.checkbutton1("CS 262", 30, 185)
    self.CS314   = self.checkbutton1("CS 314", 30, 210)
    self.CS232 = self.checkbutton1("CS 232", 30, 235)

def destroyPage4(self):
    self.STAT232[0].destroy()
    self.CS262[0].destroy()
    self.CS314[0].destroy()
    self.CS232[0].destroy() 

def page5(self):
    self.FC381 = self.checkbutton1("FC 381", 30, 160)
    self.FC313   = self.checkbutton1("FC 313", 30, 185)
    self.FC353   = self.checkbutton1("FC 353", 30, 210)
    self.ENGL201   = self.checkbutton1("ENGL 201", 30, 235)
    self.FC311   = self.checkbutton1("FC 311", 30, 260)

def destroyPage5(self):
    self.FC381[0].destroy()
    self.FC313[0].destroy()
    self.FC353[0].destroy()
    self.ENGL201[0].destroy()
    self.FC311[0].destroy() 

def page6(self):
    self.FC302 = self.checkbutton1("FC 302", 30, 160)
    self.FC332 = self.checkbutton1("FC 332", 30, 185)
    self.FC372 = self.checkbutton1("FC 372", 30, 210)
    self.FC304 = self.checkbutton1("FC 304", 30, 235)
    self.FC382 = self.checkbutton1("FC 382", 30, 260)

def destroyPage6(self):
    self.FC302[0].destroy()
    self.FC332[0].destroy()
    self.FC372[0].destroy()
    self.FC304[0].destroy()
    self.FC382[0].destroy()

def page7(self):
    self.FC491 = self.checkbutton1("FC 491", 30, 160)
    self.FC411 = self.checkbutton1("FC 411", 30, 185)
    self.FC421 = self.checkbutton1("FC 421", 30, 210)

def destroyPage7(self):
    self.FC491[0].destroy()
    self.FC411[0].destroy()
    self.FC421[0].destroy()
    
def page8(self):
    self.FC492 = self.checkbutton1("FC 492", 30, 160)
    self.FC472 = self.checkbutton1("FC 472", 30, 185)
    self.FC462 = self.checkbutton1("FC 462", 30, 210)

def destroyPage8(self):
    self.FC492[0].destroy()
    self.FC472[0].destroy()
    self.FC462[0].destroy()

def finalPage(self):
    self.firstPageLabel.destroy()
    self.nextButton.destroy()
    self.skipButton.destroy()

    self.finalPageLabel = self.label1("These are the available courses",20,120)
    self.quitButton1 = self.button1("Quit", quit, relx=0.28)

    coursesList = []     
    coursesList.sort()

    x = 30
    xCounter = 0
    y = 155

    self.labelsList = []  

    for course in coursesList:
            self.labelsList.append(self.label2(course,x,y))
            
            y += 25
            xCounter += 1
            if xCounter == 7:
                xCounter = 0
                y = 155
                x += 100
