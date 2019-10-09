import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import matplotlib as mpl
from lib.categorical import violinplot
from os import path

# Style
palette = ['#ffb66d','#009093']

volume_path = path.abspath('data/volumes.csv')
df = pd.read_csv(volume_path)

df = df.loc[df['Processing']!='Unprocessed']
df = df.loc[((df['Processing']=='Legacy') & (df['Template']=='Legacy')) | ((df['Processing']=='Generic') & (df['Template']=='Generic'))]

df.loc[df['Processing']=='Unprocessed', 'Template'] = ''
ax = violinplot(
	x='Processing',
	y='Volume Change Factor',
	data=df.loc[df['Processing']!='Unprocessed'],
	hue="Contrast",
	saturation=1,
	split=True,
	inner='quartile',
	palette=palette,
	scale='area',
	dodge=False,
	#inner_linewidth=1.0,
	linewidth=mpl.rcParams['grid.linewidth'],
	linecolor='w',
	)
