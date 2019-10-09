import sys, time
import pygame, pygame.midi
from pygame.locals import *
import mido

# todo upgrade python3

def highlightNote(note):
	drawAllRectangles([note])
	pygame.display.update()

def hideNotes():
	drawAllRectangles([])
	pygame.display.update()

def drawAllRectangles(toColorate):
	DISPLAY.fill((255,255,255))
	
	for i in range(5):
		if i in toColorate:
			pygame.draw.rect(DISPLAY,BLUE,(25 + i * 100,150,50,50))
		else:
			pygame.draw.rect(DISPLAY,GRAY,(25 + i * 100,150,50,50))
		textSurface = font.render(GAMME[i], True, (0,0,0))
		DISPLAY.blit(textSurface,(35 + i * 100,167))

def playNote(note):
	player.note_on(note, 127,1)
	time.sleep(0.2)
	player.note_off(note,127,1)
	
def showPartition():
	mid = mido.MidiFile('simple_auclair_PNO.mid')
	for msg in mid.play():
		strmsg = str(msg)
		if strmsg.startswith('note_on'):
			currentNote = int(strmsg.split(" ")[2].split("=")[1]);
			currentNoteInArray = (currentNote - 60) / 2

			highlightNote(currentNoteInArray)
			playNote(currentNote)
			hideNotes()

def learnPartition():
	mid = mido.MidiFile('simple_auclair_PNO.mid')
	for msg in mid.play():
		strmsg = str(msg)
		if strmsg.startswith('note_on'):
			currentNote = int(strmsg.split(" ")[2].split("=")[1]);
			currentNoteInArray = (currentNote - 60) / 2
			highlightNote(currentNoteInArray)

			noteFound=False
			while not noteFound:
				for event in pygame.event.get():
					if event.type == pygame.KEYDOWN:
						if event.key == pygame.K_SPACE:
							playNote(currentNote)
							noteFound=True
							break
			hideNotes()

pygame.init()
pygame.font.init()

pygame.midi.init()
player= pygame.midi.Output(0,0)

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
    		elif event.key == pygame.K_w:
        		learnPartition()
    pygame.display.update()
