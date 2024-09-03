# datai/data_cleaning.py

import pandas as pd

class DataCleaning:
    """Class for cleaning and preprocessing datasets."""

    def __init__(self, data: pd.DataFrame):
        """Initialize with a dataset."""
        self.data = data
    
    def show_details(self):
        """Display details about the dataset."""
        print("Dataset Information:")
        print(self.data.info())
        print("\nFirst 5 rows of the dataset:")
        print(self.data.head())
        print("\nMissing values in each column:")
        print(self.data.isnull().sum())
        print("\nBasic statistics of the dataset:")
        print(self.data.describe())

    def clean_missing_data(self):
        """Handle missing data by filling with median for numeric columns and mode for categorical columns."""
        for column in self.data.columns:
            if self.data[column].dtype == "object":
                # Fill missing values in categorical columns with the mode
                self.data[column].fillna(self.data[column].mode()[0], inplace=True)
            else:
                # Fill missing values in numeric columns with the median
                self.data[column].fillna(self.data[column].median(), inplace=True)
        print("\nMissing values have been handled.")
    
    def remove_outliers(self, threshold=1.5):
        """Remove outliers using the IQR method."""
        numeric_cols = self.data.select_dtypes(include=['float64', 'int64']).columns
        for col in numeric_cols:
            Q1 = self.data[col].quantile(0.25)
            Q3 = self.data[col].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - threshold * IQR
            upper_bound = Q3 + threshold * IQR
            # Filter out outliers
            self.data = self.data[(self.data[col] >= lower_bound) & (self.data[col] <= upper_bound)]
        print("\nOutliers have been removed.")
    
    def normalize_data(self):
        """Normalize numeric data to a 0-1 scale."""
        numeric_cols = self.data.select_dtypes(include=['float64', 'int64']).columns
        self.data[numeric_cols] = (self.data[numeric_cols] - self.data[numeric_cols].min()) / (self.data[numeric_cols].max() - self.data[numeric_cols].min())
        print("\nNumeric data has been normalized.")
    
    def get_cleaned_data(self):
        """Return the cleaned and preprocessed dataset."""
        self.show_details()
        self.clean_missing_data()
        self.remove_outliers()
        self.normalize_data()
        print("\nDataset has been cleaned and preprocessed.")

        return self.data
