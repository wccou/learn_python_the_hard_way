#-*- coding:utf-8 -*-
my_name = 'Wei Chenchen'
my_age = 23
my_height = 178
my_weight = 132
my_eyes = 'black'
my_teeth = 'White'
my_hair = 'black'

print "Let's talk about %s." % my_name
print "He's %d cm tall." % my_height
print "He's %d pounds heavy." % my_weight
print "He's got %s eyes and %s hair" % (my_eyes,my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth#格式化输出时 字符串类型需要加括号

#tricky 
print "If I add %d, %d, and %d I get %d." % (
	my_age, my_height, my_weight,my_age + my_height + my_weight)
