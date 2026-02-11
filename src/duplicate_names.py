import pandas as pd

def check_duplicate_names(df, column_name):
    # Step 1: Filter non-null values
    not_null_values = df[df[column_name].notna()]
    print(f"Number of non-null values in '{column_name}': {len(not_null_values)}")

    # Step 2: Convert to lowercase
    values_lower = not_null_values[column_name].str.lower()

    # Step 3: Count Duplicates
    duplicate_count = values_lower.duplicated().sum()
    print(f"The number of duplicated non-null '{column_name}' values: {duplicate_count}")

    return duplicate_count