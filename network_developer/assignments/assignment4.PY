from tkinter import *
from tkinter.ttk import *
import tkinter as tk
import tkinter


window = tk.Tk()
window.title("Centennial College")
window.geometry('420x270+20+20')
window.configure(background='light green')
lb0 = Label(window, text="ICET Student Survey",font=("Arial", 16, "bold italic"))
lb0.configure(background='light green')
lb0.grid(column=1, row=0, pady=(10,10))


lbl = Label(window, text="Full Name:")
lbl.grid(column=0, row=1, padx=(0,60))
lbl.configure(background='light green')

txt1 = Entry(window, width=30)


txt1.insert(0, "Narendra Pershad")
txt1.grid(column=1, row=1,sticky='w')

lb2 = tk.Label(window, text ='Residency')
# lb2 = Label(window, text="Residency:")
lb2.grid(column=0, row=2, padx=(0,60))
lb2.configure(bg="light green")



selected = tk.BooleanVar()
selected.set(True)
rad1 = tk.Radiobutton(window,text='Domestic', value=True, variable=selected, bg='light green')

rad1.grid(column=1, row=2,padx=0, sticky='w')
rad2 = tk.Radiobutton(window,text='International', value=False, variable=selected, bg='light green')
rad2.grid(column=1, row=3,padx=0,sticky='w')

# line 4 comboxbox

lb3 = Label(window, text="Program:")
lb3.grid(column=0, row=4, padx=(0,60))
lb3.configure(background='light green')

combo1 = Combobox(window)
combo1['values']= ('AI', 'Mathematics', 'Musics', 'Gaming')

combo1.current(1) #set the selected item

combo1.grid(column=1, row=4,sticky='w', pady=(5,5))
combo1.configure(background='light green')


# check box
lb3 = Label(window, text="Courses:")
lb3.grid(column=0, row=5, padx=(0,60))
lb3.configure(background='light green')

# labelchk = tk.Label(window, text="Check", bg="green")
# labelchk.grid(column=1, row=5,sticky='w')


chk1_state = BooleanVar()

chk1_state.set(True) #set check state

chk1 = tk.Checkbutton(window, text='Programming1', variable=chk1_state, bg='light green' )

chk1.grid(column=1, row=5,sticky='w')

chk2_state = BooleanVar()

chk2_state.set(False) #set check state

chk2 = tk.Checkbutton(window, text='Web Page Design', variable=chk2_state, bg='light green' )

chk2.grid(column=1, row=6,sticky='w')

chk3_state = BooleanVar()

chk3_state.set(False) #set check state

chk3 = tk.Checkbutton(window, text='Software Engineering', variable=chk3_state, bg='light green' )

chk3.grid(column=1, row=7,sticky='w')

ok = Button(window, text='Ok',width=17)
ok.place(relx=0.295, rely=0.85)

Reset = Button(window, text='Reset', width=17, )
Reset.place(relx=0.02, rely=0.85)

Exit = Button(window, text='Exit',width=17)
# Exit.grid(column=2, row=8, columnspan=1, padx=(0, 5) )
Exit.place(relx=0.57, rely=0.85)
       
       
        
window.mainloop()