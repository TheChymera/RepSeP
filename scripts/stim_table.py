import pandas as pd
df = pd.read_csv("data/JogB.tsv",sep='\t')
df = df.drop(['trial_type','strength','strength_unit'], axis=1)
df = df.rename(columns={
        'onset'         :   '\makecell[r]{Onset \\\\ {[}s{]}}',
        'duration'      :   '\makecell[r]{Duration \\\\ {[}s{]}}',
        'frequency'     :   '\makecell[r]{Frequency \\\\ {[}Hz{]}}',
        'pulse_width'   :   '\makecell[r]{Pulse Width \\\\ {[}s{]}}',
        'wavelength'    :   '\makecell[r]{Wavelength \\\\ {[}nm{]}}',
        })
df = df.reset_index(drop=True)
df_tex = df.to_latex(index=False, escape=False)
print(df_tex)
