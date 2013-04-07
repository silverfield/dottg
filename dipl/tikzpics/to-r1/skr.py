#!/usr/bin/python

import math

fl = open("fl.txt", "r")
for line in fl.readlines():
	line = line.strip()
	line = line.replace(")","")
	line = line.replace("(","")
	line = line.replace(" ","")
	items = line.split(",")
	if (len(items) != 2):
		continue
	print float(items[1]) / math.sqrt(float(items[0]))
