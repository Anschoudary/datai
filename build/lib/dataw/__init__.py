# dataw/__init__.py

# Import essential functions from each module to make them accessible from the package
from .visualization import plot_bar_chart, plot_line_chart, plot_scatter_plot, plot_heatmap
from .data_cleaning import clean_missing_data, remove_outliers, normalize_data
from .auto_plot import auto_plot
from .datasets import load_dataset

# Define the __all__ variable to specify what is accessible when using 'from dataw import *'
__all__ = [
    "plot_bar_chart",
    "plot_line_chart",
    "plot_scatter_plot",
    "plot_heatmap",
    "clean_missing_data",
    "remove_outliers",
    "normalize_data",
    "auto_plot",
    "load_dataset"
]

# Version of the library
__version__ = "1.0"

# Brief description of the library (optional but helpful)
__description__ = "A Python library for easy data visualization, data cleaning, and automatic chart generation."

