#-*-coding:utf-8;-*-
#qpy:3
#qpy:console
from json import dumps
from socket import socket,AF_INET,SOCK_STREAM
from androidhelper import Android
ad=Android()
soc=socket(AF_INET,SOCK_STREAM)
soc.bind(("0.0.0.0",1864))
soc.listen(1)
cli,add=soc.accept()
ad.makeToast("Location server : Successfully connected to the client.")
while True:
    rea=""
    while rea=="":
        rea=cli.recv(8).decode("utf-8").strip("\n")
    if rea=="read":
        cli.send((dumps(ad.readLocation().result)+"\n").encode("utf-8"))
    elif rea=="open":
        ad.startLocating()
        print("Start locating.")
    elif rea=="close":
        ad.stopLocating()
        print("Stop locating.")
