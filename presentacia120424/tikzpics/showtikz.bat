@ECHO off
DEL tikz2pdff.tex
DEL tikz2pdf_temp.pdf
python tikz2pdf -so %1
DEL tikz2pdff.tex