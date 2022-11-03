import pandas as pd
import numpy as np

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
