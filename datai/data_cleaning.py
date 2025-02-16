import pandas as pd
import numpy as np
from typing import List, Union

def data_info(data: pd.DataFrame) -> None:
    """
    Provides a comprehensive overview of the DataFrame, including:
        - Shape and size
        - Data types of each column
        - Descriptive statistics for numerical columns
        - Frequency counts for categorical columns
        - Number of missing values in each column
        - Memory usage
    """
    print("DataFrame Overview:")
    print(f"Shape: {data.shape}")
    print(f"Size: {data.size}")
    print("\nData Types:")
    print(data.dtypes)
    print("\nDescriptive Statistics (Numerical Columns):")
    print(data.describe())
    
    # Categorical Column Analysis
    categorical_cols = data.select_dtypes(include=['object', 'category']).columns
    print("\nFrequency Counts (Categorical Columns):")
    for col in categorical_cols:
        print(f"\nColumn: {col}")
        print(data[col].value_counts())  # Provide counts for each category
        print(f"\nColumn: {col} Percentage")
        print(data[col].value_counts(normalize = True) * 100) # Provide percentages for each category
    
    print("\nMissing Values:")
    print(data.isnull().sum())  # Show count of NaN values
    
    # Show percentage of missing values per column
    print("\nPercentage of Missing Values:")
    print((data.isnull().sum() / len(data)) * 100)
    
    print("\nMemory Usage:")
    print(data.memory_usage(deep=True))  # Show memory usage of each column
    print(f"\nTotal Memory Usage: {data.memory_usage(deep=True).sum()} bytes")

def handle_missing_values(data: pd.DataFrame, strategy: str = 'mean', columns: Union[str, List[str]] = 'all', fill_value=None) -> pd.DataFrame:
    """
    Handles missing values using various strategies.

    Args:
        data (pd.DataFrame): The DataFrame to clean.
        strategy (str, optional): Strategy for handling missing values.
            Options: 'mean', 'median', 'mode', 'ffill', 'bfill', 'constant', 'drop'. Defaults to 'mean'.
        columns (Union[str, List[str]], optional): Columns to apply the strategy to. Defaults to 'all'.
            If 'all', applies to all columns with missing values.
        fill_value: Value to use when strategy is 'constant'. Required if strategy is constant

    Returns:
        pd.DataFrame: The DataFrame with missing values handled.
    """

    if columns == 'all':
        cols_with_missing = data.columns[data.isnull().any()].tolist()
    elif isinstance(columns, str):
        cols_with_missing = [columns] if columns in data.columns else []
    elif isinstance(columns, list):
        cols_with_missing = [col for col in columns if col in data.columns]
    else:
        raise ValueError("Invalid 'columns' argument.  Must be 'all', a string, or a list of strings.")

    if not cols_with_missing:
        print("No missing values found in the specified columns.")
        return data

    cleaned_data = data.copy() # Avoid modifying original DataFrame

    for col in cols_with_missing:
        if cleaned_data[col].isnull().any(): #Double Check
            if strategy == 'mean' and pd.api.types.is_numeric_dtype(cleaned_data[col]):
                cleaned_data[col] = cleaned_data[col].fillna(cleaned_data[col].mean())
            elif strategy == 'median' and pd.api.types.is_numeric_dtype(cleaned_data[col]):
                cleaned_data[col] = cleaned_data[col].fillna(cleaned_data[col].median())
            elif strategy == 'mode':
                cleaned_data[col] = cleaned_data[col].fillna(cleaned_data[col].mode()[0]) # Mode returns a Series
            elif strategy == 'ffill':
                cleaned_data[col] = cleaned_data[col].fillna(method='ffill')
            elif strategy == 'bfill':
                cleaned_data[col] = cleaned_data[col].fillna(method='bfill')
            elif strategy == 'constant':
              if fill_value is None:
                raise ValueError("fill_value must be specified when strategy is 'constant'")
              cleaned_data[col] = cleaned_data[col].fillna(fill_value)
            elif strategy == 'drop':
                cleaned_data.dropna(subset=[col], inplace=True)
            else:
                raise ValueError(f"Invalid strategy '{strategy}' or strategy not applicable to column '{col}'")
            print(f"Missing values in column '{col}' handled using strategy '{strategy}'.")

    return cleaned_data

def remove_duplicates(data: pd.DataFrame, subset: Union[str, List[str]] = None, keep: str = 'first') -> pd.DataFrame:
    """
    Removes duplicate rows from the DataFrame.

    Args:
        data (pd.DataFrame): The DataFrame to clean.
        subset (Union[str, List[str]], optional):  Columns to consider for identifying duplicates.
            If None, all columns are used. Defaults to None.
        keep (str, optional):  Determines which duplicates to keep.
            Options: 'first' (default), 'last', False (drop all duplicates).

    Returns:
        pd.DataFrame: The DataFrame with duplicates removed.
    """
    cleaned_data = data.copy()  # Avoid modifying original DataFrame
    cleaned_data.drop_duplicates(subset=subset, keep=keep, inplace=True)
    print(f"DataFrame shape after removing duplicates: {cleaned_data.shape}")
    return cleaned_data

def standardize_column_names(data: pd.DataFrame) -> pd.DataFrame:
    """
    Standardizes column names by:
        - Converting to lowercase
        - Replacing spaces with underscores
        - Removing special characters
    """
    cleaned_data = data.copy()
    cleaned_data.columns = (cleaned_data.columns.str.lower()
                           .str.replace(' ', '_', regex=False)
                           .str.replace('[^A-Za-z0-9_]+', '', regex=True))
    print("Column names standardized.")
    return cleaned_data

def convert_column_types(data: pd.DataFrame, column_types: dict) -> pd.DataFrame:
    """
    Converts the data type of specified columns.

    Args:
        data (pd.DataFrame): The DataFrame to modify.
        column_types (dict): A dictionary where keys are column names and values are the desired data types
                           (e.g., {'col1': 'int', 'col2': 'float', 'col3': 'category'}).

    Returns:
        pd.DataFrame: The DataFrame with column types converted.
    """
    cleaned_data = data.copy()
    for column, data_type in column_types.items():
        try:
            cleaned_data[column] = cleaned_data[column].astype(data_type)
            print(f"Column '{column}' converted to type '{data_type}'.")
        except KeyError:
            print(f"Column '{column}' not found in DataFrame.")
        except ValueError:
            print(f"Unable to convert column '{column}' to type '{data_type}'.  Check data for compatibility.")
    return cleaned_data

def cap_outliers(data: pd.DataFrame, columns: Union[str, List[str]] = 'all', iqr_multiplier: float = 1.5) -> pd.DataFrame:
    """
    Caps outliers in specified numerical columns using the IQR method.

    Args:
        data (pd.DataFrame): The DataFrame to cap outliers in.
        columns (Union[str, List[str]], optional): Columns to cap outliers in. Defaults to 'all'.
        iqr_multiplier (float, optional): Multiplier for the IQR to determine outlier boundaries. Defaults to 1.5.

    Returns:
        pd.DataFrame: The DataFrame with outliers capped.
    """
    cleaned_data = data.copy()

    if columns == 'all':
        cols_to_cap = cleaned_data.select_dtypes(include=np.number).columns.tolist()
    elif isinstance(columns, str):
        cols_to_cap = [columns] if columns in cleaned_data.columns else []
    elif isinstance(columns, list):
        cols_to_cap = [col for col in columns if col in cleaned_data.columns]
    else:
        raise ValueError("Invalid 'columns' argument. Must be 'all', a string, or a list of strings.")

    for col in cols_to_cap:
        Q1 = cleaned_data[col].quantile(0.25)
        Q3 = cleaned_data[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - iqr_multiplier * IQR
        upper_bound = Q3 + iqr_multiplier * IQR

        cleaned_data[col] = np.where(cleaned_data[col] < lower_bound, lower_bound, cleaned_data[col])
        cleaned_data[col] = np.where(cleaned_data[col] > upper_bound, upper_bound, cleaned_data[col])
        print(f"Outliers in column '{col}' capped to [{lower_bound:.2f}, {upper_bound:.2f}].")

    return cleaned_data

def normalize_data(data: pd.DataFrame, columns: Union[str, List[str]] = 'all', method: str = 'minmax') -> pd.DataFrame:
    """
    Normalizes numerical columns using either Min-Max scaling or Z-score standardization.

    Args:
        data (pd.DataFrame): The DataFrame to normalize.
        columns (Union[str, List[str]], optional): Columns to normalize. Defaults to 'all'.
        method (str, optional): Normalization method. Options: 'minmax', 'zscore'. Defaults to 'minmax'.

    Returns:
        pd.DataFrame: The normalized DataFrame.
    """
    cleaned_data = data.copy()

    if columns == 'all':
        cols_to_normalize = cleaned_data.select_dtypes(include=np.number).columns.tolist()
    elif isinstance(columns, str):
        cols_to_normalize = [columns] if columns in cleaned_data.columns else []
    elif isinstance(columns, list):
        cols_to_normalize = [col for col in columns if col in cleaned_data.columns]
    else:
        raise ValueError("Invalid 'columns' argument. Must be 'all', a string, or a list of strings.")

    for col in cols_to_normalize:
        if method == 'minmax':
            min_val = cleaned_data[col].min()
            max_val = cleaned_data[col].max()
            cleaned_data[col] = (cleaned_data[col] - min_val) / (max_val - min_val)
            print(f"Column '{col}' normalized using Min-Max scaling.")
        elif method == 'zscore':
            mean_val = cleaned_data[col].mean()
            std_val = cleaned_data[col].std()
            cleaned_data[col] = (cleaned_data[col] - mean_val) / std_val
            print(f"Column '{col}' normalized using Z-score standardization.")
        else:
            raise ValueError("Invalid normalization method. Choose 'minmax' or 'zscore'.")

    return cleaned_data

def bin_numeric_data(data: pd.DataFrame, column: str, bins: int = 10, labels: list = None) -> pd.DataFrame:
    """
    Bins a numerical column into discrete intervals.

    Args:
        data (pd.DataFrame): The DataFrame.
        column (str): The name of the numerical column to bin.
        bins (int, optional): The number of bins to create. Defaults to 10.
        labels (list, optional): Custom labels for the bins. Must have length equal to bins - 1. Defaults to None.

    Returns:
        pd.DataFrame: The DataFrame with the new binned column.
    """
    cleaned_data = data.copy()

    if column not in cleaned_data.columns:
        raise ValueError(f"Column '{column}' not found in DataFrame.")

    if not pd.api.types.is_numeric_dtype(cleaned_data[column]):
        raise ValueError(f"Column '{column}' is not numeric.")
    
    try:
        cleaned_data[column + '_binned'] = pd.cut(cleaned_data[column], bins=bins, labels = labels)
        print(f"Column '{column}' binned into {bins} intervals.")
    except ValueError as e:
        print(f"Error: {e}")
    
    return cleaned_data

def one_hot_encode(data: pd.DataFrame, columns: Union[str, List[str]] = 'all') -> pd.DataFrame:
    """
    Performs one-hot encoding on specified categorical columns.

    Args:
        data (pd.DataFrame): The DataFrame to encode.
        columns (Union[str, List[str]], optional): Columns to one-hot encode. Defaults to 'all'.

    Returns:
        pd.DataFrame: The DataFrame with one-hot encoded columns.
    """
    cleaned_data = data.copy()

    if columns == 'all':
        cols_to_encode = cleaned_data.select_dtypes(include=['object', 'category']).columns.tolist()
    elif isinstance(columns, str):
        cols_to_encode = [columns] if columns in cleaned_data.columns else []
    elif isinstance(columns, list):
        cols_to_encode = [col for col in columns if col in cleaned_data.columns]
    else:
        raise ValueError("Invalid 'columns' argument. Must be 'all', a string, or a list of strings.")

    for col in cols_to_encode:
        try:
            dummies = pd.get_dummies(cleaned_data[col], prefix=col, dummy_na = False)
            cleaned_data = pd.concat([cleaned_data, dummies], axis=1)
            cleaned_data.drop(col, axis=1, inplace=True)
            print(f"Column '{col}' one-hot encoded.")
        except Exception as e:
            print(f"Error during one-hot encoding of column '{col}': {e}")

    return cleaned_data

