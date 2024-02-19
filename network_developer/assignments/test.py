import tkinter as tk

def toggle():
    if var.get() == 1:
        check_button.configure(bg="green")
    else:
        check_button.configure(bg="SystemButtonFace")  # Set it back to default

window = tk.Tk()
window.title("Check Button with Green Color")

var = tk.IntVar()

check_button = tk.Checkbutton(window, text="Check", variable=var, command=toggle)
check_button.pack(padx=10, pady=10)

window.mainloop()
