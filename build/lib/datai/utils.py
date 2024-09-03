# datai/utils.py

import pandas as pd
import numpy as np

class Utils:
    """Utility functions for data preprocessing and validation."""

    @staticmethod
    def validate_dataset(data):
        """
        Validate the input dataset to ensure it's a proper DataFrame.

        Parameters:
        - data: The dataset to validate.

        Returns:
        - bool: True if valid, raises an error if not.
        """
        if not isinstance(data, pd.DataFrame):
            raise ValueError("The provided data is not a pandas DataFrame.")
        if data.empty:
            raise ValueError("The provided DataFrame is empty.")
        return True

    @staticmethod
    def handle_missing_values(data, method='drop', fill_value=None):
        """
        Handle missing values in the dataset.

        Parameters:
        - data: The dataset with potential missing values.
        - method: The method to handle missing values ('drop', 'fill').
        - fill_value: The value to fill missing values with if method is 'fill' (optional).

        Returns:
        - pd.DataFrame: The dataset with missing values handled.
        """
        if method == 'drop':
            data = data.dropna()
        elif method == 'fill':
            if fill_value is None:
                raise ValueError("Fill value must be provided when method is 'fill'.")
            data = data.fillna(fill_value)
        else:
            raise ValueError("Invalid method for handling missing values. Use 'drop' or 'fill'.")
        
        return data

    @staticmethod
    def summarize_data(data):
        """
        Generate a summary of the dataset.

        Parameters:
        - data: The dataset to summarize.

        Returns:
        - dict: A summary including basic stats and info.
        """
        summary = {
            "Shape": data.shape,
            "Columns": data.columns.tolist(),
            "Data Types": data.dtypes.to_dict(),
            "Missing Values": data.isnull().sum().to_dict(),
            "Summary Statistics": data.describe().to_dict()
        }
        return summary

    @staticmethod
    def normalize_data(data, method='min-max'):
        """
        Normalize numeric columns in the dataset.

        Parameters:
        - data: The dataset to normalize.
        - method: The normalization method ('min-max', 'z-score').

        Returns:
        - pd.DataFrame: The normalized dataset.
        """
        numeric_cols = data.select_dtypes(include=[np.number]).columns
        
        if method == 'min-max':
            data[numeric_cols] = (data[numeric_cols] - data[numeric_cols].min()) / (data[numeric_cols].max() - data[numeric_cols].min())
        elif method == 'z-score':
            data[numeric_cols] = (data[numeric_cols] - data[numeric_cols].mean()) / data[numeric_cols].std()
        else:
            raise ValueError("Invalid normalization method. Use 'min-max' or 'z-score'.")
        
        return data

    @staticmethod
    def split_data(data, target_column, test_size=0.2, random_state=None):
        """
        Split the dataset into training and testing sets.

        Parameters:
        - data: The dataset to split.
        - target_column: The column to predict (y).
        - test_size: The proportion of the dataset to include in the test split (default 0.2).
        - random_state: The seed used by the random number generator (optional).

        Returns:
        - pd.DataFrame: Training and testing features and labels.
        """
        from sklearn.model_selection import train_test_split

        X = data.drop(columns=[target_column])
        y = data[target_column]
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
        
        return X_train, X_test, y_train, y_test
