from tkinter import *
import tkinter.font as font
from PIL import ImageTk, Image

class Window(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.setMasterUp()
        self.pack(fill=BOTH, expand=1)
        
        self.myFont = font.Font(family='Helvetica', size=18, weight='bold')
        self.CheckbuttonFont = font.Font(family='Helvetica', size=13, weight='bold')
        self.labelFont = font.Font(family='Helvetica', size=13, weight='bold')

        self.startlabel = self.label1("Press START",20,120)
        self.startButton()

        self.setImage2()
        self.setImage1()
        self.label1("Unversity of Prince Muqrin",17,50)

        self.pageNum=0

        
    def setMasterUp(self):
        self.master.title("AI's Plan")

    def setImage1(self):
        image1 = Image.open("logo1.png")
        image1 = image1.resize((100,100), Image.ANTIALIAS)
        UPM = ImageTk.PhotoImage(image1)

        imageLabel = Label(self, image=UPM)
        imageLabel.image = UPM
        imageLabel.place(relx=1, x =-2, y=2, anchor=NE)    

    def setImage2(self):
        image1 = Image.open("bar1.png")
        image1 = image1.resize((1000,110), Image.ANTIALIAS) 
        bar = ImageTk.PhotoImage(image1)

        imageLabel = Label(self, image=bar)
        imageLabel.image = bar
        imageLabel.place(relx=1, x =-2, y=0, anchor=NE) 

    def startButton(self):
        self.startbutton = Button(self, text="Start", command=self.startPages)
        self.startbutton.place(relx = 0.5, rely = 0.9, anchor = CENTER)
        self.startbutton["font"] = self.CheckbuttonFont

    def label1(self, text, x ,y):
        label1 = Label(self, text=f"{text}")
        label1.place(x=x ,y=y)
        label1["font"] = self.myFont
        return label1

    def label2(self, text, x ,y):
        label1 = Label(self, text=f"{text}")
        label1.place(x=x ,y=y)
        label1["font"] = self.labelFont
        return label1

    def entry1(self, width, x, y):
        entry1 = Entry(self, width=width)
        entry1.place(x=x,y=y)

    def button1(self, text, relx=0.8, rely = 0.9 ,anchor = CENTER):
        button1 = Button(self, text=f"{text}", command=self.pages)
        button1.place(relx = relx, rely = rely, anchor = anchor)
        button1["font"] = self.CheckbuttonFont
        return button1

    def quitButton(self, text, relx=0.8, rely = 0.9 ,anchor = CENTER):
        button1 = Button(self, text=f"{text}", command=quit)
        button1.place(relx = relx, rely = rely, anchor = anchor)
        button1["font"] = self.CheckbuttonFont
        return button1

    def checkbutton1(self, text, x, y):
        var = IntVar()
        checkbutton1 = Checkbutton(self, text=f"{text}", variable=var)
        checkbutton1.place(x=x, y=y)
        checkbutton1["font"] = self.CheckbuttonFont
        return checkbutton1, var, text
    
    def startPages(self):
        self.startbutton.destroy()
        self.startlabel.destroy()

        self.firstPageLabel = self.label1("Check the courses you have passed",20,120)
        self.nextButton = self.button1("Next")
        self.skipButton = self.button1("Skip all", relx=0.67)
        self.pages()

    def pages(self):
        if self.pageNum == 0:
            self.page1()
            self.pageNum += 1
        
        elif self.pageNum == 1:
            self.destryPage1()
            self.page2()
            self.pageNum += 1
        
        elif self.pageNum == 2:
            self.destryPage2()
            self.page3()
            self.pageNum += 1
        
        elif self.pageNum == 3:
            self.destryPage3()
            self.page4()
            self.pageNum += 1
        
        elif self.pageNum == 4:
            self.destryPage4()
            self.page5()
            self.pageNum += 1
        
        elif self.pageNum == 5:
            self.destryPage5()
            self.page6()
            self.pageNum += 1
        
        elif self.pageNum == 6:
            self.destryPage6()
            self.page7()
            self.pageNum += 1
        
        elif self.pageNum == 7:
            self.destryPage7()
            self.page8()
            self.pageNum += 1
        
        elif self.pageNum == 8:
            self.destryPage8()
            self.finalPage()


    def page1(self):
        self.MATH101 = self.checkbutton1("MATH 101", 30, 160)
        self.PHYS101 = self.checkbutton1("PHYS 101", 30, 185)
        self.CS111   = self.checkbutton1("CS 111"  , 30, 210)
        self.ENGL101 = self.checkbutton1("ENGL 101", 30, 235)
        
    def destryPage1(self):
        self.MATH101[0].destroy()
        self.PHYS101[0].destroy()
        self.CS111[0].destroy()
        self.ENGL101[0].destroy()

    def page2(self):
        self.MATH102 = self.checkbutton1("MATH 102", 30, 160)
        self.PHYS102 = self.checkbutton1("PHYS 102", 30, 185)
        self.CS112   = self.checkbutton1("CS 112"  , 30, 210)
        self.ENGL102 = self.checkbutton1("ENGL 102", 30, 235)

    def destryPage2(self):
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

    def destryPage3(self):
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
    
    def destryPage4(self):
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

    def destryPage5(self):
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

    def destryPage6(self):
        self.AI382[0].destroy()
        self.AI316[0].destroy()
        self.AI318[0].destroy()
        self.AI312[0].destroy()
        self.AI306[0].destroy()

    def page7(self):
        self.AI491 = self.checkbutton1("AI 491", 30, 160)
        self.AI407 = self.checkbutton1("AI 407", 30, 185)
        self.AI417 = self.checkbutton1("AI 417", 30, 210)
    
    def destryPage7(self):
        self.AI491[0].destroy()
        self.AI407[0].destroy()
        self.AI417[0].destroy()


    def page8(self):
        self.AI492 = self.checkbutton1("AI 492", 30, 160)
        self.AI418 = self.checkbutton1("AI 418", 30, 185)
        self.AI438 = self.checkbutton1("AI 438", 30, 210)
    
    def destryPage8(self):
        self.AI492[0].destroy()
        self.AI418[0].destroy()
        self.AI438[0].destroy()

    def finalPage(self):
        self.firstPageLabel.destroy()
        self.nextButton.destroy()
        self.skipButton.destroy()

        self.finalPageLabel = self.label1("Here are the courses that remain for you",20,120)
        self.quitButton1 = self.quitButton("Quit")

        courses =  (self.MATH101 ,
                    self.PHYS101 ,
                    self.CS111   ,
                    self.ENGL101 ,
                    self.MATH102 ,
                    self.PHYS102 ,
                    self.CS112 ,
                    self.ENGL102 ,
                    self.MATH201 ,
                    self.CS321 ,
                    self.CS201 ,
                    self.CS211 ,
                    self.CS351 ,
                    self.STAT232 ,
                    self.MATH204 ,
                    self.AI372 ,
                    self.ENGL201 ,
                    self.CS332 ,
                    self.MATH303 ,
                    self.AI381 ,
                    self.AI305 ,
                    self.AI385 ,
                    self.AI361 ,
                    self.AI382 ,
                    self.AI316 ,
                    self.AI318 ,
                    self.AI312 ,
                    self.AI306 ,
                    self.AI491 ,
                    self.AI407 ,
                    self.AI417 ,
                    self.AI492 ,
                    self.AI418 ,
                    self.AI438 )
        x = 30
        xCounter = 0
        y = 130

        for course in courses:
            if course[1].get() == 0:
                y += 25
                xCounter += 1
                course = self.label2(f"{course[2]}",x,y)
                if xCounter == 7:
                    xCounter = 0
                    y = 130
                    x += 100



root = Tk()
root.geometry("520x400+400+150")
root.maxsize(width=520,height=400)
root.minsize(width=520,height=400)

app = Window(root)
root.mainloop()
