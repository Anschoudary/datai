import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from typing import Union, List, Callable

# --- Helper Functions for Shapes ---

def heart(x, y, size):
    """Generates coordinates for a heart shape."""
    t = np.linspace(0, 2 * np.pi, 100)
    x_heart = size * 16 * (np.sin(t)**3) + x
    y_heart = size * (13*np.cos(t) - 5*np.cos(2*t) - 2*np.cos(3*t) - np.cos(4*t)) + y
    return x_heart, y_heart

def flower(x, y, size):
    """Generates coordinates for a simple flower shape."""
    t = np.linspace(0, 2 * np.pi, 100)
    x_flower = size * np.cos(6*t) * np.cos(t) + x
    y_flower = size * np.cos(6*t) * np.sin(t) + y
    return x_flower, y_flower

def star(x, y, size):
    """Generates coordinates for a star shape."""
    outer_radius = size
    inner_radius = size / 2.5
    n = 5  # Number of points in the star
    outer_angles = np.linspace(np.pi / 2, 2 * np.pi + np.pi / 2, 2 * n, endpoint=False)
    inner_angles = outer_angles + np.pi / n

    x_outer = outer_radius * np.cos(outer_angles) + x
    y_outer = outer_radius * np.sin(outer_angles) + y
    x_inner = inner_radius * np.cos(inner_angles) + x
    y_inner = inner_radius * np.sin(inner_angles) + y

    x_star = np.concatenate([x_outer[::2], x_inner[::2]])
    y_star = np.concatenate([y_outer[::2], y_inner[::2]])

    return x_star, y_star

# --- Animation Functions ---

def animate_typing_text(text: str, colors: Union[str, List[str]] = 'rainbow', font_size: int = 24,
                       file_path: str = None, duration: float = 0.5, datai_label: bool = True) -> None:
    """
    Animates text with a typing effect, showing characters accumulate sequentially.

    Args:
        text (str): The text to animate.
        colors (Union[str, List[str]], optional): Colors for the characters. Defaults to 'rainbow'.
        font_size (int, optional): The font size of the text. Defaults to 24.
        file_path (str, optional): The path to save the animation as a GIF. If None, the animation is not saved.
        duration (float, optional): The duration (in seconds) to display each character. Defaults to 0.2.
        datai_label (bool, optional): Whether to add "Datai" label in the bottom right corner. Defaults to True.
    """

    fig, ax = plt.subplots()
    ax.axis('off')

    if colors == 'rainbow':
        color_cycle = plt.cm.rainbow(np.linspace(0, 1, len(text)))
        colors = [plt.cm.colors.to_hex(color) for color in color_cycle]
    elif isinstance(colors, str):
        colors = [colors] * len(text)
    elif len(colors) < len(text):
        colors = colors * (len(text) // len(colors) + 1)
        colors = colors[:len(text)]

    text_element = ax.text(0.5, 0.5, '', color=colors[0], fontsize=font_size, ha='center', va='center')

    def update(num):
        current_text = text[:num+1]  # Show accumulated text
        text_element.set_text(current_text)
        return text_element,

    ani = animation.FuncAnimation(fig, update, frames=len(text), repeat=False)

    if datai_label:
        ax.text(0.95, 0.05, "Datai", color='gray', fontsize=8, ha='right', va='bottom', transform=ax.transAxes)

    plt.tight_layout()
    plt.show()

    if file_path:
        try:
            ani.save(file_path, writer='pillow', fps=1 / duration)
            print(f"Animation saved to {file_path}")
        except Exception as e:
            print(f"Error saving animation: {e}. Ensure you have Pillow installed.")


def animate_shape_swarm(shape_func: Callable, num_shapes: int = 50, colors: Union[str, List[str]] = 'rainbow',
                       file_path: str = None, duration: float = 0.05, datai_label: bool = True, max_x = 8, max_y = 8) -> None:
    """
    Animates a swarm of shapes moving randomly.

    Args:
        shape_func (Callable): A function that generates coordinates for a single shape.
            The function should take x, y, and size as arguments. Ex: heart, flower, star.
        num_shapes (int, optional): The number of shapes in the swarm. Defaults to 50.
        colors (Union[str, List[str]], optional): Colors for the shapes. Defaults to 'cool'.
        file_path (str, optional): The path to save the animation as a GIF. If None, the animation is not saved.
        duration (float, optional): The duration (in seconds) between each frame. Defaults to 0.05.
        datai_label (bool, optional): Whether to add "Datai" label in the bottom right corner. Defaults to True.
    """

    fig, ax = plt.subplots()
    ax.set_xlim(-max_x, max_x)
    ax.set_ylim(-max_y, max_y)
    ax.set_aspect('equal') # Keep the aspect ratio equal
    ax.axis('off')

    # Initialize shape positions and sizes
    x_positions = np.random.uniform(-max_x + 1, max_x - 1, num_shapes) # ensure they start within bounds
    y_positions = np.random.uniform(-max_y + 1, max_y - 1, num_shapes)
    sizes = np.random.uniform(0.1, 0.3, num_shapes) #Smaller sizes

    # Determine colors
    if colors == 'rainbow':
        color_cycle = plt.cm.rainbow(np.linspace(0, 1, num_shapes))
        colors = [plt.cm.colors.to_hex(color) for color in color_cycle]
    elif isinstance(colors, str):
        colors = [colors] * num_shapes
    elif len(colors) < num_shapes:
        colors = colors * (num_shapes // len(colors) + 1)
        colors = colors[:num_shapes]

    # Create shapes
    shapes = []
    for i in range(num_shapes):
        x, y = shape_func(x_positions[i], y_positions[i], sizes[i])
        shape = ax.fill(x, y, color=colors[i], animated=True)[0]  # Use fill for solid shapes, return the PolyCollection
        shapes.append(shape)

    def update(frame):
        # Update shape positions
        x_positions[:] += np.random.normal(0, 0.05, num_shapes)  # Smaller steps
        y_positions[:] += np.random.normal(0, 0.05, num_shapes)

        # Keep shapes within bounds
        x_positions[:] = np.clip(x_positions, -max_x + 1, max_x - 1)
        y_positions[:] = np.clip(y_positions, -max_y + 1, max_y - 1)

        # Update shape data
        for i, shape in enumerate(shapes):
            x, y = shape_func(x_positions[i], y_positions[i], sizes[i])
            shape.set_xy(np.c_[x, y]) # Update the vertices of the filled polygon
        return shapes

    ani = animation.FuncAnimation(fig, update, frames=100, blit=True, repeat=True)  # blit = True can improve performance

    if datai_label:
        ax.text(0.95, 0.05, "Datai", color='gray', fontsize=8, ha='right', va='bottom', transform=ax.transAxes)

    plt.tight_layout()
    plt.show()

    if file_path:
        try:
            ani.save(file_path, writer='pillow', fps=1 / duration)
            print(f"Animation saved to {file_path}")
        except Exception as e:
            print(f"Error saving animation: {e}. Ensure you have Pillow installed.")


def animate_game_of_life(grid_size: int = 50, file_path: str = None, duration: float = 0.1, datai_label: bool = True, color_map: str = 'magma') -> None:
    """
    Animates Conway's Game of Life.

    Args:
        grid_size (int, optional): The size of the Game of Life grid (grid_size x grid_size). Defaults to 50.
        file_path (str, optional): The path to save the animation as a GIF. If None, the animation is not saved.
        duration (float, optional): The duration (in seconds) between each frame. Defaults to 0.1.
        datai_label (bool, optional): Whether to add "Datai" label in the bottom right corner. Defaults to True.
        color_map (str, optional): The Matplotlib colormap to use for the cells. Defaults to 'magma'.
    """

    def generate_random_grid(size):
        """Generates a random grid for Game of Life."""
        return np.random.choice([0, 1], size=(size, size), p=[0.5, 0.5])

    def update_grid(grid):
        """Updates the Game of Life grid based on the rules."""
        new_grid = grid.copy()
        for i in range(grid.shape[0]):
            for j in range(grid.shape[1]):
                # Calculate the number of live neighbors
                total = int((
                    grid[ (i-1) % grid.shape[0], (j-1) % grid.shape[1]] +
                    grid[ (i-1) % grid.shape[0], j                 ] +
                    grid[ (i-1) % grid.shape[0], (j+1) % grid.shape[1]] +
                    grid[ i                 , (j-1) % grid.shape[1]] +
                    grid[ i                 , (j+1) % grid.shape[1]] +
                    grid[ (i+1) % grid.shape[0], (j-1) % grid.shape[1]] +
                    grid[ (i+1) % grid.shape[0], j                 ] +
                    grid[ (i+1) % grid.shape[0], (j+1) % grid.shape[1]]
                ))

                # Apply Game of Life rules
                if grid[i, j] == 1:
                    if (total < 2) or (total > 3):
                        new_grid[i, j] = 0
                else:
                    if total == 3:
                        new_grid[i, j] = 1
        return new_grid

    grid = generate_random_grid(grid_size)

    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest', cmap=color_map)
    ax.axis('off')

    def update(frame):
        nonlocal grid # Allow modification of the grid variable
        grid = update_grid(grid)
        img.set_data(grid)
        return [img]

    ani = animation.FuncAnimation(fig, update, frames=100, blit=True, repeat=True)

    if datai_label:
        ax.text(0.95, 0.05, "Datai", color='gray', fontsize=8, ha='right', va='bottom', transform=ax.transAxes)

    plt.tight_layout()
    plt.show()

    if file_path:
        try:
            ani.save(file_path, writer='pillow', fps=1 / duration)
            print(f"Animation saved to {file_path}")
        except Exception as e:
            print(f"Error saving animation: {e}. Ensure you have Pillow installed.")


def animate_spiral(colors: Union[str, List[str]] = 'viridis', num_points: int = 100,
                   file_path: str = None, duration: float = 0.05, datai_label: bool = True) -> None:
    """
    Animates a growing spiral.

    Args:
        colors (Union[str, List[str]], optional): Colors for the spiral points. Defaults to 'viridis'.
        num_points (int, optional): The number of points in the spiral. Defaults to 100.
        file_path (str, optional): The path to save the animation as a GIF. If None, the animation is not saved.
        duration (float, optional): The duration (in seconds) between each frame. Defaults to 0.05.
        datai_label (bool, optional): Whether to add "Datai" label in the bottom right corner. Defaults to True.

    Returns:
        None
    """

    fig, ax = plt.subplots()
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.axis('off')

    if colors == 'viridis':
        color_cycle = plt.cm.viridis(np.linspace(0, 1, num_points))
        colors = [plt.cm.colors.to_hex(color) for color in color_cycle]
    elif isinstance(colors, str):
        colors = [colors] * num_points
    elif len(colors) < num_points:
        colors = colors * (num_points // len(colors) + 1)
        colors = colors[:num_points]

    scat = ax.scatter([], [], s=50, c=[], cmap='viridis')

    def update(frame):
        angle = np.linspace(0, 8 * np.pi, num_points)  # Increased spiral density
        radius = np.linspace(0, 5, num_points)
        x = radius * np.cos(angle + frame * 0.1)
        y = radius * np.sin(angle + frame * 0.1)

        scat.set_offsets(np.c_[x, y])
        scat.set_color(colors) # Keep the assigned colors
        return (scat,)

    ani = animation.FuncAnimation(fig, update, frames=200, repeat=True)  # More frames
    if datai_label:
        ax.text(0.95, 0.05, "Datai", color='gray', fontsize=8, ha='right', va='bottom', transform=ax.transAxes)

    plt.tight_layout()
    plt.show()

    if file_path:
        try:
            ani.save(file_path, writer='pillow', fps=1 / duration)
            print(f"Animation saved to {file_path}")
        except Exception as e:
            print(f"Error saving animation: {e}. Ensure you have Pillow installed.")


def animate_bars(data: List[float], labels: List[str], colors: Union[str, List[str]] = 'plasma',
                   file_path: str = None, duration: float = 0.2, datai_label: bool = True) -> None:
    """
    Animates a bar chart, with bars growing sequentially.

    Args:
        data (List[float]): The data values for the bars.
        labels (List[str]): The labels for the bars.
        colors (Union[str, List[str]], optional): Colors for the bars. Defaults to 'plasma'.
        file_path (str, optional): The path to save the animation as a GIF. If None, the animation is not saved.
        duration (float, optional): The duration (in seconds) to display each frame. Defaults to 0.2.
        datai_label (bool, optional): Whether to add "Datai" label in the bottom right corner. Defaults to True.

    Returns:
        None
    """
    fig, ax = plt.subplots()
    ax.set_xlim(0, len(data))
    ax.set_ylim(0, max(data) * 1.1)
    ax.set_xticks(np.arange(len(data)))  # Set x-ticks to integers
    ax.set_xticklabels(labels, rotation=45, ha="right")  # Rotate labels for readability
    ax.set_ylabel("Value")
    ax.set_title("Animated Bar Chart")

    if colors == 'plasma':
        color_cycle = plt.cm.plasma(np.linspace(0, 1, len(data)))
        colors = [plt.cm.colors.to_hex(color) for color in color_cycle]
    elif isinstance(colors, str):
        colors = [colors] * len(data)
    elif len(colors) < len(data):
        colors = colors * (len(data) // len(colors) + 1)
        colors = colors[:len(data)]

    bars = ax.bar(np.arange(len(data)), [0] * len(data), color=colors)

    def update(frame):
        for i, bar in enumerate(bars):
            if i <= frame:
                bar.set_height(data[i])
            else:
                bar.set_height(0)
        return bars

    ani = animation.FuncAnimation(fig, update, frames=len(data), repeat=False)

    if datai_label:
        ax.text(0.95, 0.05, "Datai", color='gray', fontsize=8, ha='right', va='bottom', transform=ax.transAxes)

    plt.tight_layout()
    plt.show()

    if file_path:
        try:
            ani.save(file_path, writer='pillow', fps=1 / duration)
            print(f"Animation saved to {file_path}")
        except Exception as e:
            print(f"Error saving animation: {e}. Ensure you have Pillow installed.")


def create_custom_animation(update_func: Callable, init_func: Callable = None, num_frames: int = 100, file_path: str = None,
                             duration: float = 0.1, datai_label: bool = True) -> None:
    """
    Creates a custom animation using a user-defined update function. This is a very flexible function.

    Args:
        update_func (Callable): A function that updates the animation for each frame.  Must take a number as argument
        init_func (Callable, optional): A function to initialize the animation. Defaults to None.
        num_frames (int, optional): The number of frames in the animation. Defaults to 100.
        file_path (str, optional): The path to save the animation as a GIF. If None, the animation is not saved.
        duration (float, optional): The duration (in seconds) between each frame. Defaults to 0.1.
        datai_label (bool, optional): Whether to add "Datai" label in the bottom right corner. Defaults to True.
    """
    fig, ax = plt.subplots()

    if init_func is None:
        def init():
            return []
        init_func = init

    ani = animation.FuncAnimation(fig, update_func, init_func=init_func, frames=num_frames, blit=True, repeat=True)

    if datai_label:
        ax.text(0.95, 0.05, "Datai", color='gray', fontsize=8, ha='right', va='bottom', transform=ax.transAxes)

    plt.tight_layout()
    plt.show()

    if file_path:
        try:
            ani.save(file_path, writer='pillow', fps=1 / duration)
            print(f"Animation saved to {file_path}")
        except Exception as e:
            print(f"Error saving animation: {e}. Ensure you have Pillow installed.")


def save_animation(ani: animation.FuncAnimation, file_path: str, duration: float = 0.2, datai_label: bool = True) -> None:
    """
    Saves a matplotlib animation to a file (e.g., GIF).

    Args:
        ani (animation.FuncAnimation): The animation object to save.
        file_path (str): The path to save the animation.  Must include the file extension (e.g., "my_animation.gif").
        duration (float, optional): The duration (in seconds) of each frame in the saved animation. Defaults to 0.2.
        datai_label (bool, optional): Whether to add "Datai" label in the bottom right corner. Defaults to True.
    """
    try:
        ani.save(file_path, writer='pillow', fps=1 / duration)
        print(f"Animation saved to {file_path}")
    except Exception as e:
        print(f"Error saving animation: {e}. Ensure you have Pillow and the correct writer installed.\nError details: {e}")



