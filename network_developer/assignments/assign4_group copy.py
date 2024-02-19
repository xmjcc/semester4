import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
 
class StudentSurveyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Centennial College")
        self.geometry('420x360+10+10')
        self.configure(background='light green')
 
        # Frame to contain widgets
        self.frame = ttk.Frame(self, padding="10", relief="ridge")
        self.frame.grid(column=0, row=0, padx=5, pady=5, sticky="nsew")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
 
        # Title label
        self.lb0 = ttk.Label(self.frame, text="ICET Student Survey", font=("Arial", 16, "bold italic"))
        self.lb0.grid(column=1, row=0, pady=(10,10), columnspan=2)
 
        # Full Name label and entry
        self.lbl = ttk.Label(self.frame, text="Full Name:")
        self.lbl.grid(column=0, row=1, sticky=tk.W)
        self.txt1 = ttk.Entry(self.frame, width=30)
        self.txt1.insert(0, "Narendra Pershad")
        self.txt1.grid(column=1, row=1, sticky='ew')
 
        # Residency radio buttons
        self.lb2 = ttk.Label(self.frame, text='Residency')
        self.lb2.grid(column=0, row=2, sticky=tk.W)
        self.selected_residency = tk.StringVar(value="dom")
        self.rad1 = ttk.Radiobutton(self.frame, text='Domestic', value="dom", variable=self.selected_residency)
        self.rad1.grid(column=1, row=2, sticky=tk.W)
        self.rad2 = ttk.Radiobutton(self.frame, text='International', value="intl", variable=self.selected_residency)
        self.rad2.grid(column=1, row=3, sticky=tk.W)
 
        # Program combobox
        self.lb3 = ttk.Label(self.frame, text="Program:")
        self.lb3.grid(column=0, row=4, sticky=tk.W)
        self.combo1 = ttk.Combobox(self.frame, values=('AI', 'Health','Software','Mathematics', 'Musics', 'Gaming'), state="readonly")
        self.combo1.current(1)  # Set the selected item
        self.combo1.grid(column=1, row=4, sticky='ew', pady=(5,5))
 
        # Courses checkboxes
        self.lb4 = ttk.Label(self.frame, text="Courses:")
        self.lb4.grid(column=0, row=5, sticky=tk.W)
        self.chk1_state = tk.BooleanVar(value=True)
        self.chk1 = ttk.Checkbutton(self.frame, text='Programming I', variable=self.chk1_state)
        self.chk1.grid(column=1, row=5, sticky=tk.W)
        self.chk2_state = tk.BooleanVar(value=False)
        self.chk2 = ttk.Checkbutton(self.frame, text='Web Page Design', variable=self.chk2_state)
        self.chk2.grid(column=1, row=6, sticky=tk.W)
        self.chk3_state = tk.BooleanVar(value=False)
        self.chk3 = ttk.Checkbutton(self.frame, text='Software Engineering', variable=self.chk3_state)
        self.chk3.grid(column=1, row=7, sticky=tk.W)
 
        # Ok, Reset, and Exit buttons
        ok = ttk.Button(self, text='Ok',width=17, command=self.show_info)
        ok.place(relx=0.32, rely=0.9)

        Reset = ttk.Button(self, text='Reset', width=17, command=self.reset_form)
        Reset.place(relx=0.05, rely=0.9)

        Exit = ttk.Button(self, text='Exit',width=17,command=self.quit)
        # Exit.grid(column=2, row=8, columnspan=1, padx=(0, 5) )
        Exit.place(relx=0.6, rely=0.9)
       





   
 
        self.make_responsive()
 
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
        self.selected_residency.set("dom")
        self.combo1.current(1)
        self.chk1_state.set(True)
        self.chk2_state.set(False)
        self.chk3_state.set(False)
 
if __name__ == "__main__":
    app = StudentSurveyApp()
    app.mainloop()