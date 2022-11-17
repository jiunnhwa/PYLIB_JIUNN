import pandas as pd
import numpy as np


# https://www.geeksforgeeks.org/how-to-compare-two-columns-in-pandas/
# https://www.geeksforgeeks.org/how-to-compare-two-dataframes-with-pandas-compare/


details = {
	'Column1': [1, 2, 3, 4],
	'Column2': [7, 4, 2, 9],
	'Column3': [3, 8, 10, 30],
}

# creating a Dataframe object
df = pd.DataFrame(details)

# apply function
df['New'] = df.apply(lambda x: x['Column1'] if x['Column1'] <= x['Column2'] and x['Column1']<= x['Column3'] else np.nan, axis=1)

# printing the dataframe
print(df)







df_to_tuples = lambda df: list(df.itertuples(index=False, name=None ))
df_colnames_to_tuples = lambda df: tuple(list(df))
df_merge = lambda dfx,dfy,on,how: pd.merge(dfx,dfy,on=on,how=how)# Merge DataFrames by Column
df_astype = lambda df: df.astype({'colA':'string','colB':'int'})
