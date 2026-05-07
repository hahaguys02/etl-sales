from extract import extract_data
from transform import transform_data
from load import load_to_csv, load_to_sqlite
from analysis import analysis

def run_etl_pipeline():

    # Extract
    df = extract_data("data\Sample - Superstore.csv")

    # Transform
    df = transform_data(df)

    # Load
    load_to_csv(
        df,
        "data\cleaned_sales.csv"
    )

    load_to_sqlite(df)

    # Analysis
    analysis(df)

    print("\nETL Pipeline Completed Successfully!")

if __name__ == "__main__":
    run_etl_pipeline()