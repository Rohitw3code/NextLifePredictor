from tkinter import *
from tkinter import ttk
import random as rd
import os
from PIL import ImageTk,Image 

root = Tk()

style = ttk.Style()
style.map("C.TButton",
    foreground=[('pressed', 'red'), ('active', 'blue')],
    background=[('pressed', '!disabled', 'black'), ('active', 'white')]
    )
Estyle = ttk.Style()
Estyle.configure('TEntry', foreground = 'green')

options = [
    "Beluga",
    "Rehan",
    "Rishabh",
    "ishtika",
    "Aditi singh",
    "Princy",
    "Priyanshu",
    "Yash Arora",
    "Shubham Tiwari"
]

class App:
	def __init__(self,root):
		self.root = root
		root.geometry("860x500")
		Label(root,text="Next Life Predictor Game", font=("Helvetica",25)).pack(pady=20)

		clicked = StringVar()
		clicked.set("Beluga")
		drop = OptionMenu( root , clicked , *options)
		drop.config(width=20, font=("Helvetica",15))
		drop.place(x=20,y=100)
		
		submit = Button(root,text="Predict My Next Life", font=("Helvetica",15),width=20,command=lambda :self.predictNextLif()).place(x=20,y=150)


		self.canvas = Canvas(root, width = 200, height = 200)  
		Label(root,text="Wife Photo :)", font=("Helvetica",15)).place(x=700,y=270)
		
		self.name = Label(root,text="Name : ", font=("Helvetica",15))
		self.edu = Label(root,text="Education : ", font=("Helvetica",15))
		self.occ = Label(root,text="kya bano ge : ", font=("Helvetica",15))
		self.wife = Label(root,text="Wife : ", font=("Helvetica",15))
		self.child = Label(root,text="No. of child : ", font=("Helvetica",15))
		self.money = Label(root,text="Money : ", font=("Helvetica",15))

		xMargin = 320

		self.name.place(x=xMargin,y=100)
		self.edu.place(x=xMargin,y=150)
		self.occ.place(x=xMargin,y=200)
		self.wife.place(x=xMargin,y=250)
		self.child.place(x=xMargin,y=300)
		self.money.place(x=xMargin,y=350)

		self.canvas.place(x=650,y=50)

		root.mainloop()

	def predictNextLif(self):
		file = open("data/education.txt").readlines() 
		self.edu.config(text="Education : "+str(rd.choice(file)))

		file = open("data/occupation.txt").readlines() 
		self.occ.config(text="kya bano ge : "+str(rd.choice(file)))

		file = open("data/name.txt").readlines() 
		self.name.config(text="Name : "+str(rd.choice(file)))

		file = open("data/wife.txt").readlines() 
		self.wife.config(text="Wife : "+str(rd.choice(file)))

		file = open("data/child.txt").readlines() 
		self.child.config(text="No. of child : "+str(rd.choice(file)))

		file = open("data/paisa.txt").readlines() 
		self.money.config(text="Money : "+str(rd.choice(file)))

		iname = rd.choice(os.listdir("image"))
		self.image = Image.open("image/"+iname)
		self.image = self.image.resize((200, 200), Image.ANTIALIAS)
		self.img = ImageTk.PhotoImage(self.image) 
		self.canvas.create_image(20, 20, anchor=NW, image=self.img) 






app = App(root)
