
import socket
import threading

class RequestHandler:

    def __init__(self):
        pass

    def handleRequest(self,host,port,data: str):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(5)
            s.connect((host, int(port)))
            s.sendall(data.encode())
            return s.recv(4096).decode(errors='replace')
        