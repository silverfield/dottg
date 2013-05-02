#!/usr/bin/python

import sys
import os

arg2line = {}
arg2line["formats"]='\input parts/formats.tex'
arg2line["intr"]='\input parts/introduction.tex'
arg2line["prel"]='\input parts/preliminaries.tex'
arg2line["wrk"]='\input parts/relatedwrk.tex'
arg2line["data"]='\input parts/data.tex'
arg2line["usp"]='\input parts/usp.tex'
arg2line["neur"]='\input parts/neural.tex'
arg2line["conc"]='\input parts/conclusion.tex'
arg2line["ttbl"]='\input parts/ttblazer.tex'

def runProcess(exe):
	stream = os.popen(exe)
	return stream.read()

def escapeStr(str):
	escstr = ''
	for char in str:
		if (char == '/'):
			escstr += '\/'
			continue
		if (char == '\\'):
			escstr += '\\\\'
			continue
		if (char == ' '):
			escstr += '\ '
			continue
		escstr += char
	return escstr
	
cmd = "cp /home/ferrard/workspace/dipl/theory/dipl/dottg.tex /home/ferrard/workspace/dipl/theory/dipl/dottg-select.tex"
runProcess(cmd)

if (len(sys.argv) == 2):
	if (not sys.argv[1] in arg2line):
		print "Unknown option. Use: intr, prel, wrk, data, usp, neur, conc, formats, ttbl"
		sys.exit(1)
	for key in arg2line.keys():
		if (key == sys.argv[1]):
			continue
		searchfor = arg2line[key]
		cmd = "sed 's/" + escapeStr(searchfor) + "/\%" + escapeStr(searchfor) + "/g' /home/ferrard/workspace/dipl/theory/dipl/dottg-select.tex > /home/ferrard/workspace/dipl/theory/dipl/dottg-select.tex.bck"
		runProcess(cmd)
		runProcess("cp /home/ferrard/workspace/dipl/theory/dipl/dottg-select.tex.bck /home/ferrard/workspace/dipl/theory/dipl/dottg-select.tex")

os.system("/usr/local/texlive/2012/bin/x86_64-linux/pdflatex ~/workspace/dipl/theory/dipl/dottg-select.tex")
runProcess("evince ~/workspace/dipl/theory/dipl/dottg-select.pdf")
