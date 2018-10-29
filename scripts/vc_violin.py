import matplotlib.pyplot as plt
import pandas as pd
import matplotlib as mpl
from os import path
from itertools import product
from lib.categorical import violinplot

# Style
palette = ['#80e050','#755575']

volume_path = path.abspath('data/volumes.csv')
df = pd.read_csv(volume_path)

df.loc[df['Processing']=='Unprocessed', 'Template'] = ''
ax = violinplot(
	x="Processing",
	y='Volume Change Factor',
	data=df.loc[df['Processing']!='Unprocessed'],
	hue="Template",
	saturation=1,
	split=True,
	inner='quartile',
	palette=palette,
	scale='area',
	dodge=False,
	inner_linewidth=1.0,
	linewidth=mpl.rcParams['grid.linewidth'],
	linecolor='w',
	)
