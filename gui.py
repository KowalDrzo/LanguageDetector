from neural_network import *
from text_parser import Parser
from tkinter import *
import drawer as dr

"""
Klasa Menu odpowiedzialna jest za wyświetlanie i obsługę menu - wywoływanie metod sieci neuronowej i parsera.
"""
class Menu:

    root = Tk()
    network = None
    parser = Parser()

    text_entry = None
    out_text_var = StringVar()

    lang_tab = ["Angielski:", "Niemiecki:", "Polski:   ", "Czeski:   ", "Włoski:   ", "Rosyjski (tr.):"]

    ############################################################################################

    def display_menu(self):

        self.network = NeuralNetwork(676, len(self.lang_tab))
        np.set_printoptions(formatter={"float": lambda x: "{0:0.6f}".format(x)}, threshold=np.inf)

        self.root.geometry("640x480")
        self.root.title("Detektor języków")

        b_width = 32

        option1 = Button(self.root, width = b_width, text ="Uczenie sieci",                      command = self.option1_callback)
        option2 = Button(self.root, width = b_width, text ="Detekcja języka wpisanego tekstu",   command = self.option2_callback)
        option3 = Button(self.root, width = b_width, text ="Pokaż wagi",                         command = self.option3_callback)

        option_exit = Button(self.root, width = b_width, text ="Wyjdź",                          command = self.option_exit_callback)

        self.text_entry = Entry(self.root, width = b_width * 2)
        self.text_entry.insert(0, "Miejsce na tekst w obsługiwanym języku")
        out_text = Label(self.root, textvariable = self.out_text_var, justify = LEFT)

        option1.pack()
        self.text_entry.pack()
        option2.pack()
        option3.pack()
        option_exit.pack()

        out_text.pack()

        self.root.mainloop()

    ############################################################################################

    def option1_callback(self):

        self.parser.show_info = True

        print(self.lang_tab[0])
        eng_data = self.parser.parse_file("TrainingTexts/english.txt")

        print(self.lang_tab[1])
        ger_data = self.parser.parse_file("TrainingTexts/german.txt")

        print(self.lang_tab[2])
        pol_data = self.parser.parse_file("TrainingTexts/polish.txt")

        print(self.lang_tab[3])
        cze_data = self.parser.parse_file("TrainingTexts/czech.txt")

        print(self.lang_tab[4])
        ita_data = self.parser.parse_file("TrainingTexts/italian.txt")

        print(self.lang_tab[5])
        rus_data = self.parser.parse_file("TrainingTexts/russian.txt")

        self.parser.show_info = False

        train_inputs = np.array([eng_data, ger_data, pol_data, cze_data, ita_data, rus_data])
        train_outputs = np.identity(len(self.lang_tab))

        train_iterations = 80000
        print("Iteracje uczenia: " + str(train_iterations))

        self.network.train(train_inputs, train_outputs, train_iterations)

        self.parser.save_weights(self.network.weights)
        print("\nWagi zostały zapisane")

    ############################################################################################

    def option2_callback(self):
        
        self.network.weights = self.parser.load_weights()

        test_data = np.array( [self.parser.parse_string(self.text_entry.get())] )

        result = self.network.propagation(test_data[0])

        out_str = "Wynik detekcji:\n"
        for i in range(len(self.lang_tab)):
            out_str = out_str + str(self.lang_tab[i]) + "\t" + "{0:.2%}".format(result[i]) + "\n"

        dr.draw_plot(self.lang_tab, result)

        self.out_text_var.set(out_str)
        print(out_str)

    ############################################################################################

    def option3_callback(self):

        print("\nWagi sieci:")
        print(self.network.weights)

    ############################################################################################

    def option_exit_callback(self):
        exit()