# Copyright 1999-2022 Gentoo Foundation
# Distributed under the terms of the GNU General Public License v2

EAPI=8

PYTHON_COMPAT=( python3_{7..11} )
inherit distutils-r1

DESCRIPTION="The Reproducible Self Publishing Reference Implementation"
HOMEPAGE="https://github.com/TheChymera/RepSeP"

LICENSE="GPL-3"
SLOT="0"
IUSE=""
KEYWORDS=""

DEPEND=""
RDEPEND="
	dev-python/matplotlib[${PYTHON_USEDEP}]
	dev-python/numpy[${PYTHON_USEDEP}]
	dev-python/pandas[${PYTHON_USEDEP}]
	dev-python/pygments[${PYTHON_USEDEP}]
	dev-python/seaborn[${PYTHON_USEDEP}]
	dev-python/statsmodels[${PYTHON_USEDEP}]
	>=dev-tex/latex-beamer-3.41
	>=dev-tex/pythontex-0.16
	dev-tex/rubber[${PYTHON_USEDEP}]
	app-text/texlive
	media-gfx/graphviz
	sys-devel/make
	"
