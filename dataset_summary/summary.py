import pandas as pd

def generate_column_summary(datasets):
    """
    This function generates a summary of each column in the provided datasets.
    
    Parameters:
    datasets (dict): A dictionary where keys are dataset names and values are pandas DataFrames.

    Returns:
    pd.DataFrame: A DataFrame containing the summary of columns.
    """
    column_data = []

    # Loop through datasets and columns
    for name, df in datasets.items():
        for column in df.columns:
            # Count null values and calculate percentage
            qtd_null = df[column].isnull().sum()
            percent_null = qtd_null / len(df) * 100

            # Get the data type of the column
            dtype = df[column].dtype

            # Count unique categorical values (for object type columns)
            if dtype == 'object':
                qtd_cat = df[column].nunique()
            else:
                qtd_cat = 0

            # Append the information into the column_data list
            column_data.append({
                'dataset': name,
                'feature': column,
                'qtd_null': qtd_null,
                'percent_null': percent_null,
                'dtype': dtype,
                'qtd_cat': qtd_cat
            })

    # Convert the column summary data into a DataFrame
    column_df = pd.DataFrame(column_data)

    return column_df


def generate_dataset_summary(datasets):
    """
    This function generates a summary of each dataset, such as the number of rows, 
    columns, null values, and columns with null values.
    
    Parameters:
    datasets (dict): A dictionary where keys are dataset names and values are pandas DataFrames.

    Returns:
    pd.DataFrame: A DataFrame containing the summary of datasets.
    """
    summary_data = []

    # Loop through datasets
    for name, df in datasets.items():
        # Calculate necessary values for the summary
        n_rows = df.shape[0]
        n_cols = df.shape[1]
        null_amount = df.isnull().sum().sum()  # Total number of null values
        null_columns = df.columns[df.isnull().any()].tolist()  # Columns with null values
        qty_null_columns = len(null_columns)  # Number of columns with null values
        
        # Add the result for this dataset to the summary list
        summary_data.append({
            'dataset': name,
            'n_rows': n_rows,
            'n_cols': n_cols,
            'null_amount': null_amount,
            'qty_null_columns': qty_null_columns,
            'null_columns': ', '.join(null_columns)  # Join column names into a string
        })

    # Convert the dataset summary data into a DataFrame
    summary_df = pd.DataFrame(summary_data)

    return summary_df
