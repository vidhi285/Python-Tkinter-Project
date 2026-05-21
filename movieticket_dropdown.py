from tkinter import Tk, Label, Button
from tkinter.ttk import Combobox
w=Tk()
w.title('movie ticket price')
w.geometry('300x300')
w.iconbitmap('icon.ico')

def price():
    price=0
    if cb1.get()=='Monday' or cb1.get()=='Tuesday' or cb1.get()=='Wednesday':
        price=price+100
    if cb1.get()=='Thursday':
        price=price+80
    if cb1.get()=='Friday' or cb1.get()=='Saturday':
        price=price+120
    if cb1.get()=='Sunday':
        price=price+140

    if cb2.get()=='Front 5 rows':
        price=price-20
    if cb2.get()=='Middle rows':
        price=price
    if cb2.get()=='Last 2 rows':
        price=price+20
    if cb2.get()=='Premium':
        price=price+50

    L3=Label(w,text='your total price is '+str(price), font=('Times',20))
    L3.pack()
    
L1=Label(w,text='select a day' , font=('Times',20))
L1.pack()

option1=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
cb1=Combobox(w, value=option1)
cb1.pack()

L2=Label(w,text='select a seat' , font=('Times',20))
L2.pack()

option2=['Front 5 rows', 'Middle rows', 'Last 2 rows', 'Premium']
cb2=Combobox(w, value=option2)
cb2.pack()

B=Button(w,text='check price', font=('Times',20), command=price)
B.pack()

w.mainloop()



#create a GUI app using label, button, combobox to determine bill amount of restaurant
