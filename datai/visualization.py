import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from pandas.plotting import parallel_coordinates
import pandas as pd  # Import pandas

def bar_chart(data="titanic", x=None, y=None, title=None, x_label=None, y_label=None):
    """
    Generates a bar chart for a given dataset and specified columns.

    Args:
        data (str or pd.DataFrame, optional): The dataset to use. Defaults to "titanic".
            Can be "titanic", "tips", or a pandas DataFrame.
        x (str, optional): The column to use for the x-axis. Defaults to None.
        y (str, optional): The column to use for the y-axis. Defaults to None.
        title (str, optional): The title of the plot. Defaults to None.
        x_label (str, optional): The label for the x-axis. Defaults to None.
        y_label (str, optional): The label for the y-axis. Defaults to None.
    """

    # Example 1: Titanic Dataset
    if data == "titanic":
        df = sns.load_dataset("titanic")
        x = "class" if x is None else x
        y = "survived" if y is None else y
        title = "Survival by Class - Titanic" if title is None else title
        x_label = "Class" if x_label is None else x_label
        y_label = "Survival Rate" if y_label is None else y_label

        plt.figure(figsize=(8, 6))
        sns.barplot(x=x, y=y, data=df, errorbar=None)
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.show()
        print(f"Bar chart of {x} vs {y} from the Titanic dataset.")

    # Example 2: Tips Dataset
    elif data == "tips":
        df = sns.load_dataset("tips")
        x = "day" if x is None else x
        y = "total_bill" if y is None else y
        title = "Total Bill by Day - Tips" if title is None else title
        x_label = "Day" if x_label is None else x_label
        y_label = "Average Total Bill" if y_label is None else y_label

        plt.figure(figsize=(8, 6))
        sns.barplot(x=x, y=y, data=df, errorbar=None)
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.show()
        print(f"Bar chart of {x} vs {y} from the Tips dataset.")

    elif isinstance(data, pd.DataFrame):
        df = data
        if x is None or y is None:
            raise ValueError("x and y parameters must be specified for a custom DataFrame.")
        title = "Bar Chart" if title is None else title
        x_label = x if x_label is None else x_label
        y_label = y if y_label is None else y_label

        plt.figure(figsize=(8, 6))
        sns.barplot(x=x, y=y, data=df, errorbar=None)
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.show()
        print(f"Bar chart of {x} vs {y} from the provided DataFrame.")
    else:
        raise ValueError("Invalid dataset name. Choose 'titanic', 'tips', or provide a pandas DataFrame.")

def scatter_plot(data="iris", x=None, y=None, hue=None, title=None, x_label=None, y_label=None):
    """
    Generates a scatter plot for a given dataset.

    Args:
        data (str or pd.DataFrame, optional): The dataset to use. Defaults to "iris".
            Can be "iris", "mpg", or a pandas DataFrame.
        x (str, optional): The column to use for the x-axis. Defaults to None.
        y (str, optional): The column to use for the y-axis. Defaults to None.
        hue (str, optional): The column to use for the color hue. Defaults to None.
        title (str, optional): The title of the plot. Defaults to None.
        x_label (str, optional): The label for the x-axis. Defaults to None.
        y_label (str, optional): The label for the y-axis. Defaults to None.
    """

    # Example 1: Iris Dataset
    if data == "iris":
        df = sns.load_dataset("iris")
        x = "sepal_length" if x is None else x
        y = "sepal_width" if y is None else y
        hue = "species" if hue is None else hue
        title = "Iris Dataset - Sepal Length vs Sepal Width" if title is None else title
        x_label = "Sepal Length" if x_label is None else x_label
        y_label = "Sepal Width" if y_label is None else y_label

        plt.figure(figsize=(8, 6))
        sns.scatterplot(x=x, y=y, data=df, hue=hue)
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.show()
        print(f"Scatter plot of {x} vs {y} from the Iris dataset.")

    # Example 2: MPG Dataset
    elif data == "mpg":
        df = sns.load_dataset("mpg")
        x = "horsepower" if x is None else x
        y = "mpg" if y is None else y
        hue = "cylinders" if hue is None else hue
        title = "MPG Dataset - Horsepower vs MPG" if title is None else title
        x_label = "Horsepower" if x_label is None else x_label
        y_label = "Miles Per Gallon" if y_label is None else y_label

        plt.figure(figsize=(8, 6))
        sns.scatterplot(x=x, y=y, data=df, hue=hue)
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.show()
        print(f"Scatter plot of {x} vs {y} from the MPG dataset.")

    elif isinstance(data, pd.DataFrame):
        df = data
        if x is None or y is None:
            raise ValueError("x and y parameters must be specified for a custom DataFrame.")
        title = "Scatter Plot" if title is None else title
        x_label = x if x_label is None else x_label
        y_label = y if y_label is None else y_label

        plt.figure(figsize=(8, 6))
        sns.scatterplot(x=x, y=y, data=df, hue=hue)
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.show()
        print(f"Scatter plot of {x} vs {y} from the provided DataFrame.")
    else:
        raise ValueError("Invalid dataset name. Choose 'iris', 'mpg', or provide a pandas DataFrame.")

def line_chart(data="flights", x=None, y=None, title=None, x_label=None, y_label=None):
    """
    Generates a line chart for a given dataset.

    Args:
        data (str or pd.DataFrame, optional): The dataset to use. Defaults to "flights".
            Can be "flights", "tips", or a pandas DataFrame.
        x (str, optional): The column to use for the x-axis. Defaults to None.
        y (str, optional): The column to use for the y-axis. Defaults to None.
        title (str, optional): The title of the plot. Defaults to None.
        x_label (str, optional): The label for the x-axis. Defaults to None.
        y_label (str, optional): The label for the y-axis. Defaults to None.
    """

    # Example 1: Flights Dataset
    if data == "flights":
        df = sns.load_dataset("flights")
        x = "year" if x is None else x
        y = "passengers" if y is None else y
        title = "Passengers Over Time - Flights" if title is None else title
        x_label = "Year" if x_label is None else x_label
        y_label = "Number of Passengers" if y_label is None else y_label

        plt.figure(figsize=(8, 6))
        sns.lineplot(x=x, y=y, data=df, marker="o")
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.show()
        print(f"Line chart of {x} vs {y} from the Flights dataset.")

    # Example 2: Tips Dataset
    elif data == "tips":
        df = sns.load_dataset("tips").sort_values("size")
        x = df.index if x is None else x
        y = "total_bill" if y is None else y
        title = "Total Bill by Order Size - Tips" if title is None else title
        x_label = "Order Index" if x_label is None else x_label
        y_label = "Total Bill" if y_label is None else y_label

        plt.figure(figsize=(8, 6))
        sns.lineplot(x=x, y=y, data=df, marker="o")
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.show()
        print(f"Line chart of {x} vs {y} from the Tips dataset.")

    elif isinstance(data, pd.DataFrame):
        df = data
        if x is None or y is None:
            raise ValueError("x and y parameters must be specified for a custom DataFrame.")
        title = "Line Chart" if title is None else title
        x_label = x if x_label is None else x_label
        y_label = y if y_label is None else y_label

        plt.figure(figsize=(8, 6))
        sns.lineplot(x=x, y=y, data=df, marker="o")
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.show()
        print(f"Line chart of {x} vs {y} from the provided DataFrame.")
    else:
        raise ValueError("Invalid dataset name. Choose 'flights', 'tips', or provide a pandas DataFrame.")

def histogram(data="titanic", column=None, title=None, x_label=None, y_label=None, bins=20, color='skyblue'):
    """
    Generates a histogram for a given dataset and column.

    Args:
        data (str or pd.DataFrame, optional): The dataset to use. Defaults to "titanic".
            Can be "titanic", "tips", or a pandas DataFrame.
        column (str, optional): The column to plot the histogram for. Defaults to None.
        title (str, optional): The title of the plot. Defaults to None.
        x_label (str, optional): The label for the x-axis. Defaults to None.
        y_label (str, optional): The label for the y-axis. Defaults to None.
        bins (int, optional): The number of bins to use for the histogram. Defaults to 20.
        color (str, optional): The color of the histogram. Defaults to 'skyblue'.
    """

    # Example 1: Titanic Dataset
    if data == "titanic":
        df = sns.load_dataset("titanic")
        column = 'age' if column is None else column
        column_data = df['age'].dropna()
        title = "Age Distribution - Titanic" if title is None else title
        x_label = "Age" if x_label is None else x_label
        y_label = "Frequency" if y_label is None else y_label

        plt.figure(figsize=(8, 6))
        sns.histplot(column_data, bins=bins, kde=True, color=color)
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.show()
        print(f"Histogram of {column} from the Titanic dataset.")

    # Example 2: Tips Dataset
    elif data == "tips":
        df = sns.load_dataset("tips")
        column = 'total_bill' if column is None else column
        column_data = df['total_bill']
        title = "Total Bill Distribution - Tips" if title is None else title
        x_label = "Total Bill" if x_label is None else x_label
        y_label = "Frequency" if y_label is None else y_label

        plt.figure(figsize=(8, 6))
        sns.histplot(column_data, bins=bins, kde=True, color=color)
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.show()
        print(f"Histogram of {column} from the Tips dataset.")

    elif isinstance(data, pd.DataFrame):
        df = data
        if column is None:
            raise ValueError("Column parameter must be specified for a custom DataFrame.")
        column_data = df[column].dropna()
        title = f"Distribution of {column}" if title is None else title
        x_label = column if x_label is None else x_label
        y_label = "Frequency" if y_label is None else y_label

        plt.figure(figsize=(8, 6))
        sns.histplot(column_data, bins=bins, kde=True, color=color)
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.show()
        print(f"Histogram of {column} from the provided DataFrame.")

    else:
        raise ValueError("Invalid dataset name. Choose 'titanic', 'tips', or provide a pandas DataFrame.")

def box_plot(data="titanic", x=None, y=None, title=None, x_label=None, y_label=None, palette="Set2"):
    """
    Generates a box plot for a given dataset.

    Args:
        data (str or pd.DataFrame, optional): The dataset to use. Defaults to "titanic".
            Can be "titanic", "tips", or a pandas DataFrame.
        x (str, optional): The column to use for the x-axis. Defaults to None.
        y (str, optional): The column to use for the y-axis. Defaults to None.
        title (str, optional): The title of the plot. Defaults to None.
        x_label (str, optional): The label for the x-axis. Defaults to None.
        y_label (str, optional): The label for the y-axis. Defaults to None.
        palette (str, optional): The color palette to use. Defaults to "Set2".
    """

    # Example 1: Titanic Dataset
    if data == "titanic":
        df = sns.load_dataset("titanic")
        x = "class" if x is None else x
        y = "age" if y is None else y
        title = "Age Distribution by Class - Titanic" if title is None else title
        x_label = "Class" if x_label is None else x_label
        y_label = "Age" if y_label is None else y_label

        plt.figure(figsize=(8, 6))
        sns.boxplot(x=x, y=y, data=df, palette=palette)
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.show()
        print(f"Box plot of {y} by {x} from the Titanic dataset.")

    # Example 2: Tips Dataset
    elif data == "tips":
        df = sns.load_dataset("tips")
        x = "day" if x is None else x
        y = "total_bill" if y is None else y
        title = "Total Bill Distribution by Day - Tips" if title is None else title
        x_label = "Day" if x_label is None else x_label
        y_label = "Total Bill" if y_label is None else y_label

        plt.figure(figsize=(8, 6))
        sns.boxplot(x=x, y=y, data=df, palette=palette)
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.show()
        print(f"Box plot of {y} by {x} from the Tips dataset.")

    elif isinstance(data, pd.DataFrame):
        df = data
        if x is None or y is None:
            raise ValueError("x and y parameters must be specified for a custom DataFrame.")
        title = "Box Plot" if title is None else title
        x_label = x if x_label is None else x_label
        y_label = y if y_label is None else y_label

        plt.figure(figsize=(8, 6))
        sns.boxplot(x=x, y=y, data=df, palette=palette)
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.show()
        print(f"Box plot of {y} by {x} from the provided DataFrame.")

    else:
        raise ValueError("Invalid dataset name. Choose 'titanic', 'tips', or provide a pandas DataFrame.")

def heatmap(data="titanic", corr_method="pearson", title=None, cmap="coolwarm"):
    """
    Generates a heatmap for a given dataset.

    Args:
        data (str or pd.DataFrame, optional): The dataset to use. Defaults to "titanic".
            Can be "titanic", "flights", or a pandas DataFrame.
        corr_method (str, optional): The correlation method to use. Defaults to "pearson".
        title (str, optional): The title of the plot. Defaults to None.
        cmap (str, optional): The color map to use. Defaults to "coolwarm".
    """

    # Example 1: Titanic Dataset
    if data == "titanic":
        df = sns.load_dataset("titanic").select_dtypes(include=["float64", "int64"])
        title = "Titanic Dataset Correlation Heatmap" if title is None else title

        plt.figure(figsize=(10, 8))
        sns.heatmap(df.corr(method=corr_method), annot=True, cmap=cmap, linewidths=0.5, fmt=".2f")
        plt.title(title)
        plt.show()
        print(f"Heatmap for the Titanic dataset.")

    # Example 2: Flights Dataset
    elif data == "flights":
        df = sns.load_dataset("flights").pivot_table(index="month", columns="year", values="passengers", observed=False)
        title = "Flights Dataset Heatmap (Passengers per Year/Month)" if title is None else title
        cmap = "YlGnBu"

        plt.figure(figsize=(10, 8))
        sns.heatmap(df, annot=True, cmap=cmap, linewidths=0.5, fmt=".2f")
        plt.title(title)
        plt.show()
        print(f"Heatmap for the Flights dataset.")

    elif isinstance(data, pd.DataFrame):
        df = data.corr(method=corr_method)
        title = "Correlation Heatmap" if title is None else title

        plt.figure(figsize=(10, 8))
        sns.heatmap(df, annot=True, cmap=cmap, linewidths=0.5, fmt=".2f")
        plt.title(title)
        plt.show()
        print(f"Heatmap for the provided DataFrame.")

    else:
        raise ValueError("Invalid dataset name. Choose 'titanic', 'flights', or provide a pandas DataFrame.")

def area_chart(data="tips", x=None, y=None, title=None, x_label=None, y_label=None, color="skyblue"):
    """
    Generates an area chart for a given dataset.

    Args:
        data (str or pd.DataFrame, optional): The dataset to use. Defaults to "tips".
            Can be "tips", "planets", or a pandas DataFrame.
        x (str, optional): The column to use for the x-axis. Defaults to None.
        y (str, optional): The column to use for the y-axis. Defaults to None.
        title (str, optional): The title of the plot. Defaults to None.
        x_label (str, optional): The label for the x-axis. Defaults to None.
        y_label (str, optional): The label for the y-axis. Defaults to None.
        color (str, optional): The color of the area. Defaults to "skyblue".
    """

    # Example 1: Tips Dataset
    if data == "tips":
        df = sns.load_dataset("tips").groupby("day", observed=False).agg({"total_bill": "sum"}).reset_index()
        x = "day" if x is None else x
        y = "total_bill" if y is None else y
        title = "Total Bill Area Chart - Tips" if title is None else title
        x_label = "Day" if x_label is None else x_label
        y_label = "Total Bill" if y_label is None else y_label
        line_color = "blue"

        plt.figure(figsize=(8, 6))
        plt.fill_between(df[x], df[y], color=color, alpha=0.5)
        sns.lineplot(x=x, y=y, data=df, marker="o", color=line_color)
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.show()
        print(f"Area chart of {x} vs {y} from the Tips dataset.")

    # Example 2: Planets Dataset
    elif data == "planets":
        df = sns.load_dataset("planets").groupby("year").size().reset_index(name='discoveries')
        x = "year" if x is None else x
        y = "discoveries" if y is None else y
        title = "Planet Discovery Count Over Time - Area Chart" if title is None else title
        x_label = "Year" if x_label is None else x_label
        y_label = "Number of Discoveries" if y_label is None else y_label
        color = "lightgreen"
        line_color = "green"

        plt.figure(figsize=(8, 6))
        plt.fill_between(df[x], df[y], color=color, alpha=0.5)
        sns.lineplot(x=x, y=y, data=df, marker="o", color=line_color)
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.show()
        print(f"Area chart of {x} vs {y} from the Planets dataset.")

    elif isinstance(data, pd.DataFrame):
        df = data
        if x is None or y is None:
            raise ValueError("x and y parameters must be specified for a custom DataFrame.")
        title = "Area Chart" if title is None else title
        x_label = x if x_label is None else x_label
        y_label = y if y_label is None else y_label
        line_color = "blue"

        plt.figure(figsize=(8, 6))
        plt.fill_between(df[x], df[y], color=color, alpha=0.5)
        sns.lineplot(x=x, y=y, data=df, marker="o", color=line_color)
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.show()
        print(f"Area chart of {x} vs {y} from the provided DataFrame.")
    else:
        raise ValueError("Invalid dataset name. Choose 'tips', 'planets', or provide a pandas DataFrame.")

def pie_chart(data="tips", labels=None, values=None, title=None):
    """
    Generates a pie chart for a given dataset.

    Args:
        data (str or pd.DataFrame, optional): The dataset to use. Defaults to "tips".
            Can be "tips", "titanic", or a pandas DataFrame.
        labels (list, optional): The labels for the pie chart. Defaults to None.
        values (list, optional): The values for the pie chart. Defaults to None.
        title (str, optional): The title of the plot. Defaults to None.
    """

    # Example 1: Tips Dataset
    if data == "tips":
        df = sns.load_dataset("tips").groupby("day", observed=False).agg({"total_bill": "sum"}).reset_index()
        labels = df["day"] if labels is None else labels
        values = df["total_bill"] if values is None else values
        title = "Total Bill Distribution by Day - Tips" if title is None else title
        colors = sns.color_palette("Set2")

        plt.figure(figsize=(8, 6))
        plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
        plt.title(title)
        plt.show()
        print(f"Pie chart for the Tips dataset.")

    # Example 2: Titanic Dataset
    elif data == "titanic":
        df = sns.load_dataset("titanic").groupby("class").agg({"survived": "sum"}).reset_index()
        labels = df["class"] if labels is None else labels
        values = df["survived"] if values is None else values
        title = "Survival Rate by Class - Titanic" if title is None else title
        colors = sns.color_palette("Set3")

        plt.figure(figsize=(8, 6))
        plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
        plt.title(title)
        plt.show()
        print(f"Pie chart for the Titanic dataset.")

    elif isinstance(data, pd.DataFrame):
        df = data
        if labels is None or values is None:
            raise ValueError("labels and values parameters must be specified for a custom DataFrame.")
        title = "Pie Chart" if title is None else title
        colors = sns.color_palette("viridis")

        plt.figure(figsize=(8, 6))
        plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
        plt.title(title)
        plt.show()
        print(f"Pie chart for the provided DataFrame.")

    else:
        raise ValueError("Invalid dataset name. Choose 'tips', 'titanic', or provide a pandas DataFrame.")

def violin_plot(data="tips", x=None, y=None, hue=None, title=None, palette="muted"):
    """
    Generates a violin plot for a given dataset.

    Args:
        data (str or pd.DataFrame, optional): The dataset to use. Defaults to "tips".
            Can be "tips", "penguins", or a pandas DataFrame.
        x (str, optional): The column to use for the x-axis. Defaults to None.
        y (str, optional): The column to use for the y-axis. Defaults to None.
        hue (str, optional): The column to use for the hue. Defaults to None.
        title (str, optional): The title of the plot. Defaults to None.
        palette (str, optional): The color palette to use. Defaults to "muted".
    """

    # Example 1: Tips Dataset
    if data == "tips":
        df = sns.load_dataset("tips")
        x = "day" if x is None else x
        y = "total_bill" if y is None else y
        hue = "sex" if hue is None else hue
        title = "Total Bill Distribution by Day - Tips" if title is None else title

        plt.figure(figsize=(8, 6))
        sns.violinplot(x=x, y=y, data=df, palette=palette, hue=hue, split=True)
        plt.title(title)
        plt.show()
        print(f"Violin plot for the Tips dataset.")

    # Example 2: Penguins Dataset
    elif data == "penguins":
        df = sns.load_dataset("penguins")
        x = "species" if x is None else x
        y = "flipper_length_mm" if y is None else y
        hue = "sex" if hue is None else hue
        title = "Flipper Length Distribution by Species - Penguins" if title is None else title
        palette = "coolwarm"

        plt.figure(figsize=(8, 6))
        sns.violinplot(x=x, y=y, data=df, palette=palette, hue=hue, split=True)
        plt.title(title)
        plt.show()
        print(f"Violin plot for the Penguins dataset.")

    elif isinstance(data, pd.DataFrame):
        df = data
        if x is None or y is None:
            raise ValueError("x and y parameters must be specified for a custom DataFrame.")
        title = "Violin Plot" if title is None else title

        plt.figure(figsize=(8, 6))
        sns.violinplot(x=x, y=y, data=df, palette=palette, hue=hue, split=True)
        plt.title(title)
        plt.show()
        print(f"Violin plot for the provided DataFrame.")

    else:
        raise ValueError("Invalid dataset name. Choose 'tips', 'penguins', or provide a pandas DataFrame.")

def parallel_coordinates_plot(data="iris", class_column="species", colors=None):
    """
    Generates a parallel coordinates plot for a given dataset.

    Args:
        data (str or pd.DataFrame, optional): The dataset to use. Defaults to "iris".
            Can be "iris" or a pandas DataFrame.
        class_column (str, optional): The column to use for the class labels. Defaults to "species".
        colors (list, optional): The colors to use for each class. Defaults to None.
    """

    # Example 1: Iris Dataset
    if data == "iris":
        df = sns.load_dataset("iris")
        colors = ["blue", "green", "red"] if colors is None else colors
        title = "Parallel Coordinates Plot - Iris Dataset"
        plt.figure(figsize=(12, 6))
        parallel_coordinates(df, class_column, color=colors)
        plt.title(title)
        plt.show()
        print(f"Parallel Coordinates plot for the Iris dataset.")

    elif isinstance(data, pd.DataFrame):
        df = data
        title = "Parallel Coordinates Plot"
        plt.figure(figsize=(12, 6))
        parallel_coordinates(df, class_column, color=colors)
        plt.title(title)
        plt.show()
        print(f"Parallel Coordinates plot for the provided DataFrame.")
    else:
        raise ValueError("Invalid dataset name. Choose 'iris' or provide a pandas DataFrame.")
    if data == "iris":
      df = sns.load_dataset("iris")
      colors = ["blue", "green", "red"] if colors is None else colors
      title = "Parallel Coordinates Plot - Iris Dataset"
      plt.figure(figsize=(12, 6))
      parallel_coordinates(df, class_column, color=colors)
      plt.title(title)
      plt.show()
      print(f"Parallel Coordinates plot for the Iris dataset.")

    elif isinstance(data, pd.DataFrame):
      df = data
      title = "Parallel Coordinates Plot"
      plt.figure(figsize=(12, 6))
      parallel_coordinates(df, class_column, color=colors)
      plt.title(title)
      plt.show()
      print(f"Parallel Coordinates plot for the provided DataFrame.")
    else:
      raise ValueError("Invalid dataset name. Choose 'iris' or provide a pandas DataFrame.")

def bubble_chart(data="mpg", x="horsepower", y="weight", size="acceleration", color="mpg",
                 x_label="Horsepower", y_label="Weight", color_label="Miles per Gallon (mpg)",
                 title="Horsepower vs. Weight with Acceleration as Bubble Size (mpg Dataset)"):
    """
    Generates a bubble chart for a given dataset.

    Args:
        data (str or pd.DataFrame, optional): The dataset to use. Defaults to "mpg".
            Can be "mpg" or a pandas DataFrame.
        x (str, optional): The column to use for the x-axis. Defaults to "horsepower".
        y (str, optional): The column to use for the y-axis. Defaults to "weight".
        size (str, optional): The column to use for the bubble size. Defaults to "acceleration".
        color (str, optional): The column to use for the bubble color. Defaults to "mpg".
        x_label (str, optional): The label for the x-axis. Defaults to "Horsepower".
        y_label (str, optional): The label for the y-axis. Defaults to "Weight".
        color_label (str, optional): The label for the color bar. Defaults to "Miles per Gallon (mpg)".
        title (str, optional): The title of the plot. Defaults to
        "Horsepower vs. Weight with Acceleration as Bubble Size (mpg Dataset)".
    """
    # Example 1: MPG Dataset
    if data == "mpg":
        df = sns.load_dataset("mpg").dropna()
        title = "Horsepower vs. Weight with Acceleration as Bubble Size (MPG Dataset)" if title is None else title
        x_label = "Horsepower" if x_label is None else x_label
        y_label = "Weight" if y_label is None else y_label
        color_label = "Miles per Gallon (mpg)" if color_label is None else color_label

        plt.figure(figsize=(10, 6))
        plt.scatter(x=df[x], y=df[y], s=df[size] * 10, c=df[color], cmap='viridis', alpha=0.6, edgecolors="w", linewidth=1)

        plt.colorbar(plt.scatter(x=df[x], y=df[y], s=df[size] * 10, c=df[color], cmap='viridis', alpha=0.6, edgecolors="w", linewidth=1), label=color_label)

        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.show()
        print(f"Bubble chart of {x} vs {y} with {size} as bubble size and {color} as bubble color from the MPG dataset.")

    elif isinstance(data, pd.DataFrame):
        df = data.dropna()
        title = "Bubble Chart" if title is None else title
        x_label = x if x_label is None else x_label
        y_label = y if y_label is None else y_label
        color_label = color if color_label is None else color_label

        plt.figure(figsize=(10, 6))
        plt.scatter(x=df[x], y=df[y], s=df[size] * 10, c=df[color], cmap='viridis', alpha=0.6, edgecolors="w", linewidth=1)

        plt.colorbar(plt.scatter(x=df[x], y=df[y], s=df[size] * 10, c=df[color], cmap='viridis', alpha=0.6, edgecolors="w", linewidth=1), label=color_label)

        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.show()
        print(f"Bubble chart of {x} vs {y} with {size} as bubble size and {color} as bubble color from the provided DataFrame.")

    else:
        raise ValueError("Invalid dataset name. Choose 'mpg' or provide a pandas DataFrame.")
    
def scatter_matrix(data="iris", hue="species"):
    """
    Generates a scatter matrix plot for a given dataset.

    Args:
        data (str or pd.DataFrame, optional): The dataset to use. Defaults to "iris".
            Can be "iris" or a pandas DataFrame.
        hue (str, optional): The column to use for the color hue. Defaults to "species".
    """
    # Example 1: Iris Dataset
    if data == "iris":
        df = sns.load_dataset("iris")
        hue = "species" if hue is None else hue
        title = "Scatter Matrix Plot - Iris Dataset"

        plt.figure(figsize=(10, 8))
        sns.pairplot(df, hue=hue, palette="viridis")
        plt.suptitle(title, y=1.02)
        plt.show()
        print(f"Scatter matrix plot for the Iris dataset.")

    elif isinstance(data, pd.DataFrame):
        df = data
        title = "Scatter Matrix Plot"
        plt.figure(figsize=(10, 8))
        sns.pairplot(df, hue=hue, palette="viridis")
        plt.suptitle(title, y=1.02)
        plt.show()
        print(f"Scatter matrix plot for the provided DataFrame.")

    else:
        raise ValueError("Invalid dataset name. Choose 'iris' or provide a pandas DataFrame.")
    
def density_plot(data="iris", column=None, title=None, x_label=None, y_label=None, color='blue'):
    """
    Generates a density plot for a given dataset and column.

    Args:
        data (str or pd.DataFrame, optional): The dataset to use. Defaults to "iris".
            Can be "iris", "mpg", or a pandas DataFrame.
        column (str, optional): The column to plot the density for. Defaults to None.
        title (str, optional): The title of the plot. Defaults to None.
        x_label (str, optional): The label for the x-axis. Defaults to None.
        y_label (str, optional): The label for the y-axis. Defaults to None.
        color (str, optional): The color of the density plot. Defaults to 'blue'.
    """

    # Example 1: Iris Dataset
    if data == "iris":
        df = sns.load_dataset("iris")
        column = 'sepal_length' if column is None else column
        title = "Density Plot - Iris Dataset" if title is None else title
        x_label = column if x_label is None else x_label
        y_label = "Density" if y_label is None else y_label

        plt.figure(figsize=(8, 6))
        sns.kdeplot(df[column], shade=True, color=color)
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.show()
        print(f"Density plot of {column} from the Iris dataset.")

    # Example 2: MPG Dataset
    elif data == "mpg":
        df = sns.load_dataset("mpg")
        column = 'mpg' if column is None else column
        title = "Density Plot - MPG Dataset" if title is None else title
        x_label = column if x_label is None else x_label
        y_label = "Density" if y_label is None else y_label

        plt.figure(figsize=(8, 6))
        sns.kdeplot(df[column], shade=True, color=color)
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.show()
        print(f"Density plot of {column} from the MPG dataset.")

    elif isinstance(data, pd.DataFrame):
        df = data
        if column is None:
            raise ValueError("Column parameter must be specified for a custom DataFrame.")
        title = f"Density Plot of {column}" if title is None else title
        x_label = column if x_label is None else x_label
        y_label = "Density" if y_label is None else y_label

        plt.figure(figsize=(8, 6))
        sns.kdeplot(df[column], shade=True, color=color)
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.show()
        print(f"Density plot of {column} from the provided DataFrame.")

    else:
        raise ValueError("Invalid dataset name. Choose 'iris', 'mpg', or provide a pandas DataFrame.")
    
def hexbin_plot(data="iris", x=None, y=None, gridsize=30, cmap="Blues", title=None, x_label=None, y_label=None):
        """
        Generates a hexbin plot for a given dataset.

        Args:
            data (str or pd.DataFrame, optional): The dataset to use. Defaults to "iris".
                Can be "iris", "mpg", or a pandas DataFrame.
            x (str, optional): The column to use for the x-axis. Defaults to None.
            y (str, optional): The column to use for the y-axis. Defaults to None.
            gridsize (int, optional): The number of hexagons in the x-direction. Defaults to 30.
            cmap (str, optional): The color map to use. Defaults to "Blues".
            title (str, optional): The title of the plot. Defaults to None.
            x_label (str, optional): The label for the x-axis. Defaults to None.
            y_label (str, optional): The label for the y-axis. Defaults to None.
        """

        # Example 1: Iris Dataset
        if data == "iris":
            df = sns.load_dataset("iris")
            x = "sepal_length" if x is None else x
            y = "sepal_width" if y is None else y
            title = "Hexbin Plot - Iris Dataset" if title is None else title
            x_label = "Sepal Length" if x_label is None else x_label
            y_label = "Sepal Width" if y_label is None else y_label

            plt.figure(figsize=(8, 6))
            plt.hexbin(df[x], df[y], gridsize=gridsize, cmap=cmap)
            plt.colorbar(label='Count')
            plt.title(title)
            plt.xlabel(x_label)
            plt.ylabel(y_label)
            plt.show()
            print(f"Hexbin plot of {x} vs {y} from the Iris dataset.")

        # Example 2: MPG Dataset
        elif data == "mpg":
            df = sns.load_dataset("mpg").dropna()
            x = "horsepower" if x is None else x
            y = "mpg" if y is None else y
            title = "Hexbin Plot - MPG Dataset" if title is None else title
            x_label = "Horsepower" if x_label is None else x_label
            y_label = "Miles per Gallon (mpg)" if y_label is None else y_label

            plt.figure(figsize=(8, 6))
            plt.hexbin(df[x], df[y], gridsize=gridsize, cmap=cmap)
            plt.colorbar(label='Count')
            plt.title(title)
            plt.xlabel(x_label)
            plt.ylabel(y_label)
            plt.show()
            print(f"Hexbin plot of {x} vs {y} from the MPG dataset.")

        elif isinstance(data, pd.DataFrame):
            df = data
            if x is None or y is None:
                raise ValueError("x and y parameters must be specified for a custom DataFrame.")
            title = "Hexbin Plot" if title is None else title
            x_label = x if x_label is None else x_label
            y_label = y if y_label is None else y_label

            plt.figure(figsize=(8, 6))
            plt.hexbin(df[x], df[y], gridsize=gridsize, cmap=cmap)
            plt.colorbar(label='Count')
            plt.title(title)
            plt.xlabel(x_label)
            plt.ylabel(y_label)
            plt.show()
            print(f"Hexbin plot of {x} vs {y} from the provided DataFrame.")

        else:

            raise ValueError("Invalid dataset name. Choose 'iris', 'mpg', or provide a pandas DataFrame.")
        
def pairplot(data="iris", hue="species"):
    """
    Generates a pairplot for a given dataset.

    Args:
        data (str or pd.DataFrame, optional): The dataset to use. Defaults to "iris".
            Can be "iris" or a pandas DataFrame.
        hue (str, optional): The column to use for the color hue. Defaults to "species".
    """
    # Example 1: Iris Dataset
    if data == "iris":
        df = sns.load_dataset("iris")
        hue = "species" if hue is None else hue
        title = "Pairplot - Iris Dataset"

        plt.figure(figsize=(10, 8))
        sns.pairplot(df, hue=hue, palette="viridis")
        plt.suptitle(title, y=1.02)
        plt.show()
        print(f"Pairplot for the Iris dataset.")

    elif isinstance(data, pd.DataFrame):
        df = data
        title = "Pairplot"
        plt.figure(figsize=(10, 8))
        sns.pairplot(df, hue=hue, palette="viridis")
        plt.suptitle(title, y=1.02)
        plt.show()
        print(f"Pairplot for the provided DataFrame.")

    else:
        raise ValueError("Invalid dataset name. Choose 'iris' or provide a pandas DataFrame.")
    
def donut_chart(data="tips", labels=None, values=None, title=None):
    """
    Generates a donut chart for a given dataset.

    Args:
        data (str or pd.DataFrame, optional): The dataset to use. Defaults to "tips".
            Can be "tips", "titanic", or a pandas DataFrame.
        labels (list, optional): The labels for the donut chart. Defaults to None.
        values (list, optional): The values for the donut chart. Defaults to None.
        title (str, optional): The title of the plot. Defaults to None.
    """

    # Example 1: Tips Dataset
    if data == "tips":
        df = sns.load_dataset("tips").groupby("day", observed=False).agg({"total_bill": "sum"}).reset_index()
        labels = df["day"] if labels is None else labels
        values = df["total_bill"] if values is None else values
        title = "Total Bill Distribution by Day - Tips" if title is None else title
        colors = sns.color_palette("Set2")

        plt.figure(figsize=(8, 6))
        plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors, wedgeprops=dict(width=0.3))
        plt.title(title)
        plt.show()
        print(f"Donut chart for the Tips dataset.")

    # Example 2: Titanic Dataset
    elif data == "titanic":
        df = sns.load_dataset("titanic").groupby("class").agg({"survived": "sum"}).reset_index()
        labels = df["class"] if labels is None else labels
        values = df["survived"] if values is None else values
        title = "Survival Rate by Class - Titanic" if title is None else title
        colors = sns.color_palette("Set3")

        plt.figure(figsize=(8, 6))
        plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors, wedgeprops=dict(width=0.3))
        plt.title(title)
        plt.show()
        print(f"Donut chart for the Titanic dataset.")

    elif isinstance(data, pd.DataFrame):
        df = data
        if labels is None or values is None:
            raise ValueError("labels and values parameters must be specified for a custom DataFrame.")
        title = "Donut Chart" if title is None else title
        colors = sns.color_palette("viridis")

        plt.figure(figsize=(8, 6))
        plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors, wedgeprops=dict(width=0.3))
        plt.title(title)
        plt.show()
        print(f"Donut chart for the provided DataFrame.")

    else:
        raise ValueError("Invalid dataset name. Choose 'tips', 'titanic', or provide a pandas DataFrame.")

def lollipop_chart(data="tips", x=None, y=None, title=None, x_label=None, y_label=None):
    """
    Generates a lollipop chart for a given dataset.

    Args:
        data (str or pd.DataFrame, optional): The dataset to use. Defaults to "tips".
            Can be "tips", "titanic", or a pandas DataFrame.
        x (str, optional): The column to use for the x-axis. Defaults to None.
        y (str, optional): The column to use for the y-axis. Defaults to None.
        title (str, optional): The title of the plot. Defaults to None.
        x_label (str, optional): The label for the x-axis. Defaults to None.
        y_label (str, optional): The label for the y-axis. Defaults to None.
    """

    # Example 1: Tips Dataset
    if data == "tips":
        df = sns.load_dataset("tips")
        x = "day" if x is None else x
        y = "total_bill" if y is None else y
        title = "Total Bill by Day - Tips" if title is None else title
        x_label = "Day" if x_label is None else x_label
        y_label = "Total Bill" if y_label is None else y_label

        plt.figure(figsize=(8, 6))
        plt.stem(df[x], df[y], basefmt=" ")
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.show()
        print(f"Lollipop chart of {x} vs {y} from the Tips dataset.")

    elif isinstance(data, pd.DataFrame):
        df = data
        if x is None or y is None:
            raise ValueError("x and y parameters must be specified for a custom DataFrame.")
        title = "Lollipop Chart" if title is None else title
        x_label = x if x_label is None else x_label
        y_label = y if y_label is None else y_label

        plt.figure(figsize=(8, 6))
        plt.stem(df[x], df[y], basefmt=" ", use_line_collection=True)
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.show()
        print(f"Lollipop chart of {x} vs {y} from the provided DataFrame.")

    else:
        raise ValueError("Invalid dataset name. Choose 'tips', 'titanic', or provide a pandas DataFrame.")

def radar_chart(data="iris", categories=None, title=None):

    """
    Generates a radar chart for a given dataset.

    Args:
        data (str or pd.DataFrame, optional): The dataset to use. Defaults to "iris".
            Can be "iris" or a pandas DataFrame.
        categories (list, optional): The categories to plot. Defaults to None.
        title (str, optional): The title of the plot. Defaults to None.
    """

    # Example 1: Iris Dataset
    if data == "iris":
        df = sns.load_dataset("iris")
        categories = df.columns[:-1] if categories is None else categories
        title = "Radar Chart - Iris Dataset" if title is None else title

        # Compute the mean of each category for each species
        df_mean = df.groupby("species").mean().reset_index()

        # Number of variables
        num_vars = len(categories)

        # Compute angle of each axis
        angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

        # The plot is a circle, so we need to "complete the loop"
        angles += angles[:1]

        fig, ax = plt.subplots(figsize=(8, 6), subplot_kw=dict(polar=True))

        for i, row in df_mean.iterrows():
            values = row[categories].tolist()
            values += values[:1]
            ax.plot(angles, values, label=row["species"])
            ax.fill(angles, values, alpha=0.25)

        ax.set_title(title)
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(categories)
        ax.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1))
        plt.show()
        print(f"Radar chart for the Iris dataset.")

    elif isinstance(data, pd.DataFrame):
        df = data
        if categories is None:
            raise ValueError("Categories parameter must be specified for a custom DataFrame.")
        title = "Radar Chart" if title is None else title

        # Compute the mean of each category
        df_mean = df.mean().reset_index()

        # Number of variables
        num_vars = len(categories)

        # Compute angle of each axis
        angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

        # The plot is a circle, so we need to "complete the loop"
        angles += angles[:1]

        fig, ax = plt.subplots(figsize=(8, 6), subplot_kw=dict(polar=True))

        values = df_mean[categories].tolist()
        values += values[:1]
        ax.plot(angles, values, label="Mean")
        ax.fill(angles, values, alpha=0.25)

        ax.set_title(title)
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(categories)
        ax.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1))
        plt.show()
        print(f"Radar chart for the provided DataFrame.")

    else:
        raise ValueError("Invalid dataset name. Choose 'iris' or provide a pandas DataFrame.")
    
def boxen_plot(data="tips", x=None, y=None, title=None, x_label=None, y_label=None, color="skyblue"):
    """
    Generates a boxen plot for a given dataset.

    Args:
        data (str or pd.DataFrame, optional): The dataset to use. Defaults to "tips".
            Can be "tips", "penguins", or a pandas DataFrame.
        x (str, optional): The column to use for the x-axis. Defaults to None.
        y (str, optional): The column to use for the y-axis. Defaults to None.
        title (str, optional): The title of the plot. Defaults to None.
        x_label (str, optional): The label for the x-axis. Defaults to None.
        y_label (str, optional): The label for the y-axis. Defaults to None.
        color (str, optional): The color of the boxen plot. Defaults to "skyblue".
    """

    # Example 1: Tips Dataset
    if data == "tips":
        df = sns.load_dataset("tips")
        x = "day" if x is None else x
        y = "total_bill" if y is None else y
        title = "Total Bill Distribution by Day - Tips" if title is None else title
        x_label = "Day" if x_label is None else x_label
        y_label = "Total Bill" if y_label is None else y_label

        plt.figure(figsize=(8, 6))
        sns.boxenplot(x=x, y=y, data=df, color=color)
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.show()
        print(f"Boxen plot of {x} vs {y} from the Tips dataset.")

    # Example 2: Penguins Dataset
    elif data == "penguins":
        df = sns.load_dataset("penguins")
        x = "species" if x is None else x
        y = "flipper_length_mm" if y is None else y
        title = "Flipper Length Distribution by Species - Penguins" if title is None else title
        color = "lightgreen"
        x_label = "Species" if x_label is None else x_label
        y_label = "Flipper Length (mm)" if y_label is None else y_label

        plt.figure(figsize=(8, 6))
        sns.boxenplot(x=x, y=y, data=df, color=color)
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.show()
        print(f"Boxen plot of {x} vs {y} from the Penguins dataset.")

    elif isinstance(data, pd.DataFrame):
        df = data
        if x is None or y is None:
            raise ValueError("x and y parameters must be specified for a custom DataFrame.")
        title = "Boxen Plot" if title is None else title
        x_label = x if x_label is None else x_label
        y_label = y if y_label is None else y_label

        plt.figure(figsize=(8, 6))
        sns.boxenplot(x=x, y=y, data=df, color=color)
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.show()
        print(f"Boxen plot of {x} vs {y} from the provided DataFrame.")

    else:
        raise ValueError("Invalid dataset name. Choose 'tips', 'penguins', or provide a pandas DataFrame.")
    
