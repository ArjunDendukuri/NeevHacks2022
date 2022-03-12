from tkinter import *
import os

def tk_run():
    root = Tk()
    root.title("GUI")
    root.geometry("1980x1080")
    root.iconbitmap('')

    itemname = Label(root,text = "lols",font = ("courier new",30))
    itemname.place(x=1000,y=10)
    
    root_file = os.path.dirname(__file__)
    
    seprator = "\\"

    if not os.name == "nt":
        seprator = "/"


    sky = PhotoImage(file=root_file+"{}full_clean_ocean.png".format(seprator))

    bt1 = Button(root,bd=1,text="  .  ")
    bt1.place(x=10,y=10)
    bt2 = Button(root,bd=1,text="  .  ")
    bt2.place(x=35,y=10)
    bt3 = Button(root,bd=1,text="  .  ")
    bt3.place(x=60,y=10)
    bt4 = Button(root,bd=1,text="  .  ")
    bt4.place(x=85,y=10)
    bt5 = Button(root,bd=1,text="  .  ")
    bt5.place(x=110,y=10)
    bt6 = Button(root,bd=1,text="  .  ")
    bt6.place(x=135,y=10)
    bt7 = Button(root,bd=1,text="  .  ")
    bt7.place(x=160,y=10)
    bt8 = Button(root,bd=1,text="  .  ")
    bt8.place(x=185,y=10)
    bt9 = Button(root,bd=1,text="  .  ")
    bt9.place(x=210,y=10)

    root.mainloop()
