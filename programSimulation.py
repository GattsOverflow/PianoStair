# sons midi
# simulation led + partition
# upgrade python3
# variables globales

import pygame, sys, time
import mido
from pygame.locals import *
import pygame.midi

def isOver(button, pos):
	if pos[0] > button.x and pos[0] < button.x + button.width:
		if pos[1] > button.y and pos[1] < button.y + button.height:
			return True
	return False

def drawAllRectangles(toColorate):
	DISPLAY.fill((255,255,255))
	
	for i in range(5):
		if i in toColorate:
			pygame.draw.rect(DISPLAY,BLUE,(25 + i * 100,150,50,50))
		else:
			pygame.draw.rect(DISPLAY,GRAY,(25 + i * 100,150,50,50))
		textSurface = font.render(GAMME[i], True, (0,0,0))
		DISPLAY.blit(textSurface,(35 + i * 100,167))

def showPartition():
	mid = mido.MidiFile('simple_auclair_PNO.mid')
	for msg in mid.play():
		strmsg = str(msg)
		if strmsg.startswith('note_on'):
			currentNote = int(strmsg.split(" ")[2].split("=")[1]);
			playNote(currentNote)

def playNote(note):
	currentNoteInArray = (note - 60) / 2

	player.note_on(note, 127,1)
	drawAllRectangles([currentNoteInArray])
	pygame.display.update()

	time.sleep(0.2)

	player.note_off(note,127,1)
	drawAllRectangles([])
	pygame.display.update()

pygame.init()
pygame.font.init()

pygame.midi.init()
player= pygame.midi.Output(0)

font = pygame.font.Font(None, 25)

DISPLAY=pygame.display.set_mode((500,400),0,32)
DISPLAY.fill((255,255,255))

GREEN=(0,255,0)
BLUE=(0,0,255)
GRAY=(100,100,100)
GAMME=["DO", "RE", "MI", "FA", "SOL", "LA", "SI"]

drawAllRectangles([])

while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
        	if event.key == pygame.K_ESCAPE:
        		pygame.quit()
        		sys.exit()
        	elif event.key == pygame.K_q:
        		showPartition()
    pygame.display.update()


