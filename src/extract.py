import pandas as pd
file_path = 'C:\\Users\\humag\\OneDrive\\Documents\\PYTHON\\etl-sales\\data\\Sample - Superstore.csv'
def extract_data(file_path):
    df = pd.read_csv(file_path, encoding='latin-1')
    print(df.head())
    # print(df.info())
    # print(df.describe())
    # print(df.isnull().sum())
    # print(df.duplicated().sum())
    return df
print("Extract phase completed!")