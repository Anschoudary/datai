# Datai

Welcome to **Datai**. This library provides tools to visualize data easily, clean datasets, and automatically generate appropriate plots for your data. Whether you're a beginner or an experienced data scientist, this library aims to simplify the data exploration and visualization process.

## Features

- **Data Visualization**: Easily create bar charts, scatter plots, histograms, and more with simple functions.
- **Data Cleaning**: Clean and preprocess your data with built-in utilities for handling missing values, normalizing data, and more.
- **Auto Plotting**: Automatically generate the most suitable plot based on your dataset's characteristics.
- **Sound Visualization**: Visualize sound data with waveform, FFT, and spectrogram plots.
- **Example Datasets**: Load popular datasets like Iris, Titanic, and more for quick experimentation and testing.
- **Fun Animations**: Create animated text, shape swarms, and even Conway's Game of Life!

## Installation

To install the library, use pip:

```bash
pip install datai
```

## Basic Usage

### 1. Data Visualization

The `datai.visualization` module provides a variety of functions to easily create different types of plots. You can use example datasets or your own data.

```python
from datai.visualization import (
    bar_chart, scatter_plot, histogram, pie_chart, violin_plot, area_chart,
    box_plot, heatmap, line_chart, parallel_coordinates_plot, bubble_chart, radial_chart
)
import pandas as pd
import seaborn as sns

# Example 1: Bar chart with the Titanic dataset
bar_chart(data="titanic")

# Example 2: Scatter plot with the Iris dataset
scatter_plot(data="iris")

# Example 3: Histogram with the Tips dataset
histogram(data="tips", column="total_bill")

# Example 4: Pie chart with the Titanic dataset
pie_chart(data="titanic")

# Example 5: Using your own DataFrame
my_data = sns.load_dataset('iris')  # Replace with your actual data
scatter_plot(data=my_data, x="sepal_length", y="sepal_width", title="My Iris Plot")

# Example 6: Bubble Chart with the mpg dataset
bubble_chart(data="mpg")

# Example 7: Radial Chart with the tips dataset
radial_chart(data="tips")

# Example 8: Violin Plot with the penguins dataset
violin_plot(data="penguins")

# Example 9: Area Chart with the planet dataset
area_chart(data="planets")

# Example 10: Heatmap with the flights dataset
heatmap(data="flights")

# Example 11: Box Plot with the tips dataset
box_plot(data="tips")

# Example 12: Line Chart with the flights dataset
line_chart(data="flights")

# Example 13: Parallel coordinates plot with the iris dataset
parallel_coordinates_plot(data="iris")
```

### 2. Automatic Plotting with `auto_plot`

The `datai.auto_plot` module provides functions for automatically suggesting and generating plots, as well as individual functions for creating specific plot types.

```python
from datai.auto_plot import auto_plot
import pandas as pd

# Sample Data
data = {'Category': ['A', 'B', 'A', 'C', 'B', 'A'],
        'Value': [10, 15, 7, 12, 9, 11],
        'Group': ['X', 'Y', 'X', 'Y', 'X', 'Y']}
df = pd.DataFrame(data)

auto_plot(df)
```

This will print a summary of your data and display a selection of suggested plots, up to a maximum of 2 of each type.

#### Individual Plot Functions

You can also create specific plot types using the individual functions:

```python
from datai.auto_plot import (
    bar_chart, scatter_plot, histogram, heatmap, violin_plot, density_plot,
    pie_chart, stacked_bar_chart
)

# Example: Bar Chart
bar_chart(df, 'Category', 'Value', title='My Bar Chart', y_label='Custom Value')

# Example: Scatter Plot
scatter_plot(df, 'Value', df.index, title='Value vs Index')

# Example: Pie Chart
pie_chart(df, 'Category', title='Category Distribution')

# Example: Stacked Bar Chart
stacked_bar_chart(df, 'Category', 'Group')

# Example: Other plots
histogram(df, 'Value')
heatmap(df)  # Using the default numeric columns
violin_plot(df, 'Category', 'Value')
density_plot(df, 'Value')
```

### 3. Data Cleaning and Information

The `datai.data_cleaning` module provides functions for inspecting and cleaning your data.

#### 1. Data Information with `data_info`

The `data_info` function provides a detailed summary of your DataFrame:

```python
from datai.data_cleaning import data_info
import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35], 'City': ['New York', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)

data_info(df)
```

#### 2. Handling Missing Values with `handle_missing_values`

```python
from datai.data_cleaning import handle_missing_values

df_cleaned = handle_missing_values(df, method='mean', columns='Age')
print(df_cleaned)

# Example filling with constant value
df_cleaned = handle_missing_values(df, method='constant', columns='Age', fill_value=0)
```

#### 3. Removing Duplicates with `remove_duplicates`

```python
from datai.data_cleaning import remove_duplicates

df_no_duplicates = remove_duplicates(df, subset=['Name', 'Age'])  # considering only Name and Age
print(df_no_duplicates)
```

#### 4. Standardizing Column Names with `standardize_column_names`

```python
from datai.data_cleaning import standardize_column_names

df_standardized = standardize_column_names(df)
print(df_standardized)
```

#### 5. Converting Column Types with `convert_column_types`

```python
from datai.data_cleaning import convert_column_types

df_converted = convert_column_types(df, {'Age': 'int'})
print(df_converted.dtypes)
```

#### 6. Capping Outliers with `cap_outliers`

```python
from datai.data_cleaning import cap_outliers

df_capped = cap_outliers(df, columns='Salary', iqr_multiplier=1.5)
print(df_capped)
```

#### 7. Normalizing Data with `normalize_data`

```python
from datai.data_cleaning import normalize_data

df_normalized = normalize_data(df, columns=['Age', 'Salary'], method='minmax')
print(df_normalized)
```

#### 8. Bin Numeric Data with `bin_numeric_data`

```python
from datai.data_cleaning import bin_numeric_data

df_binned = bin_numeric_data(df, 'Age', bins=5)
print(df_binned)
```

#### 9. One Hot Encode Data with `one_hot_encode`

```python
from datai.data_cleaning import one_hot_encode

df_encoded = one_hot_encode(df, columns="Category")
print(df_encoded.head())
```

### 4. Data Utilities

The `datai.utils` module provides utility functions for validating data, ensuring column name compatibility, and performing safe data type conversions.

#### 1. Validate Dataset with `validate_dataset`

```python
from datai.utils import validate_dataset
import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
df = pd.DataFrame(data)

is_valid = validate_dataset(df)
print(f"Dataset is valid: {is_valid}")
```

#### 2. Safe Column Convert with `safe_column_convert`

```python
from datai.utils import safe_column_convert

df_converted = safe_column_convert(df, {'Age': 'float', 'Name': 'category'}, errors='ignore')
print(df_converted.dtypes)
```

#### 3. Library Data Summary with `library_data_summary`

```python
from datai.utils import library_data_summary

summary = library_data_summary(df)
print(summary)
```

#### 4. Column Name Compatibility with `column_name_compatibility`

```python
from datai.utils import column_name_compatibility

df = pd.DataFrame({'My Column': [1, 2, 3], 'Another Col!': ['A', 'B', 'C']})
df_compatible = column_name_compatibility(df)
print(df_compatible.columns)
```

### 5. Sound Visualization

The `datai.sound_visualization` module provides functions for visualizing sound signals.

#### Important: These functions require you to load the audio data into NumPy arrays before calling them. You can use libraries like librosa or scipy.io.wavfile for this.

#### 1. Load Audio Data

First, load your audio data using a library of your choice:

```python
# Example using librosa (you need to install it: pip install librosa)
import librosa
import numpy as np

audio_path = "path/to/your/audio.wav"  # Replace with your audio file
signal, sample_rate = librosa.load(audio_path, sr=None)  # Load audio file
```

#### 2. Visualize Waveform with `visualize_waveform`

```python
from datai.sound_visualization import visualize_waveform

visualize_waveform(signal, sample_rate, title="My Audio Waveform", file_path="my_waveform.png")
```

#### 3. Visualize FFT Spectrum with `visualize_fft`

```python
from datai.sound_visualization import visualize_fft

visualize_fft(signal, sample_rate, title="My Audio FFT", file_path="my_fft.png")
```

#### 4. Visualize Spectrogram with `visualize_spectrogram`

```python
from datai.sound_visualization import visualize_spectrogram

visualize_spectrogram(signal, sample_rate, title="My Audio Spectrogram", file_path="my_spectrogram.png", nfft=2048, noverlap=1024)
```

You can load the audio signal using different methods, here is a simple implementation using `generate_signal`, which is also another method from the same library.

```python
import numpy as np
import matplotlib.pyplot as plt
from datai import sound_visualization

# Generate a simple signal (e.g., a sine wave)
time, sine_wave = sound_visualization.generate_sine_wave(frequency=440, duration=2, sample_rate=8000)

# Visualize the waveform
sound_visualization.visualize_waveform(signal=sine_wave, sample_rate=8000, title='Simple Waveform', file_path="wave.png")

# Visualize multiple Waveform
signal1 = sound_visualization.generate_sine_wave(frequency=4, duration=2, sample_rate=8000)[1]
signal2 = sound_visualization.generate_cos_wave(frequency=5, duration=3, sample_rate=10000)[1]

sound_visualization.visualize_waveform_comparison(signals=[signal1, signal2], sample_rate=8000, file_path="both.png", title="Comp", titles=["sine", "cos"])

# Generate wave from a specific type with the method
time, saw_wave = sound_visualization.generate_signal(frequency=440, duration=2, sample_rate=8000, signal_type="sawtooth")

# Create combined WaveForm FFT graph
sound_visualization.visualize_waveform_fft(time, saw_wave, sample_rate=8000, file_path="combines.png")

# Visualize FFT:
sound_visualization.visualize_fft(signal=saw_wave, sample_rate=8000, title='FFT', file_path="fft.png")
```

### 6. Fun with Animations!

The `datai.gift` module provides functions for creating fun animations.

#### 1. Animate Typing Text with `animate_typing_text`

```python
from datai.gift import animate_typing_text

animate_typing_text("Datai is Typing...", file_path="typing.gif", duration=0.2)
```

This will animate the text with a typing effect and save it as "typing.gif".

#### 2. Animate Shape Swarms with `animate_shape_swarm`

Animate swarms of hearts, flowers, or stars! The hearts are now smaller and rainbow-colored.

```python
from datai.gift import animate_shape_swarm, heart, flower, star

# Animate a heart swarm
animate_shape_swarm(heart, num_shapes=30, file_path="hearts.gif", colors='rainbow', max_x=5, max_y=5)

# Animate a flower swarm
animate_shape_swarm(flower, file_path="flowers.gif", colors=['red', 'yellow', 'pink'])

# Animate a star swarm
animate_shape_swarm(star, file_path="stars.gif", colors='gold')
```

#### 3. Animate Game of Life with `animate_game_of_life`

Create an animation of Conway's Game of Life!

```python
from datai.gift import animate_game_of_life

animate_game_of_life(grid_size=50, file_path="game_of_life.gif")
```

#### 4. Create a Custom Animation with `create_custom_animation`

Create your own animations using a custom update function!

```python
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from datai.gift import create_custom_animation
import numpy as np

fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)
ax.set_xlim(0, 10)
ax.set_ylim(-1, 1)

def init():
    line.set_data([], [])
    return (line,)

def update(frame):
    x = np.linspace(0, 10, 1000)
    y = np.sin(2 * np.pi * (x - 0.01 * frame))
    line.set_data(x, y)
    return (line,)

create_custom_animation(update, init_func=init, num_frames=100, file_path="sine_wave.gif")
```

This creates a sine wave animation. The `init` function initializes the plot and is essential for blitting. The `update` function defines how the animation changes with each frame.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you have any suggestions or improvements.

## Contact

For any questions or feedback, please reach out at [m.ans.cs@outlook.com](mailto:m.ans.cs@outlook.com).

Thank you for using **Datai**! We hope it makes your data analysis journey easier and more enjoyable.

