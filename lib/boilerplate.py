import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
from os import path
from lib.utils import inline_anova

def fstatistic(factor,
	df_path='data/volumes.csv',
	**kwargs
	):
	df_path = path.abspath(df_path)
	df = pd.read_csv(df_path)

	df = df.loc[df['Processing']!='Unprocessed']

	model='Q("Volume Change Factor") ~ Processing*Template'
	ols = smf.ols(model, df).fit()
	anova = sm.stats.anova_lm(ols, typ=2)
	tex = inline_anova(anova, factor, 'tex', **kwargs)
	return tex
