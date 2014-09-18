import threading
import urllib2
import time
import pygame
from random import randint

count1 = 0
count2 = 0
pygame.init()
screen=pygame.display.set_mode((100,100),0,32)
caption = 'URL.threading - fito_segrera'
pygame.display.set_caption(caption)

urls = ["http://fii.to", "http://google.com", "http://facebook.com"]

def fetchURL():
    for i in range(len(urls)):
        data = urllib2.urlopen(urls[i]).read()
        info = urllib2.urlopen(urls[i]).info()  
        print info

thread1 = threading.Thread(target=fetchURL)
thread2 = threading.Thread(target=fetchURL)
thread1.start()
thread2.start()
while True:
    if thread1.isAlive():
        pass
    else:
        if count1 < 1:
            print "***** THREAD 1 finished after " + str(time.clock()) + " seconds *****"
            print ""
        count1+=1

    if thread2.isAlive():
        pass
    else:
        if count2 < 1:
            print "***** THREAD 2 finished after " + str(time.clock()) + " seconds *****"
            print ""
        count2+=1
    screen.fill((randint(0,255),randint(0,255),randint(0,255)))
    pygame.display.update() 
    pygame.display.flip()

