from tkinter import *
import tkinter
root = Tk()

def key(event):
    print ("pressed", repr(event.char))

def callback(event):
    frame.focus_set()
    print ("clicked at", event.x, event.y)


def aaa(event):
    print(dir(tkinter))


def left(event):
    print("left", event.x, event.y)

frame = Frame(root, width=100, height=100)

frame.bind("<Button-1>", callback)
#frame.bind("<B1-Motion>", callback)
#frame.bind("<ButtonRelease-1>", callback)
#frame.bind("<Double-Button-1>", left)
#frame.bind("<MouseWheel>", left)
#frame.bind("<Motion>", left)

frame.bind("<Leave>", left)
#frame.bind("<Enter>", left)
#frame.bind("<FocusIn>", left)
#frame.bind("<FocusOut>", left)

#frame.bind("<Activate>", left)
#frame.bind("<Deactivate>", left)

frame.bind("<Key>", key)
frame.bind("a", aaa)
#frame.bind("b", aaa)
#frame.bind("<KeyRelease>", left)

frame.pack() 
root.mainloop()
