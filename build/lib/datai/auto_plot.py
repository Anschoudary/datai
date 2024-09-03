# datai/auto_plot.py

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

class AutoPlot:
    """Class for automatically plotting the right type of graph based on the dataset."""

    @staticmethod
    def auto_plot(data: pd.DataFrame, x_column: str = None, y_column: str = None):
        """
        Automatically plot the most suitable graph for the given data.
        
        Parameters:
        - data: Pandas DataFrame containing the dataset.
        - x_column: The column to be used on the x-axis (optional).
        - y_column: The column to be used on the y-axis (optional).
        """
        # If x_column and y_column are not provided, automatically select them
        if x_column is None or y_column is None:
            numeric_cols = data.select_dtypes(include=[np.number]).columns
            categorical_cols = data.select_dtypes(include=['object']).columns

            if len(numeric_cols) >= 2:
                x_column, y_column = numeric_cols[:2]
            elif len(numeric_cols) == 1 and len(categorical_cols) >= 1:
                x_column, y_column = categorical_cols[0], numeric_cols[0]
            else:
                print("Not enough data for automatic plotting. Please provide specific columns.")
                return

        x_data = data[x_column]
        y_data = data[y_column]
        
        if np.issubdtype(y_data.dtype, np.number):
            if len(x_data.unique()) < 20:
                AutoPlot.plot_bar_chart(x_data, y_data)
            else:
                AutoPlot.plot_line_chart(x_data, y_data)
        else:
            AutoPlot.plot_scatter_plot(x_data, y_data)

    @staticmethod
    def plot_bar_chart(x_data, y_data):
        """Plot a bar chart."""
        plt.figure(figsize=(10, 6))
        plt.bar(x_data, y_data, color='blue')
        plt.xlabel(x_data.name)
        plt.ylabel(y_data.name)
        plt.title(f'{y_data.name} by {x_data.name}')
        plt.show()
        
        print(f"Bar Chart: Displaying {y_data.name} by {x_data.name}.")

    @staticmethod
    def plot_line_chart(x_data, y_data):
        """Plot a line chart."""
        plt.figure(figsize=(10, 6))
        plt.plot(x_data, y_data, color='green', marker='o')
        plt.xlabel(x_data.name)
        plt.ylabel(y_data.name)
        plt.title(f'{y_data.name} over {x_data.name}')
        plt.grid(True)
        plt.show()
        
        print(f"Line Chart: Displaying {y_data.name} over {x_data.name}.")

    @staticmethod
    def plot_scatter_plot(x_data, y_data):
        """Plot a scatter plot."""
        plt.figure(figsize=(10, 6))
        plt.scatter(x_data, y_data, color='red')
        plt.xlabel(x_data.name)
        plt.ylabel(y_data.name)
        plt.title(f'{y_data.name} vs {x_data.name}')
        plt.grid(True)
        plt.show()
        
        print(f"Scatter Plot: Displaying {y_data.name} vs {x_data.name}.")

    @staticmethod
    def plot_histogram(data):
        """Plot histograms for all numeric columns in the dataset."""
        numeric_cols = data.select_dtypes(include=[np.number]).columns
        data[numeric_cols].hist(bins=15, figsize=(15, 10), color='purple', edgecolor='black')
        plt.suptitle('Histograms of Numeric Columns', fontsize=16)
        plt.show()
        
        print("Histograms: Displaying distribution of all numeric columns.")
