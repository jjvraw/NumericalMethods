import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
from scipy import cos

# Function
def f(x):
    return cos(x)

# Fixed-point iteration
def fixed_point(func, guess, iterations):
    x = guess
    steps = [x]
    for i in range(iterations):
        x = func(x)
        steps.append(x)
    return steps

# Initial guess
x0 = 2.0

# Perform the iterations
steps = fixed_point(f, x0, 50)

# Create the figure and axes
fig, ax = plt.subplots()

# Plot y = cos(x) and y = x
x = np.linspace(-1, 3, 400)
ax.plot(x, f(x), label='y = cos(x)')
ax.plot(x, x, label='y = x')

# Create a smaller subplot for the button
button_ax = plt.axes([0.81, 0.01, 0.1, 0.075])

# Line data
xdata, ydata = [], []

# Initial red line
line, = ax.plot([], [], 'r')

# Animation update function
def update(i):
    xdata.extend([steps[i], steps[i], steps[i+1]])
    ydata.extend([steps[i], steps[i+1], steps[i+1]])
    line.set_data(xdata, ydata)
    return line,

# Add some labels, a legend, and a grid
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend()
ax.grid(True)

# Current frame
current_frame = [0]

# Update function that moves to the next frame
def next_frame(event):
    current_frame[0] += 1
    if current_frame[0] >= len(steps) - 1:
        current_frame[0] = len(steps) - 2
    update(current_frame[0])
    fig.canvas.draw()

# Button
next_button = Button(button_ax, 'Next')
next_button.on_clicked(next_frame)

# Show the plot
plt.show()
