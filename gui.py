from neural_network import *
from text_parser import Parser
from tkinter import *

class Menu:

    root = Tk()
    network = NeuralNetwork(676, 3)
    parser = Parser()

    def display_menu(self):

        self.root.geometry("640x480")
        self.root.title("Detektor języków")

        b_width = 32

        option1 = Button(self.root, width = b_width, text ="Uczenie sieci",                      command = self.option1_callback)
        option2 = Button(self.root, width = b_width, text ="Detekcja języka wpisanego tekstu",   command = self.option2_callback)

        option_exit = Button(self.root, width = b_width, text ="Wyjdź",                          command = self.option_exit_callback)

        option1.pack()
        option2.pack()
        option_exit.pack()

        self.root.mainloop()

    ############################################################################################

    def option1_callback(self):
        
        eng_data = self.parser.parse_file("TrainingTexts/english.txt")
        ger_data = self.parser.parse_file("TrainingTexts/german.txt")
        pol_data = self.parser.parse_file("TrainingTexts/polish.txt")

        train_inputs = np.array([eng_data, ger_data, pol_data])
        np.set_printoptions(threshold=np.inf)

        print("\nPoczątkowe wagi sieci:")
        print(self.network.weights)

        train_outputs = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]]).T

        train_iterations = 80000
        print("Iteracje uczenia: " + str(train_iterations))

        self.network.train(train_inputs, train_outputs, train_iterations)

        print("\nWagi sieci po uczeniu:")
        print(self.network.weights)
        self.parser.save_weights(self.network.weights)

    ############################################################################################

    def option2_callback(self):
        pass

    ############################################################################################

    def option_exit_callback(self):
        exit()