import pandas as pd

df = pd.read_parquet('D:\\YooBee\\HelloWorld\\MSE800\\Week5\\Sample-1m.parquet')
RecordCount = len(df)
print(f'The number of records in the dataset is: {RecordCount}')