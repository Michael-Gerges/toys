#os.system("pip install psutil")
#os.system("pip install pywin32")

import win32console , win32gui;win32gui.ShowWindow(win32console.GetConsoleWindow(), 0)


from tkinter import messagebox, filedialog, scrolledtext
from tkinter import * ;window=Tk(); window.geometry("420x360"); window.title("michael"); window.resizable(True,True)
from tkinter import ttk


tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control) ; tab_control.add(tab1, text='First')
tab2 = ttk.Frame(tab_control) ; tab_control.add(tab2, text='Second')
tab3 = ttk.Frame(tab_control) ; tab_control.add(tab3, text='Third' )
tab4 = ttk.Frame(tab_control) ; tab_control.add(tab4, text='Forth' )
tab5 = ttk.Frame(tab_control) ; tab_control.add(tab5, text='Fifth' )


tab_control.grid(column=6, row=6)



## tab 1 

lbl = Label(tab1, text="hello",  padx=2, pady=2) ; lbl.grid(column=0, row=1) 
txt = Entry(tab1,width=10) ; txt.grid(column=0,row=2) ; txt.focus()
#Listbox(tab1 ).grid(column=0,row=9)
def get_text():
    lbl.configure(text=txt.get())


def destroy_label():
    global lbl
    lbl.destroy()
    lbl = Label(tab1) ; lbl.grid(column=0, row=1) 


buttom_for_text_and_label = Button(tab1, width=5, height=1, text="get text", command=get_text).grid(column=0,row=3)
Button(tab1, text="destroy The Label!", command=destroy_label).grid(column=1, row=4)

### tab 2 


def msg_btn_fun():
    #res = messagebox.showinfo('Message title', 'Message content')
    #res = messagebox.showwarning('Message title', 'Message content') 
    #res = messagebox.showerror('Message title', 'Message content')  
    #res = messagebox.askquestion('Message title','Message content')
    #res = messagebox.askyesno('Message title','Message content')
    res = messagebox.askyesnocancel('Message title','Message content')
    #res = messagebox.askokcancel('Message title','Message content')
    #res = messagebox.askretrycancel('Message title','Message content')




spin,spin2 = 0,0
def show_spins():
  global spin,spin2
  var2 =IntVar()
  var2.set(36)
  spin = Spinbox(tab2, from_=0, to=100, width=5, textvariable=var2);spin.grid(column=0,row=1)
  spin2 = Spinbox(tab2, values=(3, 8, 11), width=5);spin2.grid(column=0,row=2)

  



def open_files_and_folders():
    file = filedialog.askopenfilename()
    files = filedialog.askopenfilenames()
    file = filedialog.askopenfilename(filetypes = (("Text files","*.txt"),("all files","*.*")))
    dir = filedialog.askdirectory()
    from os import path
    file = filedialog.askopenfilename(initialdir= path.dirname(__file__))




msg_btn = Button(tab2, text="show messages", font=("Arial Bold",18), fg="red",bg="yellow",command=msg_btn_fun).grid(column=0,row=9)
spins_button = Button(tab2, text="show 2 spins", command=show_spins).grid(column=0,row=10)
files_btn = Button(tab2, text="open some files ", font=("Times New Roman Bold",12), fg="blue",bg="black",command=open_files_and_folders).grid(column=0,row=11)



### tab3 

ch_state = BooleanVar(); ch_state.set(True)
def chosen_or_not():
    if ch_state.get():
        Label(tab1, text="'is that cool?' is checked").grid(column=0,row=4)
    else:
        Label(tab1, width=10).grid(column=0,row=5)
ch = Checkbutton(tab3, text="is that cool?", var=ch_state, command=chosen_or_not)
ch.grid(column=0,row=3)



selected = IntVar() ; selected.set(2)
rad1 = Radiobutton(tab3,text='First', value=1, variable=selected) ; rad1.grid(column=0, row=4)
rad2 = Radiobutton(tab3,text='Second', value=2, variable=selected) ; rad2.grid(column=1, row=4)
rad3 = Radiobutton(tab3,text='Third', value=3, variable=selected) ; rad3.grid(column=2, row=4)
def buttom_for_radios_function():
    text_radio = "choice is " +str(selected.get())
    Label(tab1, text=text_radio).grid(column=0, row=6)
buttom_for_radios = Button(tab3, text="show the choice in tab1", command=buttom_for_radios_function)
buttom_for_radios.grid(column=0, row=5)



### tab4
def showimage():
    photo = PhotoImage(file = r"C:\users\micha\desktop\l.png")

    imaglabel = ttk.Label(tab4,text="cfvgbh",image=photo, compound="image")
    imaglabel.grid(column=4,row=4)


showtheimagebutton = Button(tab4, text="show img", width=9, height=4, command=showimage)
showtheimagebutton.grid(column=0,row=8)

def create_ascrolledtext():
  Scrolled_txt = scrolledtext.ScrolledText(tab4,width=10,height=10)
  Scrolled_txt.grid(column=0,row=8)

scrolling_creator = Button(tab4, text="create a square", command=create_ascrolledtext).grid(column=2,row=2) 



### tab 5

def insertt(strr,place):
    return strr[:place] + "\n" + strr[place:]

def msg_btn_fun():
    res = messagebox.askyesnocancel('Message title','Message content')
    txxt = str(dir(res)) +str(res) + str(type(res))
    number_f_char =    ( (window.winfo_width() * 270) // 1280 )-10


    n = len(txxt) // number_f_char 

    for i in range(n):
        txxt = insertt(txxt, ((i+1)*number_f_char )+i*2)
    Label(tab5,justify="left", text=txxt, height=n+1, bg="gold").grid(column=0, row=0) 


msg_btn = Button(tab5,text="show messages", font=("Arial Bold",18), fg="green",bg="blue",command=msg_btn_fun).grid(column=0,row=4)


#var2 =IntVar()
#var2.set(36)
#spin = Spinbox(tab5, from_=0, to=100, width=5, textvariable=var2);spin.grid(column=0,row=1)
#spin2 = Spinbox(tab5, values=(3, 8, 11), width=5);spin2.grid(column=0,row=2)

def spinner():
    Label(tab5, text="go to tab 1 to see the answer", height=5).grid(column=0, row=10) 
    try:
       txxt = "the summation of the spinners in the Second tab is "+str(int(spin.get()) +int(spin2.get()))
    except:
        txxt= "please press 'show 2 spins' in the Second tab"
    Label(tab1, text=txxt, height=1).grid(column=0, row=7) 

msg_btn = Button(tab5, text="get the summmation of the spinners", font=("Arial Bold",18), fg="purple",bg="cyan",command=spinner).grid(column=0,row=9)

def funn():
  Label(tab5, text=str(window.winfo_geometry())).grid(column=3,row=3)

Button(tab5,text="whats my size", command=funn).grid(column=1,row=2)

#Scrollbar(tab1).grid(column=80,row=90)
window.mainloop()
