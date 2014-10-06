YUNSTT
======

**Voice Recognition to remotely control an arduino YUN** 

####Sumary
For this project I created a series of python libraries. In order to control an arduino YUN remotely it is necessary to start by hosting a server within the linux chip of the YUN. In my case I use a simple python socket server and a client application on the user side (on the other side of the interaction... anywhere in the world). 

Inside the yunstt folder you will find 7 files:

1.__app.py__ is the main script. it runs the whole server-side system. It is the file that is executed when the arduino is powered. It basically calls the "socketserver.py" file and returns any incoming data.

2.__gostt.py__ Is a library that I created in order to allow voice recognition within python. It records any sound over certain threshold and uses the google voice recognition engine to upload the audio file, process it and return an array with all the possible translations. 

3.__pyduino.ino__ Is the arduino file the runs on the atmega chip of the YUN simultaneously with the server (on the linux chip of the YUN). This sketch simply listens to the serialport in an infinite loop for incoming data to trigger digital pin 13 if the data is validated first as correct.

4.__pyduino.py__ Is a library that I created for stablishing direct internal serial communication between the python server (running on the linux chip) and the arduino sketch (running on the atmega). The script takes the incoming data via sockets and validates it. If the voice command is correct, it sends a signal to the arduino.

5.__socketclient.py__ Is the main library on client-side application. It is a simple bidirectional socket that sends the interpreted data (voice recognition - sound to text) to the python server running on the arduino yun. 

6.__socketserver.py__ The library that creates the server on the arduino yun.

7.__yunstt.py__ This is the file that has to be run on the remote computer that will receive the voice commands. This scripts calls the gostt.py in order to process the voice of the user.