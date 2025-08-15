import pandas as pd

# Replace 'your_file.parquet' with the path to your Parquet file
parquet_file = 'psuedo-random-HPLT.parquet'

# Read the Parquet file into a DataFrame
df = pd.read_parquet(parquet_file)

# Sample 50 pseudo-random rows and save to CSV
df.sample(n=50, random_state=42).to_csv('pseudo-random.csv', index=False)