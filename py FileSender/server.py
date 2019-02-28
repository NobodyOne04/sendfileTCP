from tkinter import Tk
from tkinter.filedialog import askopenfilename
import socket
import sys
import os
if __name__ == '__main__':
    port=9090
    host=socket.gethostbyname(socket.gethostname())
    print("this is server ip : "+str(host))
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.bind(('', port))
    sock.listen(3)
    print ("[SERVER STARTED]")
    Tk().withdraw()
    filename = askopenfilename()
    conn,addr=sock.accept()
    connection_check=conn.recv(1024)
    print(connection_check.decode('UTF-8'))
    conn.send(("Hi "+str(addr)+" from server").encode('UTF-8'))
    server=True
    with open(filename,'wb') as f:
        f.close()
    file=open(filename,'wb')
    size=0
    data_get=0
    data=b''
    const=sys.getsizeof(data)
    while server:
        try:
            size=int((conn.recv(1024)).decode('UTF-8'))
            print("This is file size : ",size)
            data = conn.recv(1024)
            data_get=data_get+sys.getsizeof(data)-const
            print("Download was started")
            while(data):
                file.write(data)
                conn.settimeout(10)
                if size>data_get:
                    data=conn.recv(1024)
                    data_get=data_get+sys.getsizeof(data)-const
                else:
                    break
            print("Download has been completed")
            file.close()
            if os.path.getsize(filename)!=size:
                print("Error : file was loaded incorrect")
                print("This is the data that was received from the client : ",data_get)
                print("This is the size of the file on the server : ",os.path.getsize(filename))
                print("This is the original size : ",size)
                ask=input("Delete file ? (y/n) ")
                if ask=="y":
                    os.remove(filename)
                raise SystemExit(os.path.getsize(filename)-size)
            else:
                print("File has loaded correct")
                conn.send("File has load correct".encode("utf-8"))
        except :
            server=False
            print("[SERVER WAS SHUT DOWN]")
    sock.close()
