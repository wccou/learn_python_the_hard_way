#-*- coding:utf-8 -*-
tabby_cat = "\tI'm tabbed in."#tab 键
persian_cat = "I'm split\non a line."#换行符
backslash_cat = "I'm \\ a \\ cat."#转义字符


#三引号可以打印分行的段落
fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
print "%"

for i in ["/", "-", "|", "\\", "|"]:
	print "%s\n" % i,
	
