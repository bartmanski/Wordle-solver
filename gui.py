import tkinter as tk
from tkinter import Entry,Canvas,Frame,Label,Listbox,Button,PhotoImage
import requests
root=tk.Tk()
url="http://127.0.0.1:8000/get-word?"
url2="http://127.0.0.1:8000/reset"
set_up_background=Canvas(root,height=530,width=780,bg="grey")
set_up_background.pack()

backgroung_looks=PhotoImage(file="tło.png")
background=Label(root, image=backgroung_looks)
background.place(relheight=1,relwidth=1)

frame=Frame(root,bg="yellow")
frame.place(relx=0.05,rely=0.005,relheight=0.4,relwidth=0.9)

background2=Label(frame,image=backgroung_looks)
background2.place(relwidth=1,relheight=1)

bottom_frame=Frame(root,bg="blue")
bottom_frame.place(relx=0.05,rely=0.405,relheight=0.6,relwidth=0.9)


def a(text,opcje):

    if(len(text)==5 and len(opcje)==5):
        dictionary.delete(0,dictionary.size())
        label = Label(frame, text=text, bg="yellow", font=60)
        label.place(relx=0.5,rely=0.5,relwidth=0.5,anchor='n')
        params={"word":text,"opcje":opcje}
        plik=requests.get(url,params=params)
        plik=plik.json()
        for i in range(len(plik)):
            dictionary.insert(i,plik[i])
    else:
        label = Label(frame, text="błędna liczba znaków!!!", bg="yellow", font=60)
        label.place(relx=0.5, rely=0.5, relwidth=0.5, anchor='n')

    place_for_text2.delete(0,len(text))
    place_for_text.delete(0,len(text))
def b():
    r=requests.get(url2)
place_for_text= Entry(frame,bg="white",font=60)
place_for_text.place(relx=0.2,anchor='n')


place_for_text2= Entry(frame,bg="white",font=60)
place_for_text2.place(relx=0.8,anchor='n')


button=Button(frame,text="wpisz",bg="gray",command=lambda: a(place_for_text.get(),place_for_text2.get()),width=35,height=2)
button.place(relx=0.2,rely=0.25,anchor='n')


button=Button(frame,text="reset",bg="gray",command=lambda: b(),width=35,height=2)
button.place(relx=0.8,rely=0.25,anchor='n')


dictionary=Listbox(bottom_frame,font=40,bg="grey")
dictionary.place(relwidth=1,relheight=1)
root.mainloop()
