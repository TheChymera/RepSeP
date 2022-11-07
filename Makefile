#!/usr/bin/env bash

COMMON := bib.bib common_header.tex
PYTHONTEX_ALL := $(wildcard lib/* pythontex/* scripts/*)
STATIC_ALL := $(wildcard img/* *.sty)

all: article.pdf poster.pdf pitch.pdf slides.pdf

article.pdf:	$(wildcard article/*) $(COMMON) $(PYTHONTEX_ALL) $(STATIC_ALL)
	rubber --pdf --unsafe article.tex
pitch.pdf:		$(wildcard pitch/*) $(COMMON) $(PYTHONTEX_ALL) $(STATIC_ALL)
	rubber --pdf --unsafe pitch.tex
poster.pdf:	$(wildcard poster/*) $(COMMON) $(PYTHONTEX_ALL) $(STATIC_ALL)
	rubber --pdf --unsafe poster.tex
slides.pdf:		$(wildcard slides/*) $(COMMON) $(PYTHONTEX_ALL) $(STATIC_ALL)
	rubber --pdf --unsafe slides.tex

cleanarticle:
	rubber --clean article.tex
	rm _minted-article -rf
cleanpitch:
	rubber --clean pitch.tex
	rm _minted-pitch -rf
cleanposter:
	rubber --clean poster.tex
	rm _minted-poster -rf
cleanslides:
	rubber --clean slides.tex
	rm _minted-slides -rf
cleantraces:
	rm -rf\
		auto_fig_py_*\
		*.aux\
		*.bbl\
		*.blg\
		*.log\
		*.nav\
		*.out\
		*.pgf\
		pythontex-files-*\
		*.pytxcode\
		*.snm\
		*.toc\
		*.vrb\
		*.rubbercache
clean: cleanarticle cleanpitch cleanposter cleanslides
cleanfull: cleanarticle cleanpitch cleanposter cleanslides cleantraces
