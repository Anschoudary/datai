# datai/visualization.py

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

class Examples:
    """Class for generating example plots using built-in datasets from pandas and seaborn."""

    @staticmethod
    def bar_chart():
        """Generates a bar chart using Seaborn's 'tips' dataset."""
        # Load dataset
        data = sns.load_dataset("tips")
        
        # Create the plot
        plt.figure(figsize=(10, 6))
        sns.barplot(x="day", y="total_bill", data=data, ci=None, palette="muted")
        
        # Add a title and labels
        plt.title("Average Total Bill by Day")
        plt.xlabel("Day of the Week")
        plt.ylabel("Average Total Bill")
        
        # Show the plot
        plt.show()
        
        # Description
        description = """
        This bar chart displays the average total bill amount by day of the week from the 'tips' dataset.
        Each bar represents the average total bill for that particular day, with the height of the bar corresponding to the bill amount.
        The dataset includes data about the total bill, tips, sex, smoker status, day, time, and size of the party.
        """
        print(description)

    @staticmethod
    def scatter_plot():
        """Generates a scatter plot using Seaborn's 'iris' dataset."""
        # Load dataset
        data = sns.load_dataset("iris")
        
        # Create the plot
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x="sepal_length", y="sepal_width", hue="species", data=data, palette="deep")
        
        # Add a title and labels
        plt.title("Sepal Length vs Sepal Width by Species")
        plt.xlabel("Sepal Length (cm)")
        plt.ylabel("Sepal Width (cm)")
        
        # Show the plot
        plt.show()
        
        # Description
        description = """
        This scatter plot displays the relationship between sepal length and sepal width for different iris species from the 'iris' dataset.
        Each point represents an individual flower, with different colors indicating different species.
        The plot helps to visualize how sepal dimensions vary between species.
        """
        print(description)

    @staticmethod
    def line_chart():
        """Generates a line chart using Pandas' 'air_quality' dataset."""
        # Load dataset
        data = pd.read_csv("https://raw.githubusercontent.com/pandas-dev/pandas/master/doc/data/air_quality_no2.csv", index_col=0, parse_dates=True)
        
        # Create the plot
        plt.figure(figsize=(10, 6))
        data.plot.line()
        
        # Add a title and labels
        plt.title("NO2 Concentration Over Time")
        plt.xlabel("Date")
        plt.ylabel("NO2 Concentration (µg/m³)")
        
        # Show the plot
        plt.show()
        
        # Description
        description = """
        This line chart displays the NO2 concentration over time for different locations using the 'air_quality' dataset.
        Each line represents the NO2 levels at a specific location, showing how air quality changes over time.
        """
        print(description)

    @staticmethod
    def histogram():
        """Generates a histogram using Seaborn's 'diamonds' dataset."""
        # Load dataset
        data = sns.load_dataset("diamonds")
        
        # Create the plot
        plt.figure(figsize=(10, 6))
        sns.histplot(data["carat"], bins=30, kde=True, color="purple")
        
        # Add a title and labels
        plt.title("Distribution of Diamond Carat Weights")
        plt.xlabel("Carat Weight")
        plt.ylabel("Frequency")
        
        # Show the plot
        plt.show()
        
        # Description
        description = """
        This histogram displays the distribution of diamond carat weights from the 'diamonds' dataset.
        The x-axis represents the carat weight, and the y-axis represents the frequency of diamonds with that carat weight.
        A KDE (Kernel Density Estimate) is also plotted to show the probability density function of the data.
        """
        print(description)

    @staticmethod
    def box_plot():
        """Generates a box plot using Seaborn's 'tips' dataset."""
        # Load dataset
        data = sns.load_dataset("tips")
        
        # Create the plot
        plt.figure(figsize=(10, 6))
        sns.boxplot(x="day", y="total_bill", data=data, palette="pastel")
        
        # Add a title and labels
        plt.title("Box Plot of Total Bill by Day")
        plt.xlabel("Day of the Week")
        plt.ylabel("Total Bill")
        
        # Show the plot
        plt.show()
        
        # Description
        description = """
        This box plot displays the distribution of total bill amounts by day of the week using the 'tips' dataset.
        The plot shows the median, quartiles, and outliers, providing a summary of how bills vary across days.
        """
        print(description)
