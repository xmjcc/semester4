import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class Application(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Simple GUI Application")
        self.geometry("400x300")
        self.initialize_form()

    def initialize_form(self):
        frame = ttk.Frame(self, padding="10", relief="sunken")
        frame.pack(fill="both", expand=True)

        ttk.Label(frame, text="Data Entry Form", font=("Arial", 14)).grid(row=0, columnspan=2, pady=(0,10))

        ttk.Label(frame, text="Full Name:").grid(row=1, column=0, sticky="e")
        self.name_entry = ttk.Entry(frame)
        self.name_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(frame, text="Residency:").grid(row=2, column=0, sticky="e")
        self.residency_var = tk.StringVar()
        self.residency_var.set("dom")
        ttk.Radiobutton(frame, text="Domestic", variable=self.residency_var, value="dom").grid(row=2, column=1, padx=5, pady=5, sticky="w")
        ttk.Radiobutton(frame, text="International", variable=self.residency_var, value="intl").grid(row=2, column=1, padx=5, pady=5, sticky="e")

        ttk.Label(frame, text="Program:").grid(row=3, column=0, sticky="e")
        self.program_combo = ttk.Combobox(frame, values=["AI", "Gaming", "Health", "Software"])
        self.program_combo.grid(row=3, column=1, padx=5, pady=5)

        ttk.Label(frame, text="Courses:").grid(row=4, column=0, sticky="ne")
        self.comp100_var = tk.StringVar()
        ttk.Checkbutton(frame, text="Programming I", variable=self.comp100_var, onvalue="COMP100", offvalue='').grid(row=4, column=1, sticky="w")
        self.comp213_var = tk.StringVar()
        ttk.Checkbutton(frame, text="Web Page Design", variable=self.comp213_var, onvalue="COMP213", offvalue='').grid(row=5, column=1, sticky="w")
        self.comp120_var = tk.StringVar()
        ttk.Checkbutton(frame, text="Software Engineering", variable=self.comp120_var, onvalue="COMP120", offvalue='').grid(row=6, column=1, sticky="w")

        ttk.Button(frame, text="Reset", command=self.reset_form).grid(row=7, column=0, pady=10)
        ttk.Button(frame, text="OK", command=self.show_info).grid(row=7, column=1, pady=10)
        ttk.Button(frame, text="Exit", command=self.quit).grid(row=8, columnspan=2, pady=(0,10))

    def reset_form(self):
        self.name_entry.delete(0, tk.END)
        self.residency_var.set("dom")
        self.program_combo.set("")
        self.comp100_var.set("")
        self.comp213_var.set("")
        self.comp120_var.set("")

    def show_info(self):
        info = f"Full Name: {self.name_entry.get()}\nResidency: {self.residency_var.get()}\nProgram: {self.program_combo.get()}\nCourses: {', '.join(filter(None, [self.comp100_var.get(), self.comp213_var.get(), self.comp120_var.get()]))}"
        messagebox.showinfo("Information", info)

app = Application()
app.mainloop()




        


