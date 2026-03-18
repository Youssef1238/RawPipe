from tkinter import *
import threading
from services import RequestHandler

class View:
    
    def __init__(self,send):
        self.send = send
        self.app = Tk()
        self.app.config(bg="gray")
        self.app.geometry("700x600")

        self.HOST = StringVar()
        self.PORT = StringVar()

        self.hostFrame = Frame(self.app,bg='white')
        self.hostFrame.pack(pady=5)
        self.hostLabel = Label(self.hostFrame,font=('Arial',18),text="Host: ")
        self.hostLabel.grid(row=1,column=0)
        self.hostEntry = Entry(self.hostFrame,font=('Arial',15),textvariable=self.HOST)
        self.hostEntry.grid(row=1,column=2)

        


        self.portFrame = Frame(self.app,bg='white')
        self.portFrame.pack(pady=5)
        self.portLabel = Label(self.portFrame,font=('Arial',18),text="Port: ")
        self.portLabel.grid(row=2,column=0)
        self.portEntry = Entry(self.portFrame,font=('Arial',15),textvariable=self.PORT)
        self.portEntry.grid(row=2,column=2)


        self.dataFrame = Frame(self.app,bg='white')
        self.dataFrame.pack_configure(pady=5)
        self.dataFrame.pack(pady=5)

        self.dataLabel = Label(self.dataFrame,font=('Arial',18),text="Data: ")
        self.dataLabel.grid(row=1,column=0)
        self.dataEntry = Text(self.dataFrame,font=('Arial',15),height='5')
        self.dataEntry.grid(row=2,column=2)

        self.responseFrame = Frame(self.app,bg='white')
        self.responseFrame.pack(pady=5)
        self.responseLabel = Label(self.responseFrame,font=('Arial',18),text="Response: ")
        self.responseLabel.grid(row=1,column=0)
        self.responseEntry = Text(self.responseFrame,font=('Arial',15),height='5',border=2,wrap='word')
        self.responseEntry.grid(row=2,column=2,pady=5,padx=1)

        self.bgButton = Button(self.app,text="send",font=('Arial',18),border='1',command=self.send)
        self.bgButton.pack()

    def getRequest(self):
        host = self.HOST.get()
        port = self.PORT.get()
        data = self.dataEntry.get("1.0")
        return (host,port,data)
    
    def showResponse(self,response):
        self.responseEntry.insert('1.0',response)
















