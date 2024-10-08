# datai/visualization.py

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from pandas.plotting import parallel_coordinates

class Examples:
    """Class for generating example plots using built-in datasets from pandas and seaborn."""

    @staticmethod
    def bar_chart():
        """Generates two bar charts in a single image: one for the Titanic dataset and one for the Tips dataset."""
        # Load datasets
        titanic = sns.load_dataset("titanic")
        tips = sns.load_dataset("tips")

        # Create subplots
        fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 6))

        # Plot Titanic dataset: count of survivors by class
        sns.barplot(x="class", y="survived", data=titanic, ax=axes[0], errorbar=None)
        axes[0].set_title("Survival by Class - Titanic")
        axes[0].set_ylabel("Survival Rate")

        # Plot Tips dataset: total bill by day
        sns.barplot(x="day", y="total_bill", data=tips, ax=axes[1], errorbar=None)
        axes[1].set_title("Total Bill by Day - Tips")
        axes[1].set_ylabel("Average Total Bill")

        # Show the plot
        plt.show()

        # Description
        description = """
        This visualization displays two bar charts side-by-side: one for the Titanic dataset and one for the Tips dataset.
        
        The Titanic bar chart shows the survival rate by passenger class (First, Second, Third). We observe higher survival rates 
        in First Class compared to other classes.
        
        The Tips bar chart shows the average total bill by day of the week. This provides insight into which days generate the 
        highest revenue, with Saturday showing the highest average bill amount.
        """
        print(description)


    @staticmethod
    def scatter_plot():
        """Generates two scatter plots in a single image: one for the Iris dataset and one for the mpg dataset."""
        # Load datasets
        iris = sns.load_dataset("iris")
        mpg = sns.load_dataset("mpg")

        # Create subplots
        fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 6))

        # Plot Iris dataset
        sns.scatterplot(x="sepal_length", y="sepal_width", data=iris, hue="species", ax=axes[0])
        axes[0].set_title("Iris Dataset")

        # Plot mpg dataset
        sns.scatterplot(x="horsepower", y="mpg", data=mpg, hue="cylinders", ax=axes[1])
        axes[1].set_title("mpg Dataset")

        # Show the plot
        plt.show()

        # Description
        description = """
        This visualization displays two scatter plots side-by-side: one for the Iris dataset and one for the mpg dataset.
        The Iris plot shows the relationship between sepal length and sepal width, colored by species.
        The mpg plot shows the relationship between horsepower and miles per gallon, colored by the number of cylinders.
        """
        print(description)

    @staticmethod
    def line_chart():
        """Generates two line charts in a single image: one for the Flights dataset and one for the Tips dataset."""
        # Load datasets
        flights = sns.load_dataset("flights")
        tips = sns.load_dataset("tips")

        # Create subplots
        fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 6))

        # Plot Flights dataset: passengers over time
        sns.lineplot(x="year", y="passengers", data=flights, ax=axes[0], marker="o")
        axes[0].set_title("Passengers Over Time - Flights")
        axes[0].set_ylabel("Number of Passengers")

        # Plot Tips dataset: total bill over time (sorted by size as a proxy for order)
        tips_sorted = tips.sort_values("size")
        sns.lineplot(x=tips_sorted.index, y="total_bill", data=tips_sorted, ax=axes[1], marker="o")
        axes[1].set_title("Total Bill by Order Size - Tips")
        axes[1].set_ylabel("Total Bill")

        # Show the plot
        plt.show()

        # Description
        description = """
        This visualization displays two line charts side-by-side: one for the Flights dataset and one for the Tips dataset.
        
        The Flights line chart shows the number of passengers per year, highlighting the growth in air travel from 1949 to 1960.
        
        The Tips line chart shows how the total bill amount changes based on order size, where the X-axis represents each order 
        (sorted by party size), and the Y-axis represents the total bill. Larger parties tend to generate higher total bills.
        """
        print(description)


    @staticmethod
    def histogram():
        """Generates two histograms in a single image: one for the Titanic dataset and one for the Tips dataset."""
        # Load datasets
        titanic = sns.load_dataset("titanic")
        tips = sns.load_dataset("tips")

        # Create subplots
        fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 6))

        # Plot Titanic dataset: distribution of age
        sns.histplot(titanic['age'].dropna(), bins=20, kde=True, ax=axes[0], color='skyblue')
        axes[0].set_title("Age Distribution - Titanic")
        axes[0].set_xlabel("Age")
        axes[0].set_ylabel("Frequency")

        # Plot Tips dataset: distribution of total bill
        sns.histplot(tips['total_bill'], bins=20, kde=True, ax=axes[1], color='lightgreen')
        axes[1].set_title("Total Bill Distribution - Tips")
        axes[1].set_xlabel("Total Bill")
        axes[1].set_ylabel("Frequency")

        # Show the plot
        plt.show()

        # Description
        description = """
        This visualization displays two histograms side-by-side: one for the Titanic dataset and one for the Tips dataset.

        The Titanic histogram shows the distribution of passengers' ages, with most passengers falling between 20 and 40 years old. 
        A KDE curve (kernel density estimate) is overlaid to give a smooth estimate of the age distribution.

        The Tips histogram shows the distribution of total bills from the restaurant dataset. The majority of the bills fall 
        between $10 and $30, with a few higher amounts, indicating occasional larger bills.
        """
        print(description)

    @staticmethod
    def box_plot():
        """Generates two box plots in a single image: one for the Titanic dataset and one for the Tips dataset."""
        # Load datasets
        titanic = sns.load_dataset("titanic")
        tips = sns.load_dataset("tips")

        # Create subplots
        fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 6))

        # Plot Titanic dataset: age distribution by class
        sns.boxplot(x="class", y="age", data=titanic, ax=axes[0], palette="Set2")
        axes[0].set_title("Age Distribution by Class - Titanic")
        axes[0].set_ylabel("Age")

        # Plot Tips dataset: total bill distribution by day
        sns.boxplot(x="day", y="total_bill", data=tips, ax=axes[1], palette="Set1")
        axes[1].set_title("Total Bill Distribution by Day - Tips")
        axes[1].set_ylabel("Total Bill")

        # Show the plot
        plt.show()

        # Description
        description = """
        This visualization displays two box plots side-by-side: one for the Titanic dataset and one for the Tips dataset.

        The Titanic box plot shows the distribution of passengers' ages across different classes (First, Second, Third). The box plot 
        highlights the median age and spread, with First Class passengers tending to be older on average than those in Third Class.

        The Tips box plot shows the distribution of total bills by day of the week. This plot reveals the spread and outliers 
        for total bills on each day, with Sunday showing some of the highest bills and largest variability.
        """
        print(description)


    @staticmethod
    def heatmap():
        """Generates two heatmaps in a single image: one for the Correlation of the Titanic dataset and one for the Flights dataset."""
        # Load datasets
        titanic = sns.load_dataset("titanic")
        flights = sns.load_dataset("flights").pivot_table(index="month", columns="year", values="passengers", observed=False)

        # Filter Titanic dataset for only numeric columns (to avoid 'male'/'female' issue)
        titanic_numeric = titanic.select_dtypes(include=["float64", "int64"])

        # Create subplots
        fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(14, 6))

        # Plot Titanic dataset: correlation heatmap
        sns.heatmap(titanic_numeric.corr(), annot=True, cmap="coolwarm", ax=axes[0])
        axes[0].set_title("Titanic Dataset Correlation Heatmap")

        # Plot Flights dataset: passenger count heatmap
        sns.heatmap(flights, cmap="YlGnBu", ax=axes[1], linewidths=0.5, annot=True, fmt=".1f")
        axes[1].set_title("Flights Dataset Heatmap (Passengers per Year/Month)")

        # Show the plot
        plt.show()

        # Description
        description = """
        This visualization displays two heatmaps side-by-side: one for the Titanic dataset and one for the Flights dataset.

        The Titanic heatmap shows the correlation matrix between numeric variables, where darker shades indicate stronger 
        positive correlations (e.g., between 'fare' and 'class') and negative correlations (e.g., 'age' and 'survived').
        
        The Flights heatmap shows the number of air passengers for each month from 1949 to 1960. The darker areas indicate 
        higher passenger counts, with a visible growth in air travel over time, particularly in the later years.
        """
        print(description)

    @staticmethod
    def area_chart():
        """Generates two area charts in a single image: one for the Tips dataset and one for the Planets dataset."""
        # Load datasets
        tips = sns.load_dataset("tips").groupby("day").agg({"total_bill": "sum"}).reset_index()
        planets = sns.load_dataset("planets")

        # Aggregate planets data by year and count methods of discovery
        planets_by_year = planets.groupby("year").size().reset_index(name='discoveries')

        # Create subplots
        fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(14, 6))

        # Plot Tips dataset: total bill area chart by day
        axes[0].fill_between(tips["day"], tips["total_bill"], color="skyblue", alpha=0.5)
        sns.lineplot(x="day", y="total_bill", data=tips, ax=axes[0], marker="o", color="blue")
        axes[0].set_title("Total Bill Area Chart - Tips")
        axes[0].set_ylabel("Total Bill")

        # Plot Planets dataset: number of discoveries by year (using the planets dataset as a proxy)
        axes[1].fill_between(planets_by_year["year"], planets_by_year["discoveries"], color="lightgreen", alpha=0.5)
        sns.lineplot(x="year", y="discoveries", data=planets_by_year, ax=axes[1], marker="o", color="green")
        axes[1].set_title("Planet Discovery Count Over Time - Area Chart")
        axes[1].set_ylabel("Number of Discoveries")

        # Show the plot
        plt.show()

        # Description
        description = """
        This visualization displays two area charts side-by-side: one for the Tips dataset and one for the Planets dataset.

        The Tips area chart shows the total bill amounts for each day of the week, demonstrating that weekends (Saturday and Sunday) 
        have higher total bills compared to weekdays.
        
        The Planet Discovery Count area chart shows the number of exoplanet discoveries over time, grouped by year. The area 
        underneath the line represents the cumulative count of discoveries, highlighting an upward trend in discoveries over the years.
        """
        print(description)


    @staticmethod
    def pie_chart():
        """Generates two pie charts in a single image: one for the Tips dataset (total bill by day) and one for the Titanic dataset (survival rate by class)."""
        # Load datasets
        tips = sns.load_dataset("tips").groupby("day").agg({"total_bill": "sum"}).reset_index()
        titanic = sns.load_dataset("titanic").groupby("class").agg({"survived": "sum"}).reset_index()

        # Create subplots
        fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(14, 6))

        # Plot pie chart for total bill in the Tips dataset
        axes[0].pie(tips["total_bill"], labels=tips["day"], autopct='%1.1f%%', startangle=90, colors=sns.color_palette("Set2"))
        axes[0].set_title("Total Bill Distribution by Day - Tips")

        # Plot pie chart for survival rate by class in the Titanic dataset
        axes[1].pie(titanic["survived"], labels=titanic["class"], autopct='%1.1f%%', startangle=90, colors=sns.color_palette("Set3"))
        axes[1].set_title("Survival Rate by Class - Titanic")

        # Show the plot
        plt.show()

        # Description
        description = """
        This visualization displays two pie charts side-by-side: one for the Tips dataset and one for the Titanic dataset.

        The first pie chart shows the distribution of total bill amounts across different days of the week from the Tips dataset. 
        It helps visualize the proportion of total bills generated on each day, showing that Saturdays and Sundays have the highest shares.
        
        The second pie chart shows the survival rate based on passenger class from the Titanic dataset. It highlights that a larger proportion 
        of survivors were from the first class, with progressively fewer survivors in the second and third classes.
        """
        print(description)



    @staticmethod
    def violin_plot():
        """Generates two violin plots in a single image: one for the Tips dataset (total bill by day) and one for the Penguins dataset (flipper length by species)."""
        # Load datasets
        tips = sns.load_dataset("tips")
        penguins = sns.load_dataset("penguins")

        # Create subplots
        fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(14, 6))

        # Plot violin plot for total bill in the Tips dataset by day
        sns.violinplot(x="day", y="total_bill", data=tips, palette="muted", ax=axes[0], hue="sex", split=True)
        axes[0].set_title("Total Bill Distribution by Day - Tips")

        # Plot violin plot for flipper length in the Penguins dataset by species
        sns.violinplot(x="species", y="flipper_length_mm", data=penguins, palette="coolwarm", ax=axes[1], hue="sex", split=True)
        axes[1].set_title("Flipper Length Distribution by Species - Penguins")

        # Show the plot
        plt.show()

        # Description
        description = """
        This visualization displays two violin plots side-by-side: one for the Tips dataset and one for the Penguins dataset.

        The first violin plot shows the distribution of total bill amounts across different days of the week from the Tips dataset. 
        The width of the violin represents the density of the data, showing that Fridays and Saturdays have more variability in the total bill values.
        
        The second violin plot shows the distribution of flipper lengths across different penguin species from the Penguins dataset. 
        It illustrates the range and distribution of flipper lengths for each species, where Gentoo penguins tend to have longer flippers compared to the other species.
        """
        print(description)


    @staticmethod
    def parallel_coordinates_plot():
        """Generates a parallel coordinates plot using Pandas."""
        # Load dataset
        iris = sns.load_dataset("iris")

        # Create the plot
        plt.figure(figsize=(12, 6))
        parallel_coordinates(iris, "species", color=["blue", "green", "red"])

        # Add a title
        plt.title("Parallel Coordinates Plot for Iris Dataset")

        # Show the plot
        plt.show()

        # Description
        description = """
        This parallel coordinates plot visualizes the relationships between multiple features for different species in the Iris dataset.
        Each line represents a data point, and the color indicates the species.
        """
        print(description)
    
    @staticmethod
    def bubble_chart():
        """Generates a bubble chart showing the relationship between horsepower, weight, and acceleration in the mpg dataset."""
        # Load dataset
        mpg = sns.load_dataset("mpg").dropna()

        # Create bubble chart
        plt.figure(figsize=(10, 6))
        plt.scatter(x=mpg["horsepower"], y=mpg["weight"], s=mpg["acceleration"]*30, alpha=0.5, c=mpg["mpg"], cmap="viridis")
        plt.colorbar(label='Miles per Gallon (mpg)')
        plt.title("Horsepower vs. Weight with Acceleration as Bubble Size (mpg Dataset)")
        plt.xlabel("Horsepower")
        plt.ylabel("Weight")

        # Show the plot
        plt.show()

        # Description
        description = """
        This bubble chart shows the relationship between horsepower, weight, and acceleration in the 'mpg' dataset.
        - The X-axis represents horsepower, and the Y-axis represents vehicle weight.
        - The size of the bubbles represents acceleration, with larger bubbles indicating higher acceleration.
        - The color gradient indicates the miles per gallon (mpg), where darker shades represent lower fuel efficiency.
        This chart helps in visualizing how different car characteristics relate to one another.
        """
        print(description)

    @staticmethod
    def radial_chart():
        """Generates a radial chart (polar chart) showing the average tips by day of the week from the Tips dataset."""
        # Load dataset
        tips = sns.load_dataset("tips").groupby("day").agg({"tip": "mean"}).reset_index()

        # Create radial chart
        plt.figure(figsize=(8, 8))
        categories = tips["day"]
        values = tips["tip"]
        
        # Convert the data to radians
        angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
        values = np.concatenate((values, [values[0]]))  # Close the plot
        angles += angles[:1]

        # Create plot
        fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
        ax.fill(angles, values, color="blue", alpha=0.25)
        ax.plot(angles, values, color="blue", linewidth=2)

        # Add category labels
        ax.set_yticklabels([])
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(categories)

        # Title
        plt.title("Average Tip by Day (Tips Dataset)", size=15)

        # Show the plot
        plt.show()

        # Description
        description = """
        This radial chart (polar chart) shows the average tips by day of the week from the 'Tips' dataset.
        - Each spoke represents a day of the week, and the distance from the center represents the average tip amount.
        - The chart makes it easy to visualize which days generate higher tips.
        Radial charts are great for comparing multiple categories in a circular layout.
        """
        print(description)

