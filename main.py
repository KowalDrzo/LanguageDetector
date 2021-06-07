#!/usr/bin/python3

from gui import Menu

"""
eng_data = tp.parse_file("TrainingTexts/english.txt")
ger_data = tp.parse_file("TrainingTexts/german.txt")
pol_data = tp.parse_file("TrainingTexts/polish.txt")

train_inputs = np.array([eng_data, ger_data, pol_data])

network = NeuralNetwork(676, 3)

#print(network.weights)

train_outputs = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]]).T

train_iterations = 80000

network.train(train_inputs, train_outputs, train_iterations)

#print(network.weights)
"""

"""
input_text = input("Podaj słowo lub zdanie: ")
#test_data = tp.parse_string(input_text)

#print(f"Result for {test_data} is:")
#print(round(network.propagation(np.array(test_data)), 3))

test_data = np.array( [tp.parse_string(input_text)] )

for data in test_data:
    #print(f"Result for {data} is:")
    print(network.propagation(data))
"""

menu = Menu()
menu.display_menu()