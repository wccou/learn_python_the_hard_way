#-*- coding:utf-8 -*-
the_count = [1, 2, 3, 4, 5]
fruits = ["apples", "oranges", "pears", "apricots"]
change = [1, "pennies", 2, "dimes", 3, "quarters"]
#first
for number in the_count:
	print "This is count %d." % number
	
#also the first
for fruit in fruits:
	print "A fruit of type: %s." % fruit
	
#mixed lists use %r
for i in change:
	print "I got %r." % i
	
#We can also build an empty lists
elements = []
#Use function to append
for i in range (0, 6):
	print "Adding %d to the list." % i
	#append is a function that lists understand
	elements.append(i)
	
#now we can print them out too
for i in elements:
	print "Elemnet was: %d." % i