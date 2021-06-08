from sympy import Symbol,plot
import matplotlib.pyplot as plt

def draw_plot(x_vals: list, y_vals: list):
    
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
    
    ax.bar(x_vals, y_vals)
    plt.grid()
    plt.show()