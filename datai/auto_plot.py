# datai/auto_plot.py

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

class AutoPlot:
    """Class for automatically plotting the right type of graph based on the dataset."""

    @staticmethod
    def auto_plot(dataset):
        """
        Suggests a type of plot based on the characteristics of the dataset and provides examples.

        Parameters:
        dataset (pd.DataFrame): The dataset to analyze.

        Returns:
        None
        """
        if not isinstance(dataset, pd.DataFrame):
            raise ValueError("The input dataset must be a pandas DataFrame.")
        
        # Analyze the dataset
        num_rows, num_cols = dataset.shape
        data_types = dataset.dtypes
        numeric_cols = data_types[data_types != 'object'].index
        categorical_cols = data_types[data_types == 'object'].index

        # Print dataset summary
        print(f"Number of rows: {num_rows}")
        print(f"Number of columns: {num_cols}")
        print(f"Numeric columns: {numeric_cols.tolist()}")
        print(f"Categorical columns: {categorical_cols.tolist()}")

    # Function to display plots
        def display_plot(plot_func, **kwargs):
            plt.figure(figsize=(10, 6))
            plot_func(**kwargs)
            plt.show()

        # Suggest plot types based on dataset characteristics
        if numeric_cols.size > 0:
            if categorical_cols.size > 0:
                print("Suggested plots:")
                print("- Pairplot: To visualize relationships between numeric columns.")
                display_plot(sns.pairplot, data=dataset, hue=categorical_cols[0] if categorical_cols.size > 0 else None)
                print("- Countplot: To visualize the distribution of categorical columns.")
                display_plot(sns.countplot, x=categorical_cols[0], data=dataset)
                print("- Boxplot: To visualize the distribution of numeric data grouped by a categorical column.")
                display_plot(sns.boxplot, x=categorical_cols[0], y=numeric_cols[0], data=dataset)
            else:
                print("Suggested plots:")
                print("- Histogram: For distribution of numeric data.")
                display_plot(sns.histplot, x=numeric_cols[0], data=dataset)
                print("- Boxplot: For distribution and outliers of numeric data.")
                display_plot(sns.boxplot, y=numeric_cols[0], data=dataset)
        else:
            if categorical_cols.size > 0:
                print("Suggested plots:")
                print("- Countplot: For frequency of categories.")
                display_plot(sns.countplot, x=categorical_cols[0], data=dataset)
                print("- Pie chart: For proportion of categories.")
                category_counts = dataset[categorical_cols[0]].value_counts()
                plt.figure(figsize=(10, 6))
                plt.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%')
                plt.title('Pie Chart of Categorical Data')
                plt.show()
            else:
                print("The dataset does not have clear numeric or categorical features for visualization.")

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

    
