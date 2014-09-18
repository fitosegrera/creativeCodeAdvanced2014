#MULTIPLE THREADS EXAMPLE
#fito_segrera

import threading
import time
import pygame

finishColor = (0,255,0)
white = (255,255,255)
caption = 'threading - fito_segrera'

pygame.init()
screen=pygame.display.set_mode((300,150),0,32)
screen.fill((0,0,0))
pygame.display.set_caption(caption)
myfont = pygame.font.SysFont("Ubuntu Mono", 16)
labelThread1 = myfont.render("thread 1", 1, (255,255,255))
labelThread2 = myfont.render("thread 2", 1, (255,255,255))
done = myfont.render("done!", 1, (255,255,255))

def countToTen():
	for i in range(1,11):
		time.sleep(0.5)
		if i == 10:
			pygame.draw.line(screen, finishColor, (25, 50), (27.5*i, 50), 7)
		else:
			pygame.draw.line(screen, white, (25, 50), (27.5*i, 50), 7)
		screen.blit(labelThread1, (25, 30))
		pygame.display.update() 

def countToTwenty():
	for i in range(1,21):
		time.sleep(0.5)	
		if i == 1:
			pygame.draw.line(screen, white, (25, 100), (27.5*i, 100), 7)
		elif i == 20:
			pygame.draw.line(screen, finishColor, (25, 100), (13.75*i, 100), 7)
		else:
			pygame.draw.line(screen, (255,255,255), (25, 100), (13.75*i, 100), 7)
		screen.blit(labelThread2, (25, 80))
		pygame.display.update() 	

child = threading.Thread(target=countToTen)
child2 = threading.Thread(target=countToTwenty)

print "START!"
child.start()
child2.start()
while child.isAlive():
	pass
print "THREAD 1 Finished"
screen.blit(done, (245, 30))
pygame.display.update() 
while child2.isAlive():
	pass
print "THREAD 2 Finished"
screen.blit(done, (245, 80))
pygame.display.update() 

pygame.display.flip()
