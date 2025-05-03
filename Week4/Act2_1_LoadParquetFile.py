import pandas as pd
df = pd.read_parquet(
    "D:\\YooBee\\HelloWorld\\MSE800\\Week4\\Sample_data_2.parquet", engine="pyarrow")
print(df.head())
num_features = len(df.columns)
print(f"Number of features in the parquet file: {num_features}")
