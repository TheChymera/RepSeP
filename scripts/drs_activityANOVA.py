import pandas as pd
from os import path
#from samri.typesetting import inline_anova

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
print(anova)
