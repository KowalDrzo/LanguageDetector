from sympy import Symbol,plot
import matplotlib.pyplot as plt

def draw_plot(x_vals: list, y_vals: list):
    
    fig = plt.figure()
    
    plt.title("Wizualizacja wyniku detekcji języków")
    plt.bar(x_vals, y_vals)
    plt.grid()
    plt.show()