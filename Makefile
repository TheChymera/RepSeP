#!/usr/bin/env bash

# Publishing variables
# Ideally these should be environment variables and we should check here whether they're defined and explain upload requires them if they're not.
SERVER=dreamarticles
WEBSITE=articles.chymera.eu
NAME=$(shell basename $(shell pwd))


# Set NOCLIENT variable to not prepend hostname to published filename:
# e.g. `NOCLIENT=1 make upload-article`
CLIENT := $(if $(NOCLIENT),$(shell cat /dev/null),$(shell hostname)_)

COMMON := $(wildcard common/*)
PYTHONTEX_ALL := $(wildcard lib/* pythontex/* scripts/*)
STATIC_ALL := $(wildcard img/* *.sty)

all: article.pdf poster.pdf pitch.pdf review.pdf slides.pdf

article.pdf:	$(wildcard article/*) $(COMMON) $(PYTHONTEX_ALL) $(STATIC_ALL) article.tex
	rubber --pdf --unsafe article.tex
pitch.pdf:		$(wildcard pitch/*) $(COMMON) $(PYTHONTEX_ALL) $(STATIC_ALL) pitch.tex
	rubber --pdf --unsafe pitch.tex
poster.pdf:	$(wildcard poster/*) $(COMMON) $(PYTHONTEX_ALL) $(STATIC_ALL) poster.tex
	rubber --pdf --unsafe poster.tex
review.pdf:		$(wildcard review/*) $(COMMON) slides.tex
	rubber --pdf --unsafe review.tex
slides.pdf:		$(wildcard slides/*) $(COMMON) $(PYTHONTEX_ALL) $(STATIC_ALL) slides.tex
	rubber --pdf slides.tex


# Cleanscripts
clean-article:
	rubber --clean article.tex
	rm _minted-article -rf
clean-pitch:
	rubber --clean pitch.tex
	rm _minted-pitch -rf
clean-poster:
	rubber --clean poster.tex
	rm _minted-poster -rf
clean-review:
	rubber --clean review.tex
	rm _minted-review -rf
clean-slides:
	rubber --clean slides.tex
	rm _minted-slides -rf
clean-traces:
	rm *.vrb
clean: clean-article clean-pitch clean-poster clean-review clean-slides clean-traces

# Upload scripts
upload: upload-article
upload-article: article.pdf
	rsync -avP article.pdf ${SERVER}:${WEBSITE}/${CLIENT}${NAME}_article.pdf
upload-pitch: pitch.pdf
	rsync -avP pitch.pdf ${SERVER}:${WEBSITE}/${CLIENT}${NAME}_pitch.pdf
upload-poster: poster.pdf
	rsync -avP poster.pdf ${SERVER}:${WEBSITE}/${CLIENT}${NAME}_poster.pdf
upload-slides: slides.pdf
	rsync -avP slides.pdf ${SERVER}:${WEBSITE}/${CLIENT}${NAME}_slides.pdf
