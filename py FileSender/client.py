from tkinter import Tk
from tkinter.filedialog import askopenfilename
import socket
import threading
import os
def data_get(name,sock):
    exit=False
    while not exit:
        try:
            while True:
                data=sock.recv(1024)
                print (data.decode('UTF-8'))
        except:
            print("[SERVER WAS SHUT DOWN]")
            exit=True
if __name__ == '__main__':
    port=9090
    exit=False
    host=socket.gethostbyname(socket.gethostname())
    server_data=(str(host),port)
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        sock.connect(("127.0.0.1",port))
    except:
        print("Problem with connecting the server")
        raise SystemExit(port)
    sock.send(("Hi server"+" from "+str(host)).encode('UTF-8'))
    multistream=threading.Thread(target=data_get,args=("multistreamTread",sock))
    multistream.start()
    while not exit:
        try:
            Tk().withdraw()
            filename = askopenfilename()
            sock.send(str(os.path.getsize(filename)).encode('UTF-8'))
            print(os.path.getsize(filename))
            file=open(filename,'rb')
            post=file.read(1024)
            while (post):
                print("Sending file...")
                sock.send(post)
                post=file.read(1024)
            print("Done.")
            exit=True
        except:
            print("[SERVER CONNECTION TERMINATED]")
            if not file.closed:
                file.close()
            exit=True
    multistream.join()
    sock.close()
