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

        self.label1("Press START",20,120)
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

    def entry1(self, width, x, y):
    	entry1 = Entry(self, width=width)
    	entry1.place(x=x,y=y)

    def button1(self, text, relx=0.8, rely = 0.9 ,anchor = CENTER):
    	button1 = Button(self, text=f"{text}", command=self.pages)
    	button1.place(relx = relx, rely = rely, anchor = anchor)
    	button1["font"] = self.CheckbuttonFont

    def checkbutton1(self, text, x, y):
        checkbutton1 = Checkbutton(self, text=f"{text}")
        checkbutton1.place(x=x, y=y)
        checkbutton1["font"] = self.CheckbuttonFont
        return checkbutton1
    
    def startPages(self):
        self.startbutton.destroy()
        self.label1("Check the courses you have passed",20,120)
        self.button1("Next")
        self.button1("Skip all", relx=0.67)
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
            # self.page3()
            self.pageNum += 1

    def page1(self):
        self.MATH101 = self.checkbutton1("MATH 101", 30, 160)
        self.PHYS101 = self.checkbutton1("PHYS 101", 30, 185)
        self.CS111 =   self.checkbutton1("CS 111"  , 30, 210)
        self.ENGL101 = self.checkbutton1("ENGL 101", 30, 235)

    def destryPage1(self):
        self.MATH101.destroy()
        self.PHYS101.destroy()
        self.CS111.destroy()
        self.ENGL101.destroy()


    def page2(self):
        self.MATH102 = self.checkbutton1("MATH 102", 30, 160)
        self.PHYS102 = self.checkbutton1("PHYS 102", 30, 185)
        self.CS112 =   self.checkbutton1("CS 112"  , 30, 210)
        self.ENGL102 = self.checkbutton1("ENGL 102", 30, 235)

    def destryPage2(self):
        self.MATH102.destroy()
        self.PHYS102.destroy()
        self.CS112.destroy()
        self.ENGL102.destroy()


        
root = Tk()
root.geometry("500x350")

app = Window(root)
root.mainloop()