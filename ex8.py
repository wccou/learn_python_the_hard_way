#-*- coding:utf-8 -*-
formatter = "%r %r %r %r"
print formatter % (1, 2, 3, 4)
print formatter % (1, "I am a student.", 2, 3)
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % ("I had this thing.",
	"That you could type up right.",
	"But it did't sing.",
	"So I said goodnight.")