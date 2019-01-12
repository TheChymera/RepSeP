# Copyright 1999-2018 Gentoo Foundation
# Distributed under the terms of the GNU General Public License v2

EAPI=7

PYTHON_COMPAT=( python{2_7,3_4,3_5,3_6} )

DESCRIPTION="The Reproducible Self Publishing Reference Implementation"
HOMEPAGE="https://github.com/TheChymera/RepSeP"

LICENSE="GPL-3"
SLOT="0"
IUSE=""
KEYWORDS=""

DEPEND=""
RDEPEND="
	dev-python/matplotlib
	dev-python/numpy
	dev-python/pandas
	dev-python/seaborn
	dev-python/pygments
	>=dev-python/statsmodels-0.9.0
	>=dev-tex/latex-beamer-3.41
	>=dev-tex/pythontex-0.16
	app-text/texlive
	media-gfx/graphviz
	"

src_unpack() {
	cp -r -L "$DOTGENTOO_PACKAGE_ROOT" "$S"
}
