import matplotlib.pyplot as plt

def analysis(df):

    print("\nRunning sales analysis...\n")

    # Group sales by category
    sales_summary = df.groupby("Category")["Sales"].sum()

    print(sales_summary)

    # Create chart
    sales_summary.plot(kind='bar')

    plt.title("Sales by Category")
    plt.xlabel("Category")
    plt.ylabel("Total Sales")

    plt.tight_layout()

    plt.savefig("output/sales_chart.png")

    plt.show()

    print("\nChart saved to output folder!")