![RepSeP Logo](img/repsep.png?raw=true "RepSeP Logo")

# RepSeP

The **Rep**roducible **Se**lf **P**ublishing toolkit demonstrates how to reuse your favourite data analysis workflows in order to seamlessly include quasi-dynamic publication-quality output (e.g. figures, tables, or statistic reports) in the most common science communication formats. Currently we provide examples for:

* Presentation Slides
* A Poster
* An Article

In these examples, analysis does not have to be initiated manually, and output elements do not have to be copied, manually scaled, styled, or otherwise manipulated.
Data analysis is kept in one and only one place, and configurable styling is applied programmatically at the document or output element level.
Data *and* code dependencies are monitored for update via checksums, and are either provided or specified, so that both the toolkit in its present incarnation - as well as your own derivatives - can be reproduced locally and autonomously by your colleagues, reviewers, students, and everybody else.
As no binaries are tracked, publications built analogously to our examples are excellently suited for collaborative editing and version tracking, e.g. via Git.

### Video Presentations

* [Reproducible Self-Publication via PythonTeX](https://www.youtube.com/watch?v=bu9_338Q7rU), at EuroSciPy 2017 in Erlangen (DE)
* [Reproducible Self-Publishing](https://www.youtube.com/watch?v=8AD4mtXJhpE), at SciPy 2017 in Austin (TX,USA)

## How To Self-Publish Reproducible Scientific Documents

* Clone this repository: `git clone git@github.com:TheChymera/RepSeP.git`
* Install the dependencies ([listed below](#dependencies)).
* Edit the document files ([`slides.tex`](slides.tex), [`poster.tex`](poster.tex), [`article.tex`](article.tex)) to contain your own research output.
* Compile the documents, e.g.: `./compile slides`
* Distribute the output and links to your fork of this repository via your favourite outreach channels.

## Dependencies

We distribute [a full list of uniquely identifiable dependencies](.gentoo/app-text/repsep/repsep-99999.ebuild) and their associated version constraints, in the format laid out by the [Package Management Specificaton](https://dev.gentoo.org/~ulm/pms/head/pms.html#x1-190003.1.2).
Depending on your distribution (and/or package manager), you may find helpful isntructions on how to best install the dependencies below.

List of dependencies:

* [matplotlib](https://matplotlib.org/)
* [numpy](https://www.numpy.org/)
* [statsmodels](https://www.statsmodels.org/stable/index.html) (>=`0.9.0`)
* [pythontex](https://github.com/gpoore/pythontex) (>=`0.16`)
* [texlive-latex](https://www.tug.org/texlive/)
* [graphviz](https://www.graphviz.org/)

Note that it is likely that you'll have to install pythontex from source
([gpoore/pythontex](https://github.com/gpoore/pythontex)). To do this, clone
the repo and follow the [installation instructions](https://github.com/gpoore/pythontex/blob/master/pythontex/pythontex.pdf).

## Examples

### Posters

* [BehavioPy Poster](https://bitbucket.org/TheChymera/behaviopy_repsep/), versions presented at:
  * [EuroSciPy 2017](https://bitbucket.org/TheChymera/behaviopy_repsep/raw/7d626813659efa1345efbf07faafaa9a6bcf3876/poster.pdf) in Erlangen (DE)
