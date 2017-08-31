import pandas as pd
df = pd.DataFrame.from_csv("data/sucrosepreference.csv")
print(df.to_latex())
