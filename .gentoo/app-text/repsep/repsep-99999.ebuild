# Copyright 1999-2018 Gentoo Foundation
# Distributed under the terms of the GNU General Public License v2

EAPI=7

PYTHON_COMPAT=( python{2_7,3_4,3_5,3_6} )

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
	>=dev-python/statsmodels-0.9.0[${PYTHON_USEDEP}]
	>=dev-tex/pythontex-0.16[${PYTHON_USEDEP}]
	dev-texlive/texlive-latex
	media-gfx/graphviz[${PYTHON_USEDEP}]
	"

src_unpack() {
	cp -r -L "$DOTGENTOO_PACKAGE_ROOT" "$S"
}
