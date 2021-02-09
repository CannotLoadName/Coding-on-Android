#-*-coding:utf-8;-*-
#qpy:3
#qpy:console
from socket import socket,AF_INET,SOCK_STREAM
from bottle import hook,response,route,run
def getdat(typ):
    soc=socket(AF_INET,SOCK_STREAM)
    soc.connect(("localhost",1860))
    soc.send((typ+"\n").encode("utf-8"))
    got=soc.recv(4096)
    soc.close()
    return got.decode("utf-8").strip("\n")
@hook("after_request")
def admit():
    response.headers["Access-Control-Allow-Origin"]="*"
    response.headers["Access-Control-Allow-Headers"]="*"
@route("/location")
def answer0():
    return getdat("loc")
@route("/acceleration")
def answer1():
    return getdat("acc")
@route("/magnet")
def answer2():
    return getdat("mag")
@route("/orientation")
def answer3():
    return getdat("ori")
@route("/gyration")
def answer4():
    return getdat("gyr")
@route("/light")
def answer5():
    return getdat("lig")
@route("/proximity")
def answer6():
    return getdat("pro")
@route("/gravity")
def answer7():
    return getdat("gra")
@route("/linear_acceleration")
def answer8():
    return getdat("lin")
@route("/rotation")
def answer9():
    return getdat("rot")
@route("/step")
def answerA():
    return getdat("ste")
@route("/sensors")
def answerB():
    return getdat("sen")
@route("/all_data")
def answerC():
    return getdat("all")
@route("/")
def answerD():
    return getdat("all")
run(host="0.0.0.0",port=4080)
