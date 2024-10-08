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
                sns.pairplot(data=dataset, hue=categorical_cols[0] if categorical_cols.size > 0 else None)
                plt.show()
                print("- Countplot: To visualize the distribution of categorical columns.")
                display_plot(sns.countplot, x=categorical_cols[0], data=dataset)
                print("- Boxplot: To visualize the distribution of numeric data grouped by a categorical column.")
                display_plot(sns.boxplot, x=categorical_cols[0], y=numeric_cols[0], data=dataset)
                print("- Violin Plot: To visualize the distribution of numeric data grouped by a categorical column.")
                display_plot(sns.violinplot, x=categorical_cols[0], y=numeric_cols[0], data=dataset)
                print("- Heatmap: To visualize the correlation matrix of numeric columns.")
                display_plot(sns.heatmap, data=dataset[numeric_cols].corr(), annot=True, cmap='coolwarm', linewidths=0.5)
            else:
                print("Suggested plots:")
                print("- Histogram: For distribution of numeric data.")
                display_plot(sns.histplot, x=numeric_cols[0], data=dataset)
                print("- Boxplot: For distribution and outliers of numeric data.")
                display_plot(sns.boxplot, y=numeric_cols[0], data=dataset)
                print("- Density Plot: For distribution of numeric data.")
                display_plot(sns.kdeplot, x=numeric_cols[0], data=dataset, fill=True)
                print("- Line Chart: For trends over time or ordered numeric data.")
                display_plot(plt.plot, x=dataset.index, y=dataset[numeric_cols[0]], marker='o')
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
    def bar_chart(data, x_col, y_col):
        """Plot a bar chart."""
        plt.figure(figsize=(10, 6))
        plt.bar(data[x_col], data[y_col], color='blue')
        plt.xlabel(x_col)
        plt.ylabel(y_col)
        plt.title(f'{y_col} by {x_col}')
        plt.show()
        print(f"Bar Chart: Displaying {y_col} by {x_col}.")

    @staticmethod
    def line_chart(data, x_col, y_col):
        """Plot a line chart."""
        plt.figure(figsize=(10, 6))
        plt.plot(data[x_col], data[y_col], color='green', marker='o')
        plt.xlabel(x_col)
        plt.ylabel(y_col)
        plt.title(f'{y_col} over {x_col}')
        plt.grid(True)
        plt.show()
        print(f"Line Chart: Displaying {y_col} over {x_col}.")

    @staticmethod
    def scatter_plot(data, x_col, y_col):
        """Plot a scatter plot for the specified x and y columns."""
        plt.figure(figsize=(10, 6))
        plt.scatter(data[x_col], data[y_col], color='red')
        plt.xlabel(x_col)
        plt.ylabel(y_col)
        plt.title(f'{y_col} vs {x_col}')
        plt.grid(True)
        plt.show()
        print(f"Scatter Plot: Displaying {y_col} vs {x_col}.")

    @staticmethod
    def histogram(data, col):
        """Plot a histogram for a specific column."""
        plt.figure(figsize=(10, 6))
        plt.hist(data[col], bins=15, color='purple', edgecolor='black')
        plt.title(f'Histogram of {col}')
        plt.xlabel(col)
        plt.ylabel('Frequency')
        plt.show()
        print(f"Histogram: Displaying distribution of {col}.")

    @staticmethod
    def heatmap(data, cols):
        """Plot a heatmap for the correlation matrix of specific columns."""
        plt.figure(figsize=(12, 8))
        correlation_matrix = data[cols].corr()
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
        plt.title('Heatmap of Correlation Matrix')
        plt.show()
        print("Heatmap: Displaying correlation matrix of the dataset.")

    @staticmethod
    def violin_plot(data, x_col, y_col):
        """Plot a violin plot for the specified x and y columns."""
        plt.figure(figsize=(10, 6))
        sns.violinplot(x=x_col, y=y_col, data=data)
        plt.xlabel(x_col)
        plt.ylabel(y_col)
        plt.title(f'Violin Plot of {y_col} by {x_col}')
        plt.show()
        print(f"Violin Plot: Displaying {y_col} by {x_col}.")

    @staticmethod
    def density_plot(data, col):
        """Plot a density plot for a specific numeric column."""
        plt.figure(figsize=(10, 6))
        sns.kdeplot(data[col], fill=True, color='blue')
        plt.xlabel(col)
        plt.title(f'Density Plot of {col}')
        plt.show()
        print(f"Density Plot: Displaying distribution of {col}.")


# Test the AutoPlot class
if __name__ == '__main__':
    # Create a sample dataset
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Age': [25, 30, 35, 40, 45],
        'Salary': [50000, 60000, 75000, 80000, 90000],
    }
    df = pd.DataFrame(data)

    # Test the bar_chart method
    AutoPlot.auto_plot(df)