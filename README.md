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

* Lightning Talk, at [EuroSciPy 2017](https://www.youtube.com/watch?v=bu9_338Q7rU)
* Lightning Talk, at [SciPy 2017](https://www.youtube.com/watch?v=8AD4mtXJhpE)

## How To Self-Publish Reproducible Scientific Documents

* Clone this repository: `git clone git@github.com:TheChymera/RepSeP.git`
* Install the dependencies ([listed below](#dependencies)).
* Edit the document files ([`pres.tex`](pres.tex), [`poster.tex`](poster.tex), [`article.tex`](article.tex)) to contain your own research output.
* Compile the documents, e.g.: `pdflatex pres.tex && pythontex.py pres.tex && pdflatex pres.tex`
* Distribute the output and links to your fork of this repository via your favourite outreach channels.

## Dependencies

We distribute [a full list of uniquely identifiable dependencies](.portage.deps) and their associated version constraints, in the format laid out by the [Package Management Specificaton](https://dev.gentoo.org/~ulm/pms/head/pms.html#x1-190003.1.2).
Depending on your distribution (and/or package manager), you may find helpful isntructions on how to best install the dependencies below.

### Gentoo (Portage)

As root, run:

```
emerge -av $(<.portage.deps)
```

## Examples

### Posters

* [BehavioPy, at EuroSciPy 2017](https://bitbucket.org/TheChymera/behaviopy_repsep/)
