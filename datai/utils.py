import pandas as pd
import numpy as np
from typing import Union, List, Dict

def validate_dataset(data: pd.DataFrame) -> bool:
    """
    Validates the input dataset to ensure it meets basic requirements for use within the datai library.

    Args:
        data (pd.DataFrame): The dataset to validate.

    Returns:
        bool: True if valid, raises an error if not.

    Raises:
        ValueError: If the data is not a DataFrame or if the DataFrame is empty.
    """
    if not isinstance(data, pd.DataFrame):
        raise ValueError("The provided data is not a pandas DataFrame.")
    if data.empty:
        raise ValueError("The provided DataFrame is empty.")

    # Add library-specific validation rules here, if any
    # Example: check if specific columns exist
    # required_columns = ['feature1', 'feature2']
    # if not all(col in data.columns for col in required_columns):
    #     raise ValueError(f"DataFrame is missing required columns: {required_columns}")

    return True

def safe_column_convert(data: pd.DataFrame, column_types: Dict[str, str], errors: str = 'ignore') -> pd.DataFrame:
    """
    Safely converts the data type of specified columns, handling potential errors.

    This function attempts to convert columns to the specified data types. If a conversion
    fails, it will either skip the column (if errors='ignore') or raise an exception
    (if errors='raise'). This is more robust than `astype` for user-provided data.

    Args:
        data (pd.DataFrame): The DataFrame to modify.
        column_types (Dict[str, str]): A dictionary where keys are column names and values are the desired data types
                           (e.g., {'col1': 'int', 'col2': 'float', 'col3': 'category'}).
        errors (str, optional): How to handle conversion errors. Defaults to 'ignore'.
            Options: 'ignore' (skip the column), 'raise' (raise an exception).

    Returns:
        pd.DataFrame: The DataFrame with column types converted (or attempted to be converted).
    """
    data = data.copy()
    for column, data_type in column_types.items():
        try:
            if column in data.columns:  # Check if column exists first
                data[column] = data[column].astype(data_type, errors=errors)
                print(f"Column '{column}' successfully converted to type '{data_type}'.")
            else:
                print(f"Warning: Column '{column}' not found in DataFrame.")
        except ValueError as e:
            if errors == 'raise':
                raise ValueError(f"Unable to convert column '{column}' to type '{data_type}'. Check data for compatibility.  Original error: {e}")
            else:
                print(f"Warning: Unable to convert column '{column}' to type '{data_type}'.  Skipping column. Original error: {e}")
    return data

def library_data_summary(data: pd.DataFrame) -> Dict:
    """
    Provides a concise summary of the DataFrame, focusing on aspects most relevant to the 'datai' library.

    This function provides a focused summary tailored for users of the 'datai' library.
    It prioritizes information useful for visualization and data analysis within the library's context.

    Args:
        data (pd.DataFrame): The dataset to summarize.

    Returns:
        Dict: A dictionary containing key summary statistics.
    """
    num_rows, num_cols = data.shape
    data_types = data.dtypes
    numeric_cols = data_types[data_types != 'object'].index.tolist()
    categorical_cols = data_types[data_types == 'object'].index.tolist()

    summary = {
        "Number of rows": num_rows,
        "Number of columns": num_cols,
        "Numeric columns": numeric_cols,
        "Categorical columns": categorical_cols,
        "Missing Values": data.isnull().sum().to_dict()
    }

    return summary

def column_name_compatibility(data: pd.DataFrame) -> pd.DataFrame:
    """
    Ensures column names are compatible with Seaborn and Matplotlib by replacing invalid characters.

    This function replaces characters that might cause issues with plotting libraries,
    such as spaces, special characters, or leading digits.  It also converts column names to lowercase.

    Args:
        data (pd.DataFrame): The DataFrame to modify.

    Returns:
        pd.DataFrame: The DataFrame with compatible column names.
    """
    data = data.copy()
    new_columns = (data.columns.str.lower()
                   .str.replace(' ', '_', regex=False)
                   .str.replace('[^A-Za-z0-9_]+', '', regex=True)
                   .tolist())

    # Ensure unique column names (add a suffix if duplicates are created)
    seen_names = set()
    unique_columns = []
    for name in new_columns:
        if name in seen_names:
            i = 1
            new_name = f"{name}_{i}"
            while new_name in seen_names:
                i += 1
                new_name = f"{name}_{i}"
            unique_columns.append(new_name)
        else:
            unique_columns.append(name)
        seen_names.add(name)

    data.columns = unique_columns
    return data

