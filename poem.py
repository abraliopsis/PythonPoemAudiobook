import random
import pyttsx
import os
import pygame
import time
pygame.mixer.init()
pygame.mixer.music.load("sad.mp3")
pygame.mixer.music.play()

poem1 = """Out of the night that covers me, 
Black as the pit from pole to pole, 
I thank whatever gods may be 
For my unconquerable soul. 
In the fell clutch of circumstance 
I have not winced nor cried aloud. 
Under the bludgeonings of chance 
My head is bloody, but unbowed. 
Beyond this place of wrath and tears 
Looms but the Horror of the shade, 
And yet the menace of the years 
Finds and shall find me unafraid. 
It matters not how strait the gate, 
How charged with punishments the scroll, 
I am the master of my fate, 
I am the captain of my soul."""

poem2 = """Two roads diverged in a yellow wood,
And sorry I could not travel both
And be one traveler, long I stood
And looked down one as far as I could
To where it bent in the undergrowth; 
Then took the other, as just as fair,
And having perhaps the better claim
Because it was grassy and wanted wear,
Though as for that the passing there
Had worn them really about the same,
And both that morning equally lay
In leaves no step had trodden black.
Oh, I kept the first for another day! 
Yet knowing how way leads on to way
I doubted if I should ever come back.
I shall be telling this with a sigh
Somewhere ages and ages hence:
Two roads diverged in a wood, and I,
I took the one less traveled by,
And that has made all the difference."""
 
poemSplit1 = poem1.split('\n')
poemSplit2 = poem2.split('\n')

voices = ["Alex", "Alice", "Alva", "Amelie", "Anna", "Carmit", "Damayanti", "Daniel", "Diego", "Ellen", "Fiona", "Fred", "Ioana", "Joana", "Jorge", "Juan", "Kanya", "Karen", "Kyoko", "Laura", "Lekha", "Luca", "Luciana", "Maged", "Mariska", "Mei-Jia", "Melina", "Milena", "Moira", "Monica", "Nora", "Paulina", "Samantha", "Sara", "Satu", "Sin-ji", "Tessa", "Thomas", "Ting-Ting", "Veena", "Victoria", "Xander", "Yelda", "Yuna", "Yuri", "Zosia", "Zuzana"]

def getName():
	return random.choice(voices)
	

for i in poemSplit1:	
	print i	+ "\n"
	os.system("say -v " + getName() + " " + i)
	time.sleep(.1)

print "-------------------------"

for i in poemSplit2:
	print i + "\n"
	os.system("say -v " + getName() + " " + i)
	time.sleep(.1)
