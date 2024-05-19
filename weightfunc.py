import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

size = 3

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)

def weightfunc(a, n):
    x = np.linspace(0, size*size, 1000)
    y = 1 - (x/a)**n

    ax.clear()
    ax.plot(x, y)
    ax.set_title(f'Distribution for a={a} n={n}')
    ax.set_xlabel('Number of MAX cells')
    ax.set_ylabel('Probability of generation')
    ax.grid(True)
    plt.draw()


a_slider_ax = plt.axes([0.25, 0.1, 0.65, 0.03])
n_slider_ax = plt.axes([0.25, 0.05, 0.65, 0.03])

a_slider = Slider(a_slider_ax, 'a', 10.0, 1000.0, valinit=225.0)
n_slider = Slider(n_slider_ax, 'n', 0.1, 5.0, valinit=2.0)

a_slider.on_changed(lambda val: weightfunc(val, n_slider.val))
n_slider.on_changed(lambda val: weightfunc(a_slider.val, val))

weightfunc(a_slider.val, n_slider.val)
plt.show()