import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns


def auto_plot(dataset):
    """
    Suggests and displays plot types based on the characteristics of the dataset, aiming for a versatile analysis,
    while limiting the number of plot suggestions for large datasets.

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
    numeric_cols = data_types[data_types != 'object'].index.tolist()  # Ensure list
    categorical_cols = data_types[data_types == 'object'].index.tolist()  # Ensure list

    # Print dataset summary
    print(f"Number of rows: {num_rows}")
    print(f"Number of columns: {num_cols}")
    print(f"Numeric columns: {numeric_cols}")
    print(f"Categorical columns: {categorical_cols}")

    # Helper Function to display plots
    def display_plot(plot_func, **kwargs):
        plt.figure(figsize=(10, 6))
        try:
            plot_func(**kwargs)
        except Exception as e:
            print(f"Error plotting: {e}")
            return  # Skip if plot fails
        plt.show()

    # Maximum number of plots to suggest for each type
    MAX_PLOTS_PER_TYPE = 2

    # 1. If ONLY Numeric Columns Exist
    if numeric_cols and not categorical_cols:
        print("Suggested plots for numeric-only data:")
        # a. Histograms for each numeric column
        num_hist = min(MAX_PLOTS_PER_TYPE, len(numeric_cols))
        for col in numeric_cols[:num_hist]:
            print(f"- Histogram for {col}")
            display_plot(sns.histplot, x=col, data=dataset, kde=True)

        # b. Scatter plot matrix (pairplot) if feasible (few columns)
        if len(numeric_cols) <= 5:  # Limit to avoid overwhelming plots
            print("- Scatter plot matrix (pairplot)")
            sns.pairplot(data=dataset[numeric_cols])
            plt.show()

        # c. Correlation Heatmap
        print("- Correlation Heatmap")
        display_plot(sns.heatmap, data=dataset[numeric_cols].corr(), annot=True, cmap='coolwarm', linewidths=0.5)

        # d. Box plots to detect outliers
        num_box = min(MAX_PLOTS_PER_TYPE, len(numeric_cols))
        for col in numeric_cols[:num_box]:
            print(f"- Box plot for {col}")
            display_plot(sns.boxplot, y=col, data=dataset)

        # e. Line plots if the index is meaningful (e.g., time series)
        if dataset.index.is_monotonic_increasing or dataset.index.is_monotonic_decreasing:
            print("- Line plots for trends over index")
            num_line = min(MAX_PLOTS_PER_TYPE, len(numeric_cols))
            for col in numeric_cols[:num_line]:
                display_plot(plt.plot, x=dataset.index, y=dataset[col], marker='o', linestyle='-')

    # 2. If ONLY Categorical Columns Exist
    elif categorical_cols and not numeric_cols:
        print("Suggested plots for categorical-only data:")
        # a. Count plots for each category
        num_count = min(MAX_PLOTS_PER_TYPE, len(categorical_cols))
        for col in categorical_cols[:num_count]:
            print(f"- Count plot for {col}")
            display_plot(sns.countplot, x=col, data=dataset)

        # b. Stacked Bar Chart (if multiple categorical cols, show relationship)
        if len(categorical_cols) >= 2:
            print("- Stacked Bar Chart")
            cross_tab = pd.crosstab(dataset[categorical_cols[0]], dataset[categorical_cols[1]])
            cross_tab.plot(kind='bar', stacked=True, figsize=(10, 6))
            plt.title('Stacked Bar Chart')
            plt.show()

        # c. Pie Charts
        num_pie = min(MAX_PLOTS_PER_TYPE, len(categorical_cols))
        for col in categorical_cols[:num_pie]:
            print(f"- Pie chart for {col}")
            category_counts = dataset[col].value_counts()
            plt.figure(figsize=(6, 6))
            plt.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%', startangle=140)
            plt.title(f'Distribution of {col}')
            plt.show()

    # 3. MIXED Numeric and Categorical Data
    elif numeric_cols and categorical_cols:
        print("Suggested plots for mixed data:")

        # a. Box plots of numeric features grouped by categorical
        num_box = min(MAX_PLOTS_PER_TYPE, len(categorical_cols))
        for cat_col in categorical_cols[:num_box]:
            num_col_box = min(MAX_PLOTS_PER_TYPE, len(numeric_cols)) #Limiting num cols inside loop
            for num_col in numeric_cols[:num_col_box]:
                print(f"- Box plot of {num_col} by {cat_col}")
                display_plot(sns.boxplot, x=cat_col, y=num_col, data=dataset)

        # b. Violin plots (similar to box plots, but show distribution)
        num_violin = min(MAX_PLOTS_PER_TYPE, len(categorical_cols))
        for cat_col in categorical_cols[:num_violin]:
            num_col_violin = min(MAX_PLOTS_PER_TYPE, len(numeric_cols))#Limiting num cols inside loop
            for num_col in numeric_cols[:num_col_violin]:
                print(f"- Violin plot of {num_col} by {cat_col}")
                display_plot(sns.violinplot, x=cat_col, y=num_col, data=dataset)

        # c. Bar plots of aggregated numeric data by category
        num_bar = min(MAX_PLOTS_PER_TYPE, len(categorical_cols))
        for cat_col in categorical_cols[:num_bar]:
            num_col_bar = min(MAX_PLOTS_PER_TYPE, len(numeric_cols))#Limiting num cols inside loop
            for num_col in numeric_cols[:num_col_bar]:
                print(f"- Bar plot of mean {num_col} by {cat_col}")
                grouped_data = dataset.groupby(cat_col)[num_col].mean().reset_index()
                display_plot(sns.barplot, x=cat_col, y=num_col, data=grouped_data)

        # d. Scatter plots with hue
        if len(numeric_cols) >= 2 and len(categorical_cols) >= 1:
            print(f"- Scatter plot of {numeric_cols[0]} vs {numeric_cols[1]}, colored by {categorical_cols[0]}")
            display_plot(sns.scatterplot, x=numeric_cols[0], y=numeric_cols[1], data=dataset, hue=categorical_cols[0])

    # 4. No Clear Features
    else:
        print("The dataset does not have clear numeric or categorical features for visualization.")


def bar_chart(data, x_col, y_col, color='blue', title=None, x_label=None, y_label=None):
    """Plot a bar chart."""
    plt.figure(figsize=(10, 6))
    plt.bar(data[x_col], data[y_col], color=color)

    # Set labels and title with defaults
    plt.xlabel(x_col if x_label is None else x_label)
    plt.ylabel(y_col if y_label is None else y_label)
    plt.title(f'{y_col} by {x_col}' if title is None else title)
    plt.show()
    print(f"Bar Chart: Displaying {y_col} by {x_col}.")


def line_chart(data, x_col, y_col, color='green', marker='o', linestyle='-', title=None, x_label=None, y_label=None):
    """Plot a line chart."""
    plt.figure(figsize=(10, 6))
    plt.plot(data[x_col], data[y_col], color=color, marker=marker, linestyle=linestyle)

    # Set labels and title with defaults
    plt.xlabel(x_col if x_label is None else x_label)
    plt.ylabel(y_col if y_label is None else y_label)
    plt.title(f'{y_col} over {x_col}' if title is None else title)

    plt.grid(True)
    plt.show()
    print(f"Line Chart: Displaying {y_col} over {x_col}.")


def scatter_plot(data, x_col, y_col, color='red', title=None, x_label=None, y_label=None):
    """Plot a scatter plot for the specified x and y columns."""
    plt.figure(figsize=(10, 6))
    plt.scatter(data[x_col], data[y_col], color=color)

    # Set labels and title with defaults
    plt.xlabel(x_col if x_label is None else x_label)
    plt.ylabel(y_col if y_label is None else y_label)
    plt.title(f'{y_col} vs {x_col}' if title is None else title)

    plt.grid(True)
    plt.show()
    print(f"Scatter Plot: Displaying {y_col} vs {x_col}.")


def histogram(data, col, bins=15, color='purple', title=None, x_label=None, y_label=None):
    """Plot a histogram for a specific column."""
    plt.figure(figsize=(10, 6))
    plt.hist(data[col], bins=bins, color=color, edgecolor='black')

    # Set labels and title with defaults
    plt.xlabel(col if x_label is None else x_label)
    plt.ylabel('Frequency' if y_label is None else y_label)
    plt.title(f'Histogram of {col}' if title is None else title)

    plt.show()
    print(f"Histogram: Displaying distribution of {col}.")


def heatmap(data, cols=None, annot=True, cmap='coolwarm', linewidths=0.5, title="Correlation Heatmap"):
    """Plot a heatmap for the correlation matrix of specific columns or all."""
    if cols is None:
        cols = data.select_dtypes(include=np.number).columns  # Use only numeric cols if None given
    plt.figure(figsize=(12, 8))
    correlation_matrix = data[cols].corr()
    sns.heatmap(correlation_matrix, annot=annot, cmap=cmap, linewidths=linewidths)
    plt.title(title)
    plt.show()
    print("Heatmap: Displaying correlation matrix of the dataset.")


def violin_plot(data, x_col, y_col, title=None, x_label=None, y_label=None):
    """Plot a violin plot for the specified x and y columns."""
    plt.figure(figsize=(10, 6))
    sns.violinplot(x=x_col, y=y_col, data=data)

    # Set labels and title with defaults
    plt.xlabel(x_col if x_label is None else x_label)
    plt.ylabel(y_col if y_label is None else y_label)
    plt.title(f'Violin Plot of {y_col} by {x_col}' if title is None else title)

    plt.show()
    print(f"Violin Plot: Displaying {y_col} by {x_col}.")


def density_plot(data, col, color='blue', title=None, x_label=None, y_label=None):
    """Plot a density plot for a specific numeric column."""
    plt.figure(figsize=(10, 6))
    sns.kdeplot(data[col], fill=True, color=color)

    # Set labels and title with defaults
    plt.xlabel(col if x_label is None else x_label)
    plt.ylabel('Density' if y_label is None else y_label)
    plt.title(f'Density Plot of {col}' if title is None else title)

    plt.show()
    print(f"Density Plot: Displaying distribution of {col}.")


def pie_chart(data, col, title=None):
    """Plots a pie chart for a categorical column."""
    category_counts = data[col].value_counts()
    plt.figure(figsize=(8, 6))
    plt.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%', startangle=140)
    plt.title(title or f'Distribution of {col}')  # Use provided title or default
    plt.show()
    print(f"Pie Chart: Displaying distribution of {col}.")


def stacked_bar_chart(data, col1, col2, title=None, x_label=None, y_label=None):
    """Plots a stacked bar chart for two categorical columns."""
    cross_tab = pd.crosstab(data[col1], data[col2])
    cross_tab.plot(kind='bar', stacked=True, figsize=(10, 6))
    plt.title(title or f'Stacked Bar Chart of {col1} and {col2}')
    plt.xlabel(x_label or col1)
    plt.ylabel(y_label or 'Frequency')
    plt.show()
    print(f"Stacked Bar Chart: Displaying relationship between {col1} and {col2}.")

