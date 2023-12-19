from tkinter import *
from tkinter import ttk,PhotoImage
from tkinter import Tk,Entry,StringVar
root=Tk()
root.title("Simple Calculator")
operator=""
root.geometry('700x200')
root.resizable(False,True)
text_input=StringVar()
txtDisplay=Entry(root,font=("Helvetica", "16"),textvariable=text_input,bd=25,insertwidth=4,bg="powder blue",justify="right")
txtDisplay.grid(row=0,column=0,columnspan=4)
image_path="C:/Users/DELL/Pictures/calcu.png"
icon_image=PhotoImage(file=image_path)
root.iconphoto(True,icon_image)
def click_button(numbers):
    global operator
    operator=operator+str(numbers)
    text_input.set(operator)
def clear():
    global operator
    operator=""
    text_input.set("")
def Ans():
    global operator
    sumup=str(eval(operator))
    text_input.set(sumup)
    operator=""
frame=Frame(root,width=398,height=238)
frame.grid(row=1, column=0, columnspan=4)
button7=Button(frame,text=7,font=("Times", "12", "bold italic"),bg="powder blue",fg="black",width=6,bd=6,command=lambda:click_button(7))
button7.grid(row=1,column=0,columnspan=1)
button8=Button(frame,text=8,font=("Times", "12", "bold italic") ,bg="powder blue",fg="black",width=6,bd=6,command=lambda:click_button(8))
button8.grid(row=1,column=1,columnspan=1)
button9=Button(frame,text=9,font=("Times", "12", "bold italic") ,bg="powder blue",fg="black",width=6,bd=6,command=lambda:click_button(9))
button9.grid(row=1,column=2,columnspan=1)
buttonplus=Button(frame,text='+',font=("Times", "12", "bold italic") ,bg="powder blue",fg="black",width=6,bd=6,command=lambda:click_button('+'))
buttonplus.grid(row=1,column=3,columnspan=1)
button4=Button(frame,text=4,font=("Times", "12", "bold italic") ,bg="powder blue",fg="black",width=6,bd=6,command=lambda:click_button(4))
button4.grid(row=2,column=0,columnspan=1)
button5=Button(frame,text=5,font=("Times", "12", "bold italic") ,bg="powder blue",fg="black",width=6,bd=6,command=lambda:click_button(5))
button5.grid(row=2,column=1,columnspan=1)
button6=Button(frame,text=6,font=("Times", "12", "bold italic") ,bg="powder blue",fg="black",width=6,bd=6,command=lambda:click_button(6))
button6.grid(row=2,column=2,columnspan=1)
buttonminus=Button(frame,text='-',font=("Times", "12", "bold italic") ,bg="powder blue",fg="black",width=6,bd=6,command=lambda:click_button('-'))
buttonminus.grid(row=2,column=3,columnspan=1)
button1=Button(frame,text=1,font=("Times", "12", "bold italic") ,bg="powder blue",fg="black",width=6,bd=6,command=lambda:click_button(1))
button1.grid(row=3,column=0,columnspan=1)
button2=Button(frame,text=2,font=("Times", "12", "bold italic"),bg="powder blue",fg="black",width=6,bd=6,command=lambda:click_button(2))
button2.grid(row=3,column=1,columnspan=1)
button3=Button(frame,text=3,font=("Times", "12", "bold italic") ,bg="powder blue",fg="black",width=6,bd=6,command=lambda:click_button(3))
button3.grid(row=3,column=2,columnspan=1)
buttonMulti=Button(frame,text='*',font=("Times", "12", "bold italic") ,bg="powder blue",fg="black",width=6,bd=6,command=lambda:click_button('*'))
buttonMulti.grid(row=3,column=3,columnspan=1)
buttonAns=Button(frame,text='Ans',font=("Times", "12", "bold italic") ,bg="powder blue",fg="black",width=6,bd=6,command=Ans)
buttonAns.grid(row=4,column=0,columnspan=1)
buttonClear=Button(frame,text='Clear',font=("Times", "12", "bold italic") ,bg="powder blue",fg="black",width=6,bd=6,command=clear)
buttonClear.grid(row=4,column=1,columnspan=1)
button0=Button(frame,text=0,font=("Times", "12", "bold italic") ,bg="powder blue",fg="black",width=6,bd=6,command=lambda:click_button(0))
button0.grid(row=4,column=2,columnspan=1)
buttonDiv=Button(frame,text='/',font=("Times", "12", "bold italic") ,bg="powder blue",fg="black",width=6,bd=6,command=lambda:click_button('/'))
buttonDiv.grid(row=4,column=3,columnspan=1)
root.mainloop()




