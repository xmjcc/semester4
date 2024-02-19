 
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
 
class StudentSurveyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        # Set window title and size
        self.title("Centennial College")
        self.geometry('420x270+20+20')
        # Set the background of the main window to gray for the border effect
        self.configure(background='light grey')
 
        # Create and configure style for Radiobuttons
        style = ttk.Style(self)
        style.configure('TRadiobutton', background='light green')
        style.configure('TCheckbutton', background='light green')  # Configure style for Checkbuttons
 
 
        # Create an inner frame with light green background to contain widgets
        # Padding around this frame creates the outer gray border effect
        self.frame = tk.Frame(self, bg='light green', padx=10, pady=10)
        self.frame.grid(column=0, row=0, padx=5, pady=5, sticky="nsew")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
       
       
        self.course_codes = {
            'Programming I': '',
            'Web Page Design': '',
            'Software Engineering': '',
        }
        # Title label for the survey
        lb0 = ttk.Label(self.frame, text="ICET Student Survey", font=("Arial", 16, "bold italic"))
        lb0.configure(background='light green')
        lb0.grid(column=1, row=0,  pady=(10,10))
 
        # Label and entry for full name
        lbl = ttk.Label(self.frame, text="Full Name:")
        lbl.grid(column=0, row=1, padx=(0,60))
        lbl.configure(background='light green')
        self.txt1 = ttk.Entry(self.frame, width=30)
        self.txt1.insert(0, "Narendra Pershad")
        self.txt1.grid(column=1, row=1, sticky='w')
 
        # Residency label and radio buttons for selection
        lb2 = ttk.Label(self.frame, text='Residency')
        lb2.grid(column=0, row=2, padx=(0,60))
        lb2.configure(background="light green")
        self.selected_residency = tk.StringVar()
        self.selected_residency.set('Dom')
        rad1 = ttk.Radiobutton(self.frame, text='Domestic', value='Dom', variable=self.selected_residency)
        rad1.grid(column=1, row=2, padx=0, sticky='w')
        rad2 = ttk.Radiobutton(self.frame, text='International', value='Intl', variable=self.selected_residency)
        rad2.grid(column=1, row=3, padx=0, sticky='w')
 
        # Program selection combobox
        lb3 = ttk.Label(self.frame, text="Program:")
        lb3.grid(column=0, row=4, padx=(0,60))
        lb3.configure(background='light green')
        self.combo1 = ttk.Combobox(self.frame)
        self.combo1['values'] = ('AI', 'Health', 'Mathematics', 'Musics', 'Gaming')
        self.combo1.current(1)  # Pre-select the second item
        self.combo1.grid(column=1, row=4, sticky='w', pady=(5,5))
 
        # Checkboxes for course selection
        lb4 = ttk.Label(self.frame, text="Courses:")
        lb4.grid(column=0, row=5, padx=(0,60))
        lb4.configure(background='light green')


        self.chk1_state =tk.StringVar()

        self.chk1_state.set('COMP100') #set check state
        # # self.chk1_state = tk.BooleanVar(value=True)
        # self.chk1_state = tk.BooleanVar()
        # self.chk1_state.set(True)  # Pre-check the Programming I course
        chk1 = ttk.Checkbutton(self.frame, text='Programming I', variable=self.chk1_state, onvalue='COMP100', offvalue='')
        chk1.grid(column=1, row=5, sticky='w')
 
        self.chk2_state =tk.StringVar()
        self.chk2_state.set('') #set check state
        chk2 = ttk.Checkbutton(self.frame, text='Web Page Design', variable=self.chk2_state, onvalue='COMP213', offvalue='')
        chk2.grid(column=1, row=6, sticky='w')
 
        self.chk3_state =tk.StringVar()
        self.chk3_state.set('') #set check state
        chk3 = ttk.Checkbutton(self.frame, text='Software Engineering', variable=self.chk3_state, onvalue='COMP120', offvalue='' )
        chk3.grid(column=1, row=7, sticky='w')
 
        
        ok = ttk.Button(self.frame, text='Ok', width=17, command=self.show_info)
        ok.place(relx=0.33, rely=0.87)
 
        Reset = ttk.Button(self.frame, text='Reset', width=17, command=self.reset_form)
        Reset.place(relx=0.02, rely=0.87)
 
        Exit = ttk.Button(self.frame, text='Exit', width=17, command=self.quit)
        Exit.place(relx=0.65, rely=0.87)
 
 
 
 
 
    def show_info(self):
        # Update the handling for course selection based on checkbox states
        self.course_codes['Programming I'] = 'COMP100' if self.chk1_state.get() else ''
        self.course_codes['Web Page Design'] = 'COMP213' if self.chk2_state.get() else ''
        self.course_codes['Software Engineering'] = 'COMP120' if self.chk3_state.get() else ''
 
        # Construct the courses info string based on selected courses
        courses_info = ', '.join([code for code in self.course_codes.values() if code])
 
        # Update the message to include courses_info
        # Gather and display the information provided by the user
        info = (f"Full Name: {self.txt1.get()}\n"
                f"Residency: {'Domestic' if self.selected_residency.get() == 'Dom' else 'International'}\n"
                f"Program: {self.combo1.get()}\n"
                f"Courses: {courses_info if courses_info else 'None'}")
        messagebox.showinfo("Form Data", info)
 


    def reset_form(self):
        # Reset the form to its initial state
        self.txt1.delete(0, tk.END)
        self.txt1.insert(0, "Narendra Pershad")
        self.selected_residency.set("Dom")
        self.combo1.current(1)  # Reset to the second item
        self.chk1_state.set('COMP100')
        self.chk2_state.set('')
        self.chk3_state.set('')
 
if __name__ == "__main__":
    app = StudentSurveyApp()
    app.mainloop()
 
