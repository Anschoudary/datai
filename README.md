
#  Datai

Welcome to **Datai**. This library provides tools to visualize data easily, clean datasets, and automatically generate appropriate plots for your data. Whether you're a beginner or an experienced data scientist, this library aims to simplify the data exploration and visualization process.

## Features

- **Data Visualization**: Easily create bar charts, scatter plots, histograms, and more with simple functions.
- **Data Cleaning**: Clean and preprocess your data with built-in utilities for handling missing values, normalizing data, and more.
- **Auto Plotting**: Automatically generate the most suitable plot based on your dataset's characteristics.
- **Example Datasets**: Load popular datasets like Iris, Titanic, and more for quick experimentation and testing.

## Installation

To install the library, use pip:

```bash
pip install datai
```

## Basic Usage


### 1. Visualize Data

Create simple visualizations with just a few lines of code:

```python
# Example: Create a bar chart

from datai.visualization import Examples
Examples.barchart()
```

### 2. Clean Data

Easily clean and preprocess your data:

```python
# Data cleaning
import seaborn as sns
from datai.data_cleaning import DataCleaning

# Load the Iris dataset
iris_data = sns.load_dataset('iris')

# Clean the data
cleaner = DataCleaning(iris_data)
cleaned_data = cleaner.get_cleaned_data()
```

### 3. Auto Plot

Automatically generate a plot based on your dataset:

```python
# Auto plot a dataset
import seaborn as sns
from datai.auto_plot import AutoPlot

tips = sns.load_dataset('tips')

AutoPlot.auto_plot(tips)
```

You can also plot a chart of your choice
```python
x_data = tips['total_bill']
y_data = tips['tip']
AutoPlot.plot_scatter_plot(x_data, y_data)
````

### 4. Gift
Here's an interesting feature in the library. You can animate your name.
```python
from datai.gift import Gift
Gift.myName("Datai")
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you have any suggestions or improvements.

## Contact

For any questions or feedback, please reach out at [m.ans.cs@outlook.com](mailto:m.ans.cs@outlook.com).


Thank you for using **Datai**! We hope it makes your data analysis journey easier and more enjoyable.
```
