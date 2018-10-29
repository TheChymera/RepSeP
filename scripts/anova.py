import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
from os import path
from lib.utils import inline_anova

df_path = path.abspath('data/volumes.csv')
df = pd.read_csv(df_path)

df = df.loc[df['Processing']!='Unprocessed']

model='Q("Volume Change Factor") ~ Processing*Template'
ols = smf.ols(model, df).fit()
anova = sm.stats.anova_lm(ols, typ=2)
tex = inline_anova(anova, 'Processing:Template', 'tex')

print(tex)
