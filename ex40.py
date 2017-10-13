#-*- coding:utf-8 -*-
class Song(object):
	def __init__(self, strings):
		self.strings = strings
		
	def sing_me_a_song(self):
		for line in self.strings:
			print line
			
happy_bday = Song(["Happy birthday to you", "I fell good", "It's good!"])
happy_bday.sing_me_a_song()