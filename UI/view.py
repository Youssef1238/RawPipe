from tkinter import *
import random
from services.pipelineService import send


COLORS = ["pink","black","white","red","blue","green","violet","gold"]

app = Tk()

HOST = StringVar()
PORT = StringVar()


def Send():
    # get the host and port
    host = HOST.get()
    port = int(PORT.get())
    # get the data
    data = dataEntry.get("1.0", "end-1c")
    # send them 
    send(host,port,data)



app.config(bg="gray")
app.geometry("700x600")



hostFrame = Frame(app,bg='white')
hostFrame.pack(pady=5)
hostLabel = Label(hostFrame,font=('Arial',18),text="Host: ")
hostLabel.grid(row=1,column=0)
hostEntry = Entry(hostFrame,font=('Arial',15),textvariable=HOST)
hostEntry.grid(row=1,column=2)


portFrame = Frame(app,bg='white')
portFrame.pack(pady=5)
portLabel = Label(portFrame,font=('Arial',18),text="Port: ")
portLabel.grid(row=2,column=0)
portEntry = Entry(portFrame,font=('Arial',15),textvariable=PORT)
portEntry.grid(row=2,column=2)


dataFrame = Frame(app,bg='white')
dataFrame.pack_configure(pady=5)
dataFrame.pack(pady=5)

dataLabel = Label(dataFrame,font=('Arial',18),text="Data: ")
dataLabel.grid(row=1,column=0)
dataEntry = Text(dataFrame,font=('Arial',15),height='5')
dataEntry.grid(row=2,column=2)

responseFrame = Frame(app,bg='white')
responseFrame.pack(pady=5)
responseLabel = Label(responseFrame,font=('Arial',18),text="Response: ")
responseLabel.grid(row=1,column=0)
responseEntry = Text(responseFrame,font=('Arial',15),height='5',state='disabled',border=2)
responseEntry.grid(row=2,column=2,pady=5,padx=1)

bgButton = Button(app,text="send",font=('Arial',18),border='1',command=Send)
bgButton.pack()
