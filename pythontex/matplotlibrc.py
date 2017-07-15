def main():
	import matplotlib as mpl
	mpl.rcParams['font.size'] = 7 
	mpl.rcParams['figure.titlesize'] = "x-small"
	mpl.rcParams['axes.labelsize'] = "xx-small"
	mpl.rcParams['axes.titlesize'] = "x-small"
	mpl.rcParams['xtick.labelsize'] = "x-small"
	mpl.rcParams['ytick.labelsize'] = "x-small"
	mpl.rcParams['legend.fontsize'] = "x-small"
	mpl.rcParams['legend.markerscale'] = "0.5"
	mpl.rcParams['lines.markersize'] = "5"
	mpl.rcParams['legend.frameon'] = True
	mpl.rcParams['legend.labelspacing'] = "0.3"
	mpl.rcParams['axes.labelcolor'] = "0.4"
	mpl.rcParams['xtick.color'] = "0.4"
	mpl.rcParams['ytick.color'] = "0.4"
	mpl.rcParams['ytick.direction'] = "in"
	mpl.rcParams['savefig.bbox'] = "tight"
	mpl.rcParams['savefig.dpi'] = 400
	mpl.rcParams['text.usetex'] = True
	mpl.rcParams['pgf.texsystem'] = "pdflatex"
	mpl.rcParams['text.latex.preamble'] = r"\usepackage{siunitx}"
	mpl.rcParams['lines.linewidth'] = 1.0
