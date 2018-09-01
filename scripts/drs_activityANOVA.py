import pandas as pd
from os import path
#from samri.typesetting import inline_anova

def float_to_tex(f,
	max_len=4,
	condensed=False,
	):
	"""Reformat float to tex syntax
	Parameters
	----------
	f : float
		Float to format.
	max_len : int
		Maximum digit length of output strings.
	"""

	if condensed:
		model_str="{}\\!\\!\\times\\!\\!10^{{{}}}"
	else:
		model_str="{} \\times 10^{{{}}}"


	if f >= 10**-max_len and f <= 10**max_len:
		f_str_template = "{{:.{}g}}".format(max_len)
		f_str = f_str_template.format(f)
	else:
		f_str = "{:e}".format(f)
		f_decimals, f_exponent = f_str.split("e")
		truncated_decimals = f_decimals[:max_len].rstrip('.')
		f_str = model_str.format(truncated_decimals,int(f_exponent))
	return f_str

max_len=3
data_dir = "data"
data_path = path.join(data_dir,'drs_activity.csv')
df = pd.read_csv(data_path)

import statsmodels.formula.api as smf
import numpy as np

model = smf.mixedlm("t ~ Session * treatment", df, groups=df["subject"])
fit = model.fit()

omnibus_tests = np.eye(len(fit.params))[1:-1]
omnibus_tests = omnibus_tests[:4]
omnibus_tests[0,6] = -1
omnibus_tests[1,7] = -1
omnibus_tests[2,8] = -1
omnibus_tests[3,9] = -1
anova = fit.f_test(omnibus_tests)
#print(inline_anova(anova,style="tex", max_len=2, condensed=True))
string_template = "$F_{{{},{}}}\!=\!{},\\, p\!=\!{}$"
try:
        degrees_of_freedom = float_to_tex(anova["df"][factor], max_len=max_len)
        degrees_of_freedom_rest = float_to_tex(anova["df"]["Residual"], max_len=max_len)
        f_string = float_to_tex(anova["F"][factor], max_len=max_len, condensed=True)
        p_string = float_to_tex(anova["PR(>F)"][factor], max_len=max_len, condensed=True)
except TypeError:
        degrees_of_freedom = float_to_tex(anova.df_num, max_len=max_len)
        degrees_of_freedom_rest = float_to_tex(anova.df_denom, max_len=max_len)
        f_string = float_to_tex(anova.fvalue[0][0], max_len=max_len, condensed=True)
        p_string = float_to_tex(float(anova.pvalue), max_len=max_len, condensed=True)
inline = string_template.format(
        degrees_of_freedom,
        degrees_of_freedom_rest,
        f_string,
        p_string,)
print(inline)
