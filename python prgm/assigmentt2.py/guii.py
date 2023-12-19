# from tkinter import*

# root=Tk()
# root.title("my window")
# root.geometry('250x200')
# root.mainloop()

# LABEL
# root =Tk()
# root.title("window")
# root.geometry('300x250')
# lab=Label(root,text="we are python programers")
# lab.pack()
# root.mainloop()

# BUTTON
# root=Tk()
# root.title("welcome to python")
# def clicked():
#     print("i am clicked")
# btn=Button(root,text="click me",command=clicked,background='green')
# btn.pack()
# root.geometry('350x200')
# lab=Label(root,text="WELCOME TO PYTHON PROGRAMMERS",background='red',fg='blue')
# lab.pack()
# root.mainloop()

# PLACE LAYOT
# root=Tk()
# lab=Label(root,text="My World",bg='red',fg='green')
# lab.place(x=0,y=30)
# lab=Label(root,text="Python Programmer",bg='yellow',fg='black')
# lab.place(x=90,y=120)
# root.geometry("350x200")
# root.mainloop()

# font style

# from tkinter import *
# root = Tk()
# root.title("Welcome to Python Lobby")
# root.geometry('250x200')
# name = "We are Python Lobby-ian"
# lbl = Label(root, text = name, font=("Helvetica", 50), fg = 'green' , bg='blue')
# lbl.pack()
# root.mainloop()

# Grid
# root=Tk()
# root.title("python")
# lab=Label(root,text="red zone",bg='red',fg='white')
# lab.grid(row=0,column=0)
# lab=Label(root,text='green glossy',bg='light green',fg='red')
# lab.grid(row=2,column=2)
# root.geometry("350x250")
# root.mainloop()

# Checkbutton
# from tkinter import *
# root=Tk()
# root.title("welcome")
# lab=Label(root,text='python',font='60')
# lab.pack()
# checkbox1=IntVar()
# checkbox2=IntVar()
# button0=Checkbutton(root,text='learning',variable=checkbox1,onvalue=1,offvalue=0,height=3,width=12)
# button1=Checkbutton(root,text='tutorial',variable=checkbox2,onvalue=1,offvalue=0,height=3,width=12)
# button0.pack()
# button1.pack()
# root.geometry('340x400')
# mainloop()

# Image

# from tkinter import *
# from PIL import Image, ImageTk
# root = Tk()
# label = Label(root, text="This is Image")
# label.place(x=50,y=100)
# image = Image.open("C:/Users/DELL/Pictures/bird.jpeg")

# tk_image = ImageTk.PhotoImage(image)
# label_image = Label(root, image=tk_image,width=400, height=400)
# label_image.place(x=100,y=200)
# root.geometry("600x440")
# root.title("PythonLobby.com")
# root.mainloop()


# exmple3
from tkinter import *
from PIL import Image,ImageTk
root=Tk()
root.configure(bg="black")
root.geometry("500x450")
def click_me_for_courier():
    print("click_me_for_courier")
lab1=Label(root,text="Username",font=("Helvetica", "20"),fg='#EEC900',bg='black')
lab1.place(x=25,y=140)
entry=Entry(root,bg='black')
entry.place(x=25,y=200)
lab2=Label(root,text="Password",font=("Helvetica", "20"),fg='#EEC900',bg='black')
lab2.place(x=25,y=250)
entry=Entry(root,bg='black')
entry.place(x=25,y=300)
btn=Button(root,text="Sign In",command=click_me_for_courier,bg='black',fg='#EEC900')
btn.place(x=25,y=400)
lab3=Label(root,text="GUCCI STORE",font=("Times", "25", "bold italic"),fg='#EEC900',bg='black')
lab3.pack()
image=Image.open("C:/Users/DELL/Pictures/guuci.jpeg")
image1=ImageTk.PhotoImage(image)
lab_img=Label(root,image=image1,width=530,height=560)
lab_img.place(x=700,y=250)
root.geometry('300x400')
root.mainloop()


# from tkinter import *
# from PIL import Image,ImageTk
# root=Tk()
# label=Label(root,text='image')
# label.pack()
# root.configure(bg="red")
# image=Image.open("C:/Users/DELL/Pictures/santa.jpg")
# image1=ImageTk.PhotoImage(image)
# lab_img=Label(root,image=image1,)
# lab_img.pack()
# root.geometry('500x400')
# root.title("welcome")
# root.mainloop()


# EXAMPLE
# root=Tk()
# root.title("python")
# root.geometry('300x250')
# lab=Label(root,text='Username')
# lab.grid(row=0,column=0)
# Entry(root)
# lab.grid(row=0,column=1)
# lab.pack()
# root.mainloop()
# INSTAGRAM

# from tkinter import *
# root=Tk()
# root.title("window")
# root.geometry("500x500")
# root.configure(bg='pink')
# lab=Label(root,text='INSTAGRAM',bg='pink',fg='black',font=("Times", "24", "bold italic"))
# lab.place(x=700,y=50)
# lab1=Label(root,text='username',font=("Helvetica", "16"),bg='dark blue',fg='white')
# lab1.place(x=25,y=140)
# entry=Entry(root)
# entry.place(x=25,y=200)
# lab2=Label(root,text='password',font=("Helvetica", "16"),bg='dark blue',fg='white')
# lab2.place(x=25,y=250)
# entry=Entry(root)
# entry.place(x=25,y=300)
# btn=Button(root,text='Sign In',command='clicked',bg='light green',fg='black')
# btn.place(x=25,y=400)
# root.mainloop()

# FACEBOOK

# from tkinter import *
# root=Tk()
# root.title("window")
# root.geometry('600x600')
# root.configure(bg='sky blue')
# lab=Label(root,text='FACEBOOK',bg='blue',fg='black',font=("Helvetica", "16"))
# lab.place(x=650,y=50)
# lab1=Label(root,text='Username',font=("Times", "16", "bold italic"),bg='sky blue',fg='black')
# lab1.place(x=25,y=140)
# entry=Entry(root)
# entry.place(x=25,y=200)
# lab2=Label(root,text='password',font=("Times", "16", "bold italic"),bg='sky blue',fg='black')
# lab2.place(x=25,y=250)
# entry=Entry(root)
# entry.place(x=25,y=300)
# btn=Button(root,text='Sign In',command='clicked',bg='blue',fg='black')
# btn.place(x=25,y=400)
# root.mainloop()

# checkbox example1
# from tkinter import*
# root=Tk()
# root.title('subjects')
# lab=Label(root,text='SUBJECTS OF HSS',font='60',bg='pink',fg='white')
# lab.pack()
# checkbox1=IntVar()
# checkbox2=IntVar()
# checkbox3=IntVar()
# checkbox4=IntVar()
# checkbox5=IntVar()
# button0=Checkbutton(root,text='English',variable=checkbox1,onvalue=1,offvalue=0,height=3,width=12)
# button1=Checkbutton(root,text='Hindi',variable=checkbox2,onvalue=1,offvalue=0,height=3,width=12)
# button2=Checkbutton(root,text='Maths',variable=checkbox3,onvalue=1,offvalue=0,height=3,width=12)
# button3=Checkbutton(root,text='Physics',variable=checkbox4,onvalue=1,offvalue=0,height=3,width=12)
# button4=Checkbutton(root,text='Malayalam',variable=checkbox5,onvalue=1,offvalue=0,height=3,width=12)
# button0.pack()
# button1.pack()
# button2.pack()
# button3.pack()
# button4.pack()
# root.geometry('400x350')
# root.mainloop()


