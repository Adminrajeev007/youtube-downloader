from tkinter import *
from pytube import YouTube 
from tkinter import Tk, mainloop, TOP 
from tkinter.ttk import Button 

root=Tk()
root.geometry('500x200') 
root.resizable(0,0)
root.title('youtube downloader by adminrajeev')
root.mainloop()

Label(root,text="Download youtube video", font='san-serif 14 bold').pack()
link=StringVar()
Label(root,text="paste your link here", font='san-serif 15 bold').place(x=150,y=55)
link_enter=Entry(root, width=70, textvariable=link).place(x=30,y=85)

Button(root,text='Download',font='san-serif 16 bold', bg='pink',padx=2,command="download").place(x=150,y=200)