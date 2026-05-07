# Retail Sales ETL Pipeline

## Overview
This project demonstrates a complete ETL (Extract, Transform, Load) pipeline using Python, pandas, SQLite, and data visualization techniques.

The pipeline processes retail sales data from the Superstore dataset, performs cleaning and transformation, loads the processed data into a SQLite database, and generates business insights through analysis and charts.

---

## Features

- Extract data from CSV
- Remove duplicates and missing values
- Convert date columns
- Create new calculated features
- Load cleaned data into SQLite database
- Generate sales analysis by category
- Visualize results using matplotlib

---

## Tech Stack

- Python
- pandas
- SQLite
- matplotlib

---

## Project Structure

etl-sales/
│
├── data/
├── output/
├── src/
├── requirements.txt
├── README.md
└── sales.db

---

## Run Project

pip install -r requirements.txt

python src/main.py

---

## Output

- Cleaned CSV dataset
- SQLite database
- Sales visualization chart

---

## Sample Analysis

- Sales by category
- Profit ratio calculations
- Monthly order analysis