# datai/myname.py

import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Function to animate the characters
def myName(name):

    # Create a list of characters in the name
    chars = list(name.upper())

    # Create a list of x-coordinates (one for each character)
    x = range(len(chars))

    # Create a list of y-coordinates (all set to 0)
    y = [0] * len(chars)

    # Create a figure and axis
    fig, ax = plt.subplots(figsize=(12, 6))

    # Initialize the plot with no characters
    ax.set_xlim(-1, len(chars))
    ax.set_ylim(-1, 1)
    ax.axis('off')

    # Function to update the plot for each frame
    def update(frame):
        ax.set_facecolor('black')
        ax.clear()
        ax.set_xlim(-1, len(chars))
        ax.set_ylim(-1, 1)
        ax.axis('off')
        for i in range(frame+1):
            ax.text(x[i], y[i], chars[i], 
                    fontsize=56, 
                    ha='center', 
                    color='blue', 
                    fontstyle='italic')

    # Create the animation
    anim = animation.FuncAnimation(fig, update, frames=len(chars), interval=400)

    # Show the animation
    plt.show()


# Example usage
name = "Hello, World!"
myName(name)
