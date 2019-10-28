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

def pytex_tab(
	inner_tabular='',
	script='',
	caption='',
	label='',
	options_post='',
	options_pre='',
	data='',
	):
	"""
	Print a LaTeX formatted table (including outer table environment and additional options), based on a script which returns an inner tabular environment, or based on an inner tabular environment string.
	Such scripts are best created using Pandas' `pd.to_latex()` function.
	"""
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

	if script and not inner_tabular:
		pytex.add_dependencies(script)
		with stdoutIO() as s:
			exec(open(script).read(), locals())
		inner_tabular = s.getvalue()

	tab = latex_table(inner_tabular,
		caption=caption,
		label=label,
		options_post=options_post,
		options_pre=options_pre,
		)
	return tab

def pytex_subfigs(scripts,
	caption='',
	label='',
	placement='[h]',
	options_pre='',
	options_post='',
	data=[],
	figure_format='pgf',
	main_env='figure',
	):
	"""
	Executes a series of Python scripts, grabbing the figures individually, and placing them as subfigures in a figure environment
	"""
	pytex.add_dependencies(*data)
	subfigs = '\\begin{{{}}}{}\n'.format(main_env,placement)
	if options_pre:
		subfigs += '{}\n'.format(options_pre)
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
		try:
			script_options_pre_caption = script['options_pre_caption']
		except KeyError:
			script_options_pre_caption = ''
		try:
			script_figure_format = script['figure_format']
		except KeyError:
			script_figure_format = figure_format
		subfig = pytex_fig(script['script'],
			conf=script_conf,
			caption=script_caption,
			label=script_label,
			environment='subfigure',
			options_post=script_options_post,
			options_pre=script_options_pre,
			options_pre_caption=script_options_pre_caption,
			figure_format=script_figure_format,
			)
		subfigs += subfig
		subfigs += '\\hfill\n'
	if caption:
		subfigs += '\\caption{{{}}}\n'.format(caption)
	if label:
		subfigs += '\\label{{{}}}\n'.format(label)
	if options_post:
		subfigs += '{}\n'.format(options_post)
	subfigs += '\\end{{{}}}'.format(main_env)
	return subfigs

def pytex_fig(script,
	conf=[],
	caption='',
	label='',
	multicol=False,
	environment='figure',
	options_post='',
	options_pre='[htp]',
	options_pre_caption='',
	data=[],
	figure_format='pgf',
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
	figure_styles = [document_style]+conf+data
	pytex.add_dependencies(*figure_styles)
	with plt.style.context(figure_styles):
		exec(open(script).read())
	if multicol:
		environment='figure*'
	fig = latex_figure(save_fig(ext='.{}'.format(figure_format)), environment,
		caption=caption,
		label=label,
		options_post=options_post,
		options_pre=options_pre,
		options_pre_caption=options_pre_caption,
		figure_format=figure_format,
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
		if len(name) > 4 and name[:-4] in ['.pdf', '.pgf', '.svg', '.png', '.jpg']:
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
	options_pre_caption='',
	options_pre='[htp]',
	figure_format='pgf',
	):
	"""
	Auto wrap `name` in a LaTeX figure environment.
	Width is a fraction of `\textwidth`.
	"""
	if not name:
		name = save_fig()
	content = '\\centering\n'
	if figure_format == 'pgf':
		content += '\\makeatletter\\let\\input@path\\Ginput@path\\makeatother\n'
		content += '\\input{{{}.{}}}\n'.format(name, figure_format)
	elif figure_format == 'pdf':
		content += '\\includegraphics{{{}}}\n'.format(name)
	if options_pre_caption:
		content += '{}\n'.format(options_pre_caption)
	if not label:
		label = name
	if caption:
		# `\label` needs to be in `\caption` to avoid issues in some cases
		content += "\\caption{%s\\label{%s:%s}}\n" % (caption, fig_label_prefix, label)
	return latex_environment(environment,
		content=content,
		options_pre=options_pre,
		options_post=options_post,
		)

\end{pythontexcustomcode}
\begin{pythontexcustomcode}[end]{py}
\end{pythontexcustomcode}
