def AI_startPages(self):
    
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
    self.MATH201 = self.checkbutton1("MATH 201", 30, 160)
    self.CS321   = self.checkbutton1("CS 321", 30, 185)
    self.CS201   = self.checkbutton1("CS 201", 30, 210)
    self.CS211   = self.checkbutton1("CS 211", 30, 235)
    self.CS351   = self.checkbutton1("CS 351", 30, 260)

def destroyPage3(self):
    self.MATH201[0].destroy()
    self.CS321[0].destroy()
    self.CS201[0].destroy()
    self.CS211[0].destroy()
    self.CS351[0].destroy()

def page4(self):
    self.STAT232 = self.checkbutton1("STAT 232", 30, 160)
    self.MATH204 = self.checkbutton1("MATH 204", 30, 185)
    self.AI372   = self.checkbutton1("AI 372", 30, 210)
    self.ENGL201 = self.checkbutton1("ENGL 201", 30, 235)
    self.CS332   = self.checkbutton1("CS 332", 30, 260)

def destroyPage4(self):
    self.STAT232[0].destroy()
    self.MATH204[0].destroy()
    self.AI372[0].destroy()
    self.ENGL201[0].destroy()
    self.CS332[0].destroy()    

def page5(self):
    self.MATH303 = self.checkbutton1("MATH 303", 30, 160)
    self.AI381   = self.checkbutton1("AI 381", 30, 185)
    self.AI305   = self.checkbutton1("AI 305", 30, 210)
    self.AI385   = self.checkbutton1("AI 385", 30, 235)
    self.AI361   = self.checkbutton1("AI 361", 30, 260)

def destroyPage5(self):
    self.MATH303[0].destroy()
    self.AI381[0].destroy()
    self.AI305[0].destroy()
    self.AI385[0].destroy()
    self.AI361[0].destroy() 

def page6(self):
    self.AI382 = self.checkbutton1("AI 382", 30, 160)
    self.AI316 = self.checkbutton1("AI 316", 30, 185)
    self.AI318 = self.checkbutton1("AI 318", 30, 210)
    self.AI312 = self.checkbutton1("AI 312", 30, 235)
    self.AI306 = self.checkbutton1("AI 306", 30, 260)

def destroyPage6(self):
    self.AI382[0].destroy()
    self.AI316[0].destroy()
    self.AI318[0].destroy()
    self.AI312[0].destroy()
    self.AI306[0].destroy()

def page7(self):
    self.AI491 = self.checkbutton1("AI 491", 30, 160)
    self.AI407 = self.checkbutton1("AI 407", 30, 185)
    self.AI417 = self.checkbutton1("AI 417", 30, 210)

def destroyPage7(self):
    self.AI491[0].destroy()
    self.AI407[0].destroy()
    self.AI417[0].destroy()
    

def page8(self):
    self.AI492 = self.checkbutton1("AI 492", 30, 160)
    self.AI418 = self.checkbutton1("AI 418", 30, 185)
    self.AI438 = self.checkbutton1("AI 438", 30, 210)

def destroyPage8(self):
    self.AI492[0].destroy()
    self.AI418[0].destroy()
    self.AI438[0].destroy()

def finalPage(self):
    self.firstPageLabel.destroy()
    self.nextButton.destroy()
    self.skipButton.destroy()

    self.finalPageLabel = self.label1("These are the available courses",20,120)
    self.quitButton1 = self.button1("Quit", quit, relx=0.28)

    coursesList = []

    if self.MATH101[1].get() == 0:
        coursesList.append(self.MATH101[2])
    else :
        if self.MATH102[1].get() == 0:
            coursesList.append(self.MATH102[2])
        else:
            if self.MATH201[1].get() == 0:
                coursesList.append(self.MATH201[2])
            if self.CS201[1].get() == 0:
                coursesList.append(self.CS201[2])
            if self.STAT232[1].get() == 0:
                coursesList.append(self.STAT232[2])
            if self.MATH204[1].get() == 0:
                coursesList.append(self.MATH204[2])
            else:
                if self.AI305[1].get() == 0:
                    coursesList.append(self.AI305[2])
                else:
                    if self.AI318[1].get() == 0:
                        coursesList.append(self.AI318[2])
                    if self.AI312[1].get() == 0:
                        coursesList.append(self.AI312[2])
                    if self.AI306[1].get() == 0:
                        coursesList.append(self.AI306[2])
                    if self.AI417[1].get() == 0:
                        coursesList.append(self.AI417[2])
                if self.AI385[1].get() == 0:
                    coursesList.append(self.AI385[2])
                if self.AI361[1].get() == 0:
                    coursesList.append(self.AI361[2])
            if self.MATH303[1].get() == 0:
                coursesList.append(self.MATH303[2])
            else:
                if self.AI316[1].get() == 0:
                    coursesList.append(self.AI316[2])
                    
    if self.PHYS101[1].get() == 0:
        coursesList.append(self.PHYS101[2])
    else:
        if self.PHYS102[1].get() == 0:
            coursesList.append(self.PHYS102[2])
            
    if self.ENGL101[1].get() == 0:
        coursesList.append(self.ENGL101[2])
    else:
        if self.ENGL102[1].get() == 0:
            coursesList.append(self.ENGL102[2])

    if self.CS111[1].get() == 0:
        coursesList.append(self.CS111[2])
    else:
        if self.CS112[1].get() == 0:
            coursesList.append(self.CS112[2])
        else:
            if self.CS321[1].get() == 0:
                coursesList.append(self.CS321[2])
            if self.CS211[1].get() == 0:
                coursesList.append(self.CS211[2])
            else:
                if self.AI381[1].get() == 0:
                    coursesList.append(self.AI381[2])
                else:
                    if self.AI382[1].get() == 0:
                        coursesList.append(self.AI382[2])
                    else:
                        if self.AI438[1].get() == 0:
                            coursesList.append(self.AI438[2])

            if self.CS351[1].get() == 0:
                coursesList.append(self.CS351[2])
            if self.ENGL201[1].get() == 0:
                coursesList.append(self.ENGL201[2])
            if self.CS332[1].get() == 0:
                coursesList.append(self.CS332[2])
                


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
