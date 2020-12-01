from tkinter import *
import tkinter.font as font
from PIL import ImageTk, Image
from AI import *
from SE import *
from FC import *

class Window(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.setMasterUp()
        self.pack(fill=BOTH, expand=1)
        
        self.myFont = font.Font(family='Helvetica', size=18, weight='bold')
        self.CheckbuttonFont = font.Font(family='Helvetica', size=13, weight='bold')
        self.buttonFont = font.Font(family='Helvetica', size=12, weight='bold')
        self.labelFont = font.Font(family='Helvetica', size=13, weight='bold')

        self.backgroundImage()
        self.setBar1()
        self.firstPage()

        self.pageNum = 0

    def setMasterUp(self):
        self.master.title("UPM Computer Major Plans")

    def backgroundImage(self):
        label1 = Label(self, bg="#050627", height=520, width=400)
        label1.place(x=0, y=0)  

    def setBar1(self):
        image1 = Image.open("Photos/bar2.png")
        image1 = image1.resize((520,110), Image.ANTIALIAS) 
        bar = ImageTk.PhotoImage(image1)

        imageLabel = Label(self, image=bar, bg="#050627")
        imageLabel.image = bar
        imageLabel.place( x=-2, y=-2)

    def setLogoImage(self, fileName,x ,y):
        image1 = Image.open(fileName)
        image1 = image1.resize((89,93), Image.ANTIALIAS)
        logo = ImageTk.PhotoImage(image1)

        imageLabel = Label(self, image=logo ,bg="#050627")
        imageLabel.image = logo
        imageLabel.place(x=x ,y=y)
        return imageLabel

    def firstPage(self): # This is the first page function
        self.startlabel = self.label1("Hello! Please select a major :",20,120)
        self.AI_Button = self.button1("Artificial intelligence", self.AI_press, relx = 0.2, rely = 0.5)
        self.SE_Button = self.button1("Software Engineering", self.SE_press, relx = 0.81, rely = 0.5)
        self.FC_Button = self.button1("Cyber Security", self.FC_press, relx = 0.5, rely = 0.5)

        self.AI_logo = self.setLogoImage("Photos/AI.jpg", 60 , 250)
        self.SE_logo = self.setLogoImage("Photos/SE.jpg", 375, 250)
        self.FC_logo = self.setLogoImage("Photos/FC.jpg", 215, 250)

    def AI_press(self):
        AI_startPages(self)

    def SE_press(self):
        SE_startPages(self)

    def FC_press(self):
        FC_startPages(self)

    def label1(self, text, x ,y): # This label uses the 18 sized font
        label1 = Label(self, text=f"{text}", bg="#050627", fg='white')
        label1.place(x=x ,y=y)
        label1["font"] = self.myFont
        return label1

    def label2(self, text, x ,y): # This label uses the 13 sized font
        label1 = Label(self, text=f"{text}", bg="#050627", fg='white')
        label1.place(x=x ,y=y)
        label1["font"] = self.labelFont
        return label1

    def button1(self, text, command, relx=0.8, rely = 0.9 ,anchor = CENTER):
        button1 = Button(self, text=f"{text}", command=command, relief=RIDGE, bg="#4CBB17", fg="white")
        button1.place(relx = relx, rely = rely, anchor = anchor)
        button1["font"] = self.buttonFont
        return button1

    def checkbutton1(self, text, x, y):
        var = IntVar()
        checkbutton1 = Checkbutton(self, text=f"{text}", variable=var, bg="#050627", fg="white", cursor="hand1",
                                         selectcolor="#4CBB17", activebackground="#050627", activeforeground="yellow")
        checkbutton1.place(x=x, y=y)
        checkbutton1["font"] = self.CheckbuttonFont
        return checkbutton1, var, text

root = Tk()
root.geometry("520x400+400+150")
root.maxsize(width=520,height=400)
root.minsize(width=520,height=400)

app = Window(root)
root.mainloop()
