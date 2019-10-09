import thread
import RPi.GPIO as GPIO
import pygame

def playDo():
	pygame.mixer.music.load('doctave.wav')
	pygame.mixer.music.play(1)

def my_callback(channel):
	if GPIO.input(channel) == GPIO.LOW:
		thread.start_new_thread ( playDo, () )
		GPIO.output(15, 255)
	else:
		GPIO.output(15, 0)

pygame.mixer.init(0, -16, 2, 64)

GPIO.setmode(GPIO.BOARD)

GPIO.setup(7, GPIO.IN)
GPIO.setup(15, GPIO.OUT)

GPIO.add_event_detect(7, GPIO.BOTH, callback=my_callback) 

try:
	while 1:
		a = 0
		#GPIO.output(40, 255)
finally:
	GPIO.cleanup()
