from time import sleep
import serial
import socketserver

server = socketserver.socketServer()
returnedData = server.create()
while True:
	print returnedData
	sleep(1)
