#-*- coding:utf-8 -*- 
class Parent(object):
	def altered(self):
		print "PARENT altered()"
		
class Child(Parent):
	def altered(self):
		print "CHILD, BEFORE PARENT altered()"
		super(Child, self).altered()
		print "CHILD, AFTER PARENT alteed()"
		
dad = Parent()
son = Child()

dad.altered()
son.altered()
