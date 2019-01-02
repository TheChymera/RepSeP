\begin{pythontexcustomcode}[begin]{py}
import os, sys

import matplotlib.pyplot as plt
from pylab import gcf
from lib import boilerplate

# Set the prefix used for figure labels
fig_label_prefix = 'fig'
# Track figure numbers to create unique auto-generated names
fig_count = 0

def pytex_printonly(script, data=''):
	import sys
	try:
		from StringIO import StringIO
	except ImportError:
		from io import StringIO
	import contextlib

	if data:
		pytex.add_dependencies(data)

	@contextlib.contextmanager
	def stdoutIO(stdout=None):
		old = sys.stdout
		if stdout is None:
			stdout = StringIO()
		sys.stdout = stdout
		yield stdout
		sys.stdout = old

	with stdoutIO() as s:
		exec(open(script).read(), locals())

	return s.getvalue()

def pytex_tab(script,
	caption='',
	label='',
	options_post='',
	options_pre='',
	data='',
	):
	"""
	Print a LaTeX formatted table (including outer table environment and additional options), based on a script which returns an inner tabular environment and table structure.
	Such scripts are best created using Pandas' `pd.to_latex()` function.
	"""
	pytex.add_dependencies(script)
	import sys
	try:
		from StringIO import StringIO
	except ImportError:
		from io import StringIO
	import contextlib

	if data:
		pytex.add_dependencies(data)

	@contextlib.contextmanager
	def stdoutIO(stdout=None):
		old = sys.stdout
		if stdout is None:
			stdout = StringIO()
		sys.stdout = stdout
		yield stdout
		sys.stdout = old

	with stdoutIO() as s:
		exec(open(script).read(), locals())

	tab = latex_table(s.getvalue(),
		caption=caption,
		label=label,
		options_post=options_post,
		options_pre=options_pre,
		)
	return tab

def pytex_subfigs(scripts,
	caption='',
	label='',
	placement='[ht]',
	main_environment='figure',
	):
	"""
	Executes a series of Python scripts, grabbing the figures individually, and placing them as subfigures in a figure environment
	"""
	subfigs = '\\begin{{{}}}{}\n'.format(main_environment,placement)
	for script in scripts:
		try:
			script_conf = script['conf']
		except KeyError:
			script_conf=[]
		try:
			script_caption = script['caption']
		except KeyError:
			script_caption=''
		try:
			script_label = script['label']
		except KeyError:
			script_label=''
		try:
			script_options_post = script['options_post']
		except KeyError:
			script_options_post=''
		try:
			script_options_pre = script['options_pre']
		except KeyError:
			script_options_pre=''
		subfig = pytex_fig(script['script'],
			conf=script_conf,
			caption=script_caption,
			label=script_label,
			environment='subfigure',
			options_post=script_options_post,
			options_pre=script_options_pre,
			)
		subfigs += subfig
		subfigs += '\\hfill\n'
	subfigs += '\\caption{{{}}}\n'.format(caption)
	subfigs += '\\label{{{}}}\n'.format(label)
	subfigs += '\\end{{{}}}'.format(main_environment)
	return subfigs

def pytex_fig(script,
	conf=[],
	caption='',
	label='',
	multicol=False,
	environment='figure',
	options_post='',
	options_pre='[htp]'
	):
	'''
	Executes a Python script while applying the custom style.

	Notes
	-----
	We go about this in a somewhat roundabout fashion - always applying `DOC_STYLE`, and then additionally applying a context style which may be only `[DOC_STYLE]` in case no other config file is specified.
	This is because scripts need to be executed in a while statement lest rcParams become persistent between figures.
	Conversely, the text engine part of the configuration needs to be applied outside of the context statement, because it will not work inside it.
	'''
	pytex.add_dependencies(script)
	try:
		document_style = DOC_STYLE
	except NameError:
		document_style = ''
	#for some reason this needs to be applied here, in addition to the context application
	#below (where it can be omitted, but is needed to make sure the `figre_styles` variable is populated).
	plt.style.use(document_style)
	try:
		if isinstance(conf, basestring):
			conf = [conf]
	except NameError:
		if isinstance(conf, str):
			conf = [conf]
	figure_styles = [document_style]+conf
	pytex.add_dependencies(*figure_styles)
	with plt.style.context(figure_styles):
		exec(open(script).read())
	if multicol:
		environment='figure*'
	fig = latex_figure(save_fig(), environment,
		caption=caption,
		label=label,
		options_post=options_post,
		options_pre=options_pre,
		)
	return fig

def figure_by_path(figure_path,textheight_frac=1,caption=None,label=None):
	latex_code = "\\begin{figure}\n"
	latex_code += "\\centering\\includegraphics[width={textheight_frac}\\textheight]{{{figure_path}}}\n".format(textheight_frac=textheight_frac,figure_path=figure_path)
	latex_code += "\\vspace{-.5em}\n"
	latex_code += "\\caption{{{caption}}}\n".format(caption=caption)
	latex_code += "\\label{{fig:{label}}}\n".format(label=label)
	latex_code += "\\end{figure}\n"
	return latex_code

def save_fig(name='', legend=False, fig=None, ext='.pgf'):
	'''
	Save the current figure (or `fig`) to file using `plt.save_fig()`.
	If called with no arguments, automatically generate a unique filename.
	Return the filename.
	'''
	# Get name (without extension) and extension
	if not name:
		global fig_count
		# Need underscores or other delimiters between `input_*` variables
		# to ensure uniqueness
		name = 'auto_fig_{}-{}'.format(pytex.id, fig_count)
		fig_count += 1
	else:
		if len(name) > 4 and name[:-4] in ['.pgf', '.svg', '.png', '.jpg']:
			name, ext = name.rsplit('.', 1)

	# Get current figure if figure isn't specified
	if not fig:
		fig = gcf()
	fig.savefig(name + ext)
	fig.clear()
	plt.cla()
	plt.clf()
	plt.close()
	plt.close('all')
	return name

def latex_environment(name,
	content='',
	options_post='',
	options_pre='',
	):
	"""
	Simple helper function to write the `\begin...\end` LaTeX block.
	"""
	return '\\begin{%s}%s%s%s\\end{%s}' % (name, options_pre, content, options_post, name)

def latex_table(table,
	caption='',
	label='',
	options_post='',
	options_pre='',
	):
	"""
	Add caption and label to an inner tabular environment and than wrap in the outer LaTeX `'table'` environment.
	"""
	content = table
	caption= "\\caption{%s\\label{%s:%s}}\n" % (caption, "tab", label)
	options_post += caption
	return latex_environment("table",
		content=content,
		options_post=options_post,
		options_pre=options_pre,
		)

def latex_figure(name, environment,
	caption='',
	label='',
	width=1,
	options_post='',
	options_pre='[htp]',
	):
	"""
	Auto wrap `name` in a LaTeX figure environment.
	Width is a fraction of `\textwidth`.
	"""
	if not name:
		name = save_fig()
	content = '\\centering\n'
	content += '\\makeatletter\\let\\input@path\\Ginput@path\\makeatother\n'
	content += '\\input{%s.pgf}\n' % name
	if not label:
		label = name
	if caption and not caption.rstrip().endswith('.'):
		caption += '.'
	if caption:
		# `\label` needs to be in `\caption` to avoid issues in some cases
		content += "\\caption{%s\\label{%s:%s}}\n" % (caption, fig_label_prefix, label)
	return latex_environment(environment,
		content=content,
		options_pre=options_pre,
		options_post=options_post,
		)

pytex.bio_fignum = 0
#global pytex # try without this line
def bio_fig(gdd, fname=None, caption=None, label=None):
#		global pytex # and this one, should work
	if fname is None:
		fname = 'pythontex-files-pres/biopython_fig_{0}-{1}.pdf'.format(pytex.id, pytex.bio_fignum)
	gdd.write(fname, "PDF")
	template = '''
	\\begin{{figure}}
	\\centering
	\\includegraphics{{{fname}}}
	\\caption{{ {label} {caption} }}
	\\end{{figure}}
	'''
	if caption is None:
		caption = ''
	if label is None:
		label = ''
	else:
		if not label.startswith('fig:'):
			label = 'fig:' + label
		label = '\\label{{{0}}}'.format(label)
	template = template.format(fname=fname.rsplit('.', 1)[0], label=label, caption=caption)
	print(template)
	pytex.add_created(fname)
	pytex.bio_fignum += 1
	return template
\end{pythontexcustomcode}
\begin{pythontexcustomcode}[end]{py}
\end{pythontexcustomcode}
