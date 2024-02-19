import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
 
class StudentSurveyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
      
 
    
        self.title("Centennial College")
        self.geometry('420x270+20+20')
        self.configure(background='light green')

        
       
       


        lb0 = ttk.Label(self, text="ICET Student Survey",font=("Arial", 16, "bold italic"))
        lb0.configure(background='light green')
        lb0.grid(column=1, row=0, pady=(10,10))

        


            # Frame to contain widgets
        # self.frame = ttk.Frame(self, padding="10", relief="ridge")
        # self.frame.grid(column=0, row=0, padx=5, pady=5, sticky="nsew")
        # self.columnconfigure(0, weight=1)
        # self.rowconfigure(0, weight=1)
 

        lbl = ttk.Label(self, text="Full Name:")
        lbl.grid(column=0, row=1, padx=(0,60))
        lbl.configure(background='light green')

        self.txt1 = ttk.Entry(self, width=30)


        self.txt1.insert(0, "Narendra Pershad")
        self.txt1.grid(column=1, row=1,sticky='w')

        lb2 = ttk.Label(self, text ='Residency')
        # lb2 = Label(self, text="Residency:")
        lb2.grid(column=0, row=2, padx=(0,60))
        lb2.configure(background="light green")

        # configure raido button style: background color to light green
        style=ttk.Style()
        style.configure('TRadiobutton', background='light green')

        self.selected_residency = tk.StringVar()
        self.selected_residency.set('Dom')
        rad1 =ttk.Radiobutton(self,text='Domestic', value='Dom', variable=self.selected_residency)
        

        rad1.grid(column=1, row=2,padx=0, sticky='w')
        rad2 = ttk.Radiobutton(self,text='International', value='Intl', variable=self.selected_residency)
        rad2.grid(column=1, row=3,padx=0,sticky='w')

        # line 4 comboxbox

        lb3 = ttk.Label(self, text="Program:")
        lb3.grid(column=0, row=4, padx=(0,60))
        lb3.configure(background='light green')

        self.combo1 = ttk.Combobox(self)
        self.combo1['values']= ('AI', 'Gaming', 'Health', 'Software')

        self.combo1.current(1) #set the selected item

        self.combo1.grid(column=1, row=4,sticky='w', pady=(5,5))
        self.combo1.configure(background='light green')


        # check box
        lb3 = ttk.Label(self, text="Courses:")
        lb3.grid(column=0, row=5, padx=(0,60))
        lb3.configure(background='light green')

        # labelchk = tk.Label(self, text="Check", background="green")
        # labelchk.grid(column=1, row=5,sticky='w')


        self.chk1_state =tk.StringVar()

        self.chk1_state.set('COMP100') #set check state
        # self.chk1_state = tk.BooleanVar(value=True)

        chk1 = tk.Checkbutton(self, text='Programming1', variable=self.chk1_state, background='light green', onvalue='COMP100', offvalue='') #, onvalue='COMP100', offvalue=''

        chk1.grid(column=1, row=5,sticky='w')

        self.chk2_state = tk.StringVar()

        self.chk2_state.set(False) #set check state

        chk2 = tk.Checkbutton(self, text='Web Page Design', variable=self.chk2_state, background='light green', onvalue='COMP213', offvalue='') #, onvalue='COMP213', offvalue='' 

        chk2.grid(column=1, row=6,sticky='w')

        self.chk3_state = tk.StringVar()

        self.chk3_state.set(False) #set check state

        chk3 = tk.Checkbutton(self, text='Software Engineering', variable=self.chk3_state, background='light green',onvalue='COMP120', offvalue='' ) #,onvalue='COMP213', offvalue='' 

        chk3.grid(column=1, row=7,sticky='w')

        ok = tk.Button(self, text='Ok',width=17, command=self.show_info)
        ok.place(relx=0.33, rely=0.85)

        Reset = tk.Button(self, text='Reset', width=17, command=self.reset_form)
        Reset.place(relx=0.02, rely=0.85)

        Exit = tk.Button(self, text='Exit',width=17,command=self.quit)
        # Exit.grid(column=2, row=8, columnspan=1, padx=(0, 5) )
        Exit.place(relx=0.65, rely=0.85)

        # self.make_responsive()
       
 
    def make_responsive(self):
        for i in range(3):  # Columns
            self.frame.columnconfigure(i, weight=1)
        for i in range(9):  # Rows
            self.frame.rowconfigure(i, weight=1)
 
    def show_info(self):
        info = f"Full Name: {self.txt1.get()}\n"
        info += f"Residency: {'Domestic' if self.selected_residency.get() == 'dom' else 'International'}\n"
        info += f"Program: {self.combo1.get()}\n"
        courses = []
        if self.chk1_state.get(): courses.append('Programming I')
        if self.chk2_state.get(): courses.append('Web Page Design')
        if self.chk3_state.get(): courses.append('Software Engineering')
        info += "Courses: " + ", ".join(courses)
        messagebox.showinfo("Form Data", info)

    def reset_form(self):
        self.txt1.delete(0, tk.END)
        self.txt1.insert(0, "Narendra Pershad")
        self.selected_residency.set("Dom")
        self.combo1.current(1)
        self.chk1_state.set('COMP100')
        self.chk2_state.set('')
        self.chk3_state.set('')
 
 
 
if __name__ == "__main__":
    app = StudentSurveyApp()
    app.mainloop()