def SE_startPages(self):
    
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
    self.PHYS102[0].destroy()
    self.CS112[0].destroy()
    self.MATH102[0].destroy()
    self.ENGL102[0].destroy()

def page3(self):
    self.CS351 = self.checkbutton1("CS 351", 30, 160)
    self.CS201   = self.checkbutton1("CS 201", 30, 185)
    self.CS211   = self.checkbutton1("CS 211", 30, 210)
    self.ENGL201    = self.checkbutton1("ENGL 201", 30, 235)

def destroyPage3(self):
    self.CS351[0].destroy()
    self.CS201[0].destroy()
    self.CS211[0].destroy()
    self.ENGL201[0].destroy()

def page4(self):
    self.STAT232 = self.checkbutton1("STAT 232", 30, 160)
    self.MATH202 = self.checkbutton1("MATH 202", 30, 185)
    self.CS224   = self.checkbutton1("CS 224", 30, 210)
    self.SE262 = self.checkbutton1("SE 262", 30, 235)
    self.CS332   = self.checkbutton1("CS 332", 30, 260)

def destroyPage4(self):
    self.STAT232[0].destroy()
    self.MATH202[0].destroy()
    self.CS224[0].destroy()
    self.SE262[0].destroy()
    self.CS332[0].destroy()    

def page5(self):
    self.MATH204 = self.checkbutton1("MATH 204", 30, 160)
    self.CS321   = self.checkbutton1("CS 321", 30, 185)
    self.SE464   = self.checkbutton1("CS 464", 30, 210)
    self.SE311   = self.checkbutton1("SE 311", 30, 235)
    self.SE323   = self.checkbutton1("SE 323", 30, 260)

def destroyPage5(self):
    self.MATH204[0].destroy()
    self.CS321[0].destroy()
    self.SE464[0].destroy()
    self.SE311[0].destroy()
    self.SE323[0].destroy() 

def page6(self):
    self.SE342 = self.checkbutton1("SE 342", 30, 160)
    self.CS332 = self.checkbutton1("CS 332", 30, 185)
    self.SE463 = self.checkbutton1("SE 463", 30, 210)
    self.SE324 = self.checkbutton1("SE 324", 30, 235)
    self.FC372 = self.checkbutton1("FC 372", 30, 260)

def destroyPage6(self):
    self.SE342[0].destroy()
    self.CS332[0].destroy()
    self.SE463[0].destroy()
    self.SE324[0].destroy()
    self.FC372[0].destroy()

def page7(self):
    self.SE491 = self.checkbutton1("SE 491", 30, 160)
    self.SE431 = self.checkbutton1("SE 431", 30, 185)

def destroyPage7(self):
    self.SE491[0].destroy()
    self.SE431[0].destroy()    

def page8(self):
    self.SE492 = self.checkbutton1("SE 492", 30, 160)
    self.SE472 = self.checkbutton1("SE 472", 30, 185)

def destroyPage8(self):
    self.SE492[0].destroy()
    self.SE472[0].destroy()
    
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
        else :
            if self.MATH202[1].get() == 0:
                coursesList.append(self.MATH202[2])
            if self.MATH204[1].get() == 0:
                coursesList.append(self.MATH204[2])
            if self.STAT232[1].get() == 0:
                coursesList.append(self.STAT232[2])
            if self.CS201[1].get() == 0:
                coursesList.append(self.CS201[2])
            else:
                if self.CS224[1].get() == 0:
                    coursesList.append(self.CS224[2])
                if self.CS211[1].get() == 0:
                    coursesList.append(self.CS211[2])
                else:
                    if self.CS321[1].get() == 0:
                        coursesList.append(self.CS321[2])

    if self.PHYS101[1].get() == 0:
        coursesList.append(self.PHYS101[2])
    else:
        if self.PHYS102[1].get() == 0:
            coursesList.append(self.PHYS102[2])

    if self.CS111[1].get() == 0:
        coursesList.append(self.CS111[2])
    else:
        if self.CS112[1].get() == 0:
            coursesList.append(self.CS112[2])
        else:
            if self.CS351[1].get() == 0:
                coursesList.append(self.CS351[2])
            if self.CS211[1].get() == 0:
                coursesList.append(self.CS211[2])
            else:
                if self.SE262[1].get() == 0:
                    coursesList.append(self.SE262[2])
                else:
                    if self.SE464[1].get() == 0:
                        coursesList.append(self.SE464[2])               
                    if self.SE311[1].get() == 0:
                        coursesList.append(self.SE311[2])
                    else:
                        if self.SE463[1].get() == 0:
                            coursesList.append(self.SE463[2])
                    if self.SE323[1].get() == 0:
                        coursesList.append(self.SE323[2])
                    else:
                        if self.SE342[1].get() == 0:
                            coursesList.append(self.SE342[2])
                        if self.SE324[1].get() == 0:
                            coursesList.append(self.SE324[2])
                    if self.SE431[1].get() == 0:
                        coursesList.append(self.SE431[2])



            if self.CS332[1].get() == 0:
                coursesList.append(self.CS332[2])
            else:
                if self.SE472[1].get() == 0:
                    coursesList.append(self.SE472[2])
    if self.ENGL101[1].get() == 0:
        coursesList.append(self.ENGL101[2])
    else:
        if self.ENGL102[1].get() == 0:
            coursesList.append(self.ENGL102[2])
        else:
            if self.ENGL201[1].get() ==0:
                coursesList.append(self.ENGL201[2])

                    











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
