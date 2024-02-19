from tkinter import *
from tkinter.ttk import *

#To create a file dialog (file chooser), you can use the filedialog class like this:


window = Tk()

window.title("Welcome to LikeGeeks app")

# tab_control = ttk.Notebook(window)

# tab1 = ttk.Frame(tab_control)
# tab_control.add(tab1, text='First')

# tab2 = ttk.Frame(tab_control)
# tab_control.add(tab2, text='second')

# lbl1 = Label(tab1, text= 'label1', padx=5, pady=5)

# lbl1.grid(column=0, row=0)

# lbl2 = Label(tab2, text= 'label2')

# lbl2.grid(column=0, row=0)

# tab_control.pack(expand=1, fill='both')



# create menu

# window = Tk()
# window.title("Welcome to LikeGeeks app")

# menu = Menu(window)

# new_item = Menu(menu)

# new_item.add_command(label='New') #, command=clicked

# new_item.add_separator()

# new_item.add_command(label='Edit')

# menu.add_cascade(label='File', menu=new_item)
# window.config(menu=menu)




# file = filedialog.askopenfilename()
# dir = filedialog.askdirectory()
# file = filedialog.askopenfilename(initialdir= path.dirname(__file__))
# file = filedialog.askopenfilename(filetypes = (("Text files","*.txt"),("all files","*.*")))





#create progress bar
# random_number = random.randint(0, 100)


# window = Tk()

# window.title("Centenial College")
# window.geometry('350x200')

# style = ttk.Style()

# style.theme_use('default')

# style.configure("red.Horizontal.TProgressbar", background='blue')


# bar = Progressbar(window, length=200,style='red.Horizontal.TProgressbar')

# bar['value'] = 80

# bar.grid(column=0, row=0)



# spin = Spinbox(window, from_=0, to=10, width=5)


# def clicked():
#     print(spin.get())
# spin = Spinbox(window, values=(3,8,11), width=5, command=clicked)
# spin.set(8)




# spin.grid(column=0,row=0)





# #msg box demo
# def clicked():

#     # messagebox.showinfo('Message title test', 'Message content benjamin')
#     # messagebox.showwarning('Message title', 'Message content')  #shows warning message
#     # messagebox.showerror('Message title', 'Message content')    #shows error message
#     res = messagebox.askquestion('Message title','Message content')
#     print(res)
#     # messagebox.askyesnocancel('Message title','Message content')

# btn = Button(window,text='Click here', command=clicked)

# btn.grid(column=0,row=0)


#scroll box create
# txt = scrolledtext.ScrolledText(window,width=40,height=10)
# txt.insert(INSERT,'You text goes here')
# txt.delete(1.0,END)
# txt.grid(column=0,row=0)




# #radio button

# selected = IntVar() #selected variable

# rad1 = Radiobutton(window,text='First', value=1, variable=selected)

# rad2 = Radiobutton(window,text='Second', value=2, variable=selected)

# rad3 = Radiobutton(window,text='Third', value=3, variable=selected)

# def clicked():

#    print(selected.get())

# btn = Button(window, text="Click Me", command=clicked)

# rad1.grid(column=0, row=0)

# rad2.grid(column=1, row=0)

# rad3.grid(column=2, row=0)

# btn.grid(column=3, row=0)



# #check button

# chk1_state = IntVar()

# chk1_state.set(False) #set check state

# chk= Checkbutton(window, text='Choose', var=chk1_state)

# chk.grid(column=0, row=0)

#Combo box
combo1 = Combobox(window)
combo1['values']= (1, 2, 3, 4, 5, "Text")

combo1.current(1) #set the selected item

combo1.grid(column=0, row=0)

combo2 = Combobox(window)
combo2['values']= (1, 12, 3, 4, 5, "Text")

combo2.current(1) #set the selected item

combo2.grid(column=0, row=1)


# lb1 = Label(window, text ="Hello") #, font=("Arial Bold", 50
# lb1.grid(column=0,row=0)
# txt = Entry(window,width=20) #, state='disabled'
# txt.focus()

# txt.grid(column=1, row=0)

# def clicked():
#     res = "Welcome to "+txt.get()
#     lb1.configure(text=res)

# btn = Button(window, text="Click Me", command=clicked)
# btn.grid(column=2, row=0)


window.mainloop()


