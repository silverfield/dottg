@echo off
setlocal EnableDelayedExpansion
for %%I in (..\tikzpics\*.tikz) do (
	SET _var=%%I
	SET _result=!_var:~0,-5!
	pdflatex --jobname !_result!-external presentation.tex
)