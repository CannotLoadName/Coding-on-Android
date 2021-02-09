#-*-coding:utf-8;-*-
#qpy:3
#qpy:console
from time import time,sleep
from json import loads,dumps
from socket import socket,AF_INET,SOCK_STREAM
from threading import Thread
senname=["acceleration","magnet","orientation","gyration","light","proximity","gravity","linear_acceleration","rotation","step"]
sensign=["acc","mag","ori","gyr","lig","pro","gra","lin","rot","ste"]
tcploc=socket(AF_INET,SOCK_STREAM)
tcpsen=socket(AF_INET,SOCK_STREAM)
try:
    tcploc.connect(("localhost",1864))
except:
    locexist=False
else:
    locexist=True
try:
    tcpsen.connect(("localhost",1862))
except:
    senexist=False
else:
    senexist=True
if senexist:
    sentime=[0.0]*10
    def opensen(typ):
        global tcpsen
        tcpsen.send(("open\n%s\n"%(typ)).encode("utf-8"))
    def readsen(typ):
        global tcpsen
        tcpsen.send(("read\n%s\n"%(typ)).encode("utf-8"))
        return loads(tcpsen.recv(256).decode("utf-8").strip("\n"))
    def closesen(typ):
        global tcpsen
        tcpsen.send(("close\n%s\n"%(typ)).encode("utf-8"))
if locexist:
    loctime=0.0
    def openloc():
        global tcploc
        tcploc.send("open\n".encode("utf-8"))
    def readloc():
        global tcploc
        tcploc.send("read\n".encode("utf-8"))
        return loads(tcploc.recv(1024).decode("utf-8").strip("\n"))
    def closeloc():
        global tcploc
        tcploc.send("close\n".encode("utf-8"))
cando=True
def killer():
    global sensign,cando,senexist,locexist
    if senexist:
        global sentime
    if locexist:
        global loctime
    while True:
        if cando and senexist:
            for t in range(0,10):
                if sentime[t]!=0.0 and time()>sentime[t]:
                    closesen(sensign[t])
                    sentime[t]=0.0
        if cando and locexist:
            if loctime!=0.0 and time()>loctime:
                closeloc()
                loctime=0.0
Thread(target=killer).start()
server=socket(AF_INET,SOCK_STREAM)
server.bind(("0.0.0.0",1860))
server.listen(4096)
while True:
    client,address=server.accept()
    cando=False
    req=client.recv(8).decode("utf-8").strip("\n")
    print("Connected to : %s:%d"%address)
    print("Read : %s"%(req))
    res=dict()
    if req=="all":
        lpau=False
        spau=False
        if locexist:
            if loctime==0.0:
                openloc()
                lpau=True
        if senexist:
            for t in range(0,10):
                if sentime[t]==0.0:
                    opensen(sensign[t])
                    spau=True
        if lpau:
            sleep(3)
        elif spau:
            sleep(0.5)
        if locexist:
            res["location"]=readloc()
            loctime=time()+30
        if senexist:
            for t in range(0,10):
                res[senname[t]]=readsen(sensign[t])
            sentime=[time()+15]*10
    elif req=="loc":
        if locexist:
            if loctime==0.0:
                openloc()
                sleep(3)
            res["location"]=readloc()
            loctime=time()+30
    elif req=="sen":
        if senexist:
            spau=False
            for t in range(0,10):
                if sentime[t]==0.0:
                    opensen(sensign[t])
                    spau=True
            if spau:
                sleep(0.5)
            for t in range(0,10):
                res[senname[t]]=readsen(sensign[t])
            sentime=[time()+15]*10
    else:
        for t in range(0,10):
            if req==sensign[t]:
                if senexist:
                    if sentime[t]==0.0:
                        opensen(sensign[t])
                        sleep(0.5)
                    res[senname[t]]=readsen(sensign[t])
                    sentime[t]=time()+15
                break
    resp=dumps(res)
    client.send((resp+"\n").encode("utf-8"))
    print("Written : %s"%(resp))
    client.close()
    cando=True
