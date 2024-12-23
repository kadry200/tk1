from tkinter import *
import datetime

def click():
    age=int(Entry1.get())
    label2["text"]=f"Output: {datetime.datetime.now().year-age}"
    
def click1():
    window.destroy()
    
window=Tk()
window.geometry("800x600")
window.config(bg="green")

label1=Label(window,text="Please Enter Your Age: ",bg="green",fg="black",font=("aria",20))
label1.place(x=0,y=10)

Entry1=Entry(window,bg="white",font=("aria",16))
Entry1.place(x=300,y=10,width=250,height=40)

Button1 = Button(window,text="Press",font=("aria",12),command=click)
Button1.place(x=570,y=20,width=150,height=30)

label2=Label(window,text="Output:  ",bg="green",fg="black",font=("aria",18))
label2.place(x=0,y=80)

Button2 = Button(window,text="Exit",font=("aria",12),command=click1)
Button2.place(x=10,y=150,width=60,height=30)

window.mainloop()