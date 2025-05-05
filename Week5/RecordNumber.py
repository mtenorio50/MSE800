import pandas as pd


class RecordCount:
    def __init__(self, file_path):
        self.file_path = file_path

    def GetRecordNumber(self):
        df = pd.read_parquet(self.file_path)
        return len(df)


def main():
    file_path = 'D:\\YooBee\\HelloWorld\\MSE800\\Week5\\Sample-1m.parquet'
    record_counter = RecordCount(file_path)
    count = record_counter.GetRecordNumber()
    print(f'The number of records in the dataset is: {count}')


if __name__ == "__main__":
    main()
