#-*- coding:utf-8 -*-
tabby_cat = "\tI'm tabbed in."#tab ��
persian_cat = "I'm split\non a line."#���з�
backslash_cat = "I'm \\ a \\ cat."#ת���ַ�


#�����ſ��Դ�ӡ���еĶ���
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
	
