import tkinter as tk
from tkinter import messagebox, Tk
w=Tk()
w.geometry('500x500')

def submit_registration():
    name = name_entry.get()
    age = age_entry.get()
    birthdate = birthdate_entry.get()
    age_confirmed = age_confirmed_var.get()

    if not name or not age or not birthdate:
        messagebox.showerror("Error", "Please fill in all fields.")
        return

    if not age_confirmed:
        messagebox.showerror("Error", "You must confirm you are not under 18.")
        return

    messagebox.showinfo("Success", "Registration successful!")

def open_registration_form():
    registration_form = tk.Toplevel(root)
    registration_form.title("Registration Form")

    # Labels
    tk.Label(w,registration_form, text="Your Name:").grid(row=0, column=0, sticky="w")
    tk.Label(w,registration_form, text="Your Age:").grid(row=1, column=0, sticky="w")
    tk.Label(w,registration_form, text="Your Birthdate:").grid(row=2, column=0, sticky="w")
    tk.Label(w,registration_form, text="Your Address:").grid(row=2, column=0, sticky="w")


    # Entries
    global name_entry, age_entry, birthdate_entry
    name_entry = tk.Entry(registration_form)
    age_entry = tk.Entry(registration_form)
    birthdate_entry = tk.Entry(registration_form)
    name_entry.grid(row=0, column=1)
    age_entry.grid(row=1, column=1)
    birthdate_entry.grid(row=2, column=1)

    # Checkbutton
    global age_confirmed_var
    age_confirmed_var = tk.BooleanVar()
    age_confirmed_checkbox = tk.Checkbutton(registration_form, text="You are not under 18", variable=age_confirmed_var)
    age_confirmed_checkbox.grid(row=3, columnspan=2)

    # Submit button
    submit_button = tk.Button(registration_form, text="Submit", command=submit_registration)
    submit_button.grid(row=4, columnspan=2)

def open_quiz():
    messagebox.showinfo("Quiz", "Quiz will be implemented here.")

# Main application window
root = tk.Tk()
root.title("Registration and Quiz App")

# Menu bar
menubar = tk.Menu(root)
root.config(menu=menubar)

# Registration Form menu
registration_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Registration Form", menu=registration_menu)
registration_menu.add_command(label="Open Form", command=open_registration_form)

# Quiz menu
quiz_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Quiz", menu=quiz_menu)
quiz_menu.add_command(label="Start Quiz", command=open_quiz)

root.mainloop()
