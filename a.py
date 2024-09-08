import pandas as pd
from web3 import Web3

# pd.options.display.max_rows= None
# pd.options.display.max_columns=None
# Read the CSV file into a DataFrame
data_frame = pd.read_csv('a.csv')
print(data_frame.columns)

df = data_frame[data_frame['Value_IN(ETH)'] > 1]

print(df)
df.to_csv('filtered_transactions.csv', index=False)

