# from tkinter import *
# from tkinter import messagebox
# root=Tk()
# def callback():
#     mbox=messagebox.askquestion("Delete","Well Done Great",icon="warning")
#     print("delete")
# button1=Button(root,text="Delete",command=callback)
# button1.place(x=100,y=100)
# root.geometry('400x500')
# root.title('python')
# root.mainloop()

# LIST BOX
# from tkinter import *
# from tkinter import ttk
# root=Tk()
# listbox=Listbox(root,width=45,height=15)
# listbox.place(x=100,y=100)
# listbox.insert(0,"c")
# listbox.insert(1,"java")
# listbox.insert(2,"python")
# listbox.insert(3,"c++")
# listbox.insert(4,"mysql")
# listbox.insert(5,"html")
# root.geometry('400x240')
# root.title("python")
# root.mainloop()

# CANVAS
# from tkinter import *
# root=Tk()
# canvas=Canvas(root,bg="green",width=150,height=250)
# canvas.pack()
# line=canvas.create_rectangle(70,150,140,5,fill="red")
# root.geometry('400x300')
# root.title("python")
# root.mainloop()

# RADIOBUTTON

# from tkinter import*
# root=Tk()
# root.title("python")
# val1=StringVar(root,"2")
# btn1=Radiobutton(root,text="Radio Button 1",variable=val1,value="1")
# btn1.pack()
# btn2=Radiobutton(root,text="Radio Button 2",variable=val1,value="2")
# btn2.pack()
# btn3=Radiobutton(root,text="Radio Button 3",variable=val1,value="3")
# btn3.pack()
# root.geometry('150x100')
# root.mainloop()

# FRAME
# from tkinter import *
# root=Tk()
# lab=Label(root,text='python',font="60")
# lab.pack()
# bottom_frame=Frame(root,bg="red",width=120,height=100)
# bottom_frame.place(x=100,y=150)
# top_frame=Frame(root,bg="green",width=120,height=100)
# top_frame.place(x=100,y=200)
# root.geometry("500x400")
# root.mainloop()

# PANED WINDOW
from tkinter import *
from tkinter import ttk
root=Tk()
lab=ttk.PanedWindow(root,orient=HORIZONTAL)
lab.pack(fill=BOTH,expand=True)
frame1=ttk.Frame(lab,relief=SUNKEN)
frame2=ttk.Frame(lab,relief=SUNKEN)
lab.add(frame1,weight=1)
lab.add(frame2,weight=3)
root.geometry("300x200")
root.title('python')
root.mainloop()