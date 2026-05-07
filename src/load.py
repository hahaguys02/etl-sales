import sqlite3

def load_to_csv(df, output_path):

    print("Loading cleaned CSV...")

    df.to_csv(output_path, index=False)

    print("CSV saved successfully!")

def load_to_sqlite(df):

    print("Loading data into SQLite database...")

    conn = sqlite3.connect("sales.db")

    df.to_sql(
        "superstore_sales",
        conn,
        if_exists="replace",
        index=False
    )

    conn.close()

    print("Database loaded successfully!")