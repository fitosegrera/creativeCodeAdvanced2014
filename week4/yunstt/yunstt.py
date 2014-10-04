#!/usr/bin/python
# -*- coding: utf-8 -*-
##############################################
##############################################
#yunstt - voice recognition software to 
#wirelessly control an arduino yun
#created by: fito_segrera
#fii.to
##############################################
##############################################
import sys
import socketclient
import gosttpy

#main function
if __name__ == "__main__":

    if(len(sys.argv) < 3) :
        print 'Usage : python client.py hostname port'
        sys.exit()

    host = sys.argv[1]
    port = sys.argv[2]

##############################################
########### Voice Recognition ################
##############################################
speech = gosttpy.gosttpy()#Create an instance of the class gosttpy

#your google API Key. get one from: 
#https://console.developers.google.com/
apiKey = 'AIzaSyDT34UUHcNJ6lDTkj4EegMMpDn3FHaTSwY'
result = speech.voiceRecognition(apiKey);
##############################################

##############################################
############# SETUP websocket ################
##############################################
socket = socketclient.socketClient()
socket.connect(host, int(port), result)
##############################################