import numpy as np


"""
Klasa NeutralNetwork odpowiedzialna jest za obsługę sieci neuronowej.
Kod tej klasy inspirowany był zajęciami z SNiN oraz przykładem udostępnianym publicznie przez ImpiCode.
"""
class NeuralNetwork:

    """
    Konstruktor losujący początkowe wartości wag.
    
    Parametry:
    in_nb - ilość wejść,
    out_nb - ilość wyjść.
    """

    def __init__(self, in_nb, out_nb):
        np.random.seed(1)
        self.weights = 2 * np.random.random((in_nb, out_nb)) - 1

    ############################################################################################

    """
    Metoda sigmoid zwraca wartość funkcji logitowej dla danego argumentu.

    Parametry:
    x - argument, dla którego należy policzyć wartość

    Zwraca:
    Wartość funkcji matematycznej.
    """

    def sigmoid(self, x) -> float:
        
        return 1 / (1 + np.exp(-x))

    ############################################################################################

    """
    Metoda d_sigmoid zwraca wartość pochodnej funkcji logitowej dla danego argumentu.

    Parametry:
    x - argument, dla którego należy policzyć wartość

    Zwraca:
    Wartość funkcji matematycznej.
    """

    def d_sigmoid(self, x) -> float:

        return x * (1 - x)

    ############################################################################################

    """
    Metoda propagation przeprowadza iloczyn skalarny wektora wartości funkcji aktywacji i wektora wag.
    """

    def propagation(self, inputs):

        return self.sigmoid(np.dot(inputs.astype(float), self.weights))

    ############################################################################################

    """
    Metoda train przeprowadza uczenie sieci neuronowej - propagację oraz poprawkę wag.

    Parametry:
    train_input - wartości wejściowe,
    train_output - oczekiwane wartości wyjściowe,
    train_iters - liczba iteracji algorytmu.
    """

    def train(self, train_input, train_output, train_iters):
        
        for i in range(train_iters):
            
            propagation_result = self.propagation(train_input)

            self.correct_wages(propagation_result, train_input, train_output)    

    ############################################################################################

    """
    Metoda correct_wages przeprowadza poprawkę wag sieci.

    Parametry:
    propagation_result - realna wartość wyjściowa,
    train_input - wartość wejściowa,
    train_output - oczekiwana wartość wyjściowa.
    """

    def correct_wages(self, propagation_result, train_input, train_output):

        error = train_output - propagation_result

        self.weights += np.dot(train_input.T, error * self.d_sigmoid(propagation_result))
