import pandas as pd

# This function helps to limit the result only to columns with null values per dataset
def show_null_columns(df, df_name="Dataset"):
    null_counts = df.isnull().sum()
    null_counts = null_counts[null_counts > 0]

    print(f"\nNull values in {df_name}:")
    
    if null_counts.empty:
        print("No null values found.")
    else:
        print(null_counts.sort_values(ascending=False))