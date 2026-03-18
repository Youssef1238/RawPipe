from UI.view import View
from services.RequestHandler import RequestHandler
from threading import Thread

def send():
    host, port, data = view.getRequest()
    res = requestHandler.handleRequest(host,port,data)
    print(res)
    view.showResponse(res)



view = View(send)
requestHandler = RequestHandler()


view.app.mainloop()