import pandas as pd

def transform_data(df):

    print("Transform phase started...")

    # Remove duplicates
    df = df.drop_duplicates()

    # Handle missing values
    df = df.dropna()

    # Convert dates
    df['Order Date'] = pd.to_datetime(df['Order Date'])
    df['Ship Date'] = pd.to_datetime(df['Ship Date'])

    # Create profit ratio column
    df['Profit Ratio'] = df['Profit'] / df['Sales']

    # Create processing year/month
    df['Order Month'] = df['Order Date'].dt.month
    df['Order Year'] = df['Order Date'].dt.year

    print("Transformation completed!")

    return df