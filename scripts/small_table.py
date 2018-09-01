import pandas as pd
df = pd.read_csv("data/sucrosepreference.csv")
print(df.to_latex())
