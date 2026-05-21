#create a GUI having quiz of 3 to 5 questions after submitting it should display score

from tkinter import Tk, Label, Button, Radiobutton, IntVar

w=Tk()
w.title('MCQS')
w.iconbitmap('icon.ico')
w.geometry('500x500')

def check_answer():
    if v.get() == 2:
        L10.grid(row=6, column=0, padx=20, pady=10)
    else:
        L20.grid(row=6, column=0, padx=20, pady=10)
    
v1=IntVar() 

#1st question
L1=Label(w,text='Best Movie?', font=('cambria',20))
L1.grid(row=0, column=0, padx=20, pady=20, sticky='W')

R1=Radiobutton(w,text='Lagan Special',font=('Cambria',20), variable=v1, value=1)
R1.grid(row=1, column=0, padx=20, pady=20, sticky='W')

R2=Radiobutton(w,text='Gadar 2',font=('Cambria',20), variable=v1, value=2)
R2.grid(row=2, column=0, padx=20, pady=20, sticky='W')

R3=Radiobutton(w,text='Ashiqui 2',font=('Cambria',20), variable=v1, value=3)
R3.grid(row=3, column=0, padx=20, pady=20, sticky='W')

R4=Radiobutton(w,text='Hum sath sath hai',font=('cambria',20), variable=v1, value=4)
R4.grid(row=4, column=0, padx=20, pady=20, sticky='W')

L10=Label(w,text='your answer is correct',font=('cambria',20))
L20=Label(w,text='your answer is wrong',font=('cambria',20))

#2nd question
L2=Label(w,text='prime minister?', font=('cambria',20))
L2.grid(row=0, column=0, padx=20, pady=20, sticky='W')

R5=Radiobutton(w,text='Rahul Gandhi',font=('Cambria',20), variable=v, value=5)
R5.grid(row=1, column=0, padx=20, pady=20, sticky='W')

R6=Radiobutton(w,text='Narendra Modi',font=('Cambria',20), variable=v, value=6)
R6.grid(row=2, column=0, padx=20, pady=20, sticky='W')

R7=Radiobutton(w,text='Kejriwal',font=('Cambria',20), variable=v, value=7)
R7.grid(row=3, column=0, padx=20, pady=20, sticky='W')

R8=Radiobutton(w,text='Mamta Banerji',font=('cambria',20), variable=v, value=8)
R8.grid(row=4, column=0, padx=20, pady=20, sticky='W')

L30=Label(w,text='your answer is correct',font=('cambria',20))
L40=Label(w,text='your answer is wrong',font=('cambria',20))

#3rd question
L3=Label(w,text='Best heroine?', font=('cambria',20))
L3.grid(row=0, column=0, padx=20, pady=20, sticky='W')

R9=Radiobutton(w,text='Ananya Pandey',font=('Cambria',20), variable=v, value=9)
R9.grid(row=1, column=0, padx=20, pady=20, sticky='W')

R10=Radiobutton(w,text='Tara Sutariya',font=('Cambria',20), variable=v, value=10)
R10.grid(row=2, column=0, padx=20, pady=20, sticky='W')

R11=Radiobutton(w,text='Janvi Kapoor',font=('Cambria',20), variable=v, value=11)
R11.grid(row=3, column=0, padx=20, pady=20, sticky='W')

R12=Radiobutton(w,text='None of the above',font=('cambria',20), variable=v, value=12)
R12.grid(row=4, column=0, padx=20, pady=20, sticky='W')


B=Button(w,text='submit',font=('cambria',20), command=check_answer)
B.grid(row=5, column=0, padx=20, pady=20)

L50=Label(w,text='your answer is correct',font=('cambria',20))
L60=Label(w,text='your answer is wrong',font=('cambria',20))


w.mainloop()
