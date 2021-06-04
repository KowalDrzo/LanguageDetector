#!/usr/bin/python3

from neural_network import *
import text_parser as tp

"""
train_inputs = np.array( [[0, 0, 0, 0], [1, 1, 1, 1]] )

network = NeuralNetwork(4)

print(network.weights)

train_outputs = np.array([[1, 0]]).T

train_iterations = 50000

network.train(train_inputs, train_outputs, train_iterations)

print(network.weights)

print("Testing the data")
test_data = np.array( [[1, 1, 1, 1], [1, 0, 0, 1], [0, 1, 1, 1], [0, 1, 0, 1]] )

for data in test_data:
    print(f"Result for {data} is:")
    print(round(network.propagation(data)[-1], 3))
"""

eng_data = tp.parse_file("TrainingTexts/english.txt")
ger_data = tp.parse_file("TrainingTexts/german.txt")
pol_data = tp.parse_file("TrainingTexts/polish.txt")

train_inputs = np.array([eng_data, ger_data, pol_data])

network = NeuralNetwork(676)

#print(network.weights)

train_outputs = np.array([[0, 0, 1]]).T

train_iterations = 1000

network.train(train_inputs, train_outputs, train_iterations)

#print(network.weights)

input_text = input("Podaj słowo lub zdanie: ")
#test_data = tp.parse_string(input_text)

#print(f"Result for {test_data} is:")
#print(round(network.propagation(np.array(test_data)), 3))

test_data = np.array( [tp.parse_string(input_text)] )

for data in test_data:
    #print(f"Result for {data} is:")
    print(network.propagation(data))


train_inputs = np.array([eng_data, ger_data, pol_data])

network = NeuralNetwork(676)

train_outputs = np.array([[1, 0, 0]]).T

train_iterations = 1000

network.train(train_inputs, train_outputs, train_iterations)

test_data = np.array( [tp.parse_string(input_text)] )

for data in test_data:
    #print(f"Result for {data} is:")
    print(round(network.propagation(data)[-1], 3))



train_inputs = np.array([eng_data, ger_data, pol_data])

network = NeuralNetwork(676)

train_outputs = np.array([[0, 1, 0]]).T

train_iterations = 1000

network.train(train_inputs, train_outputs, train_iterations)

test_data = np.array( [tp.parse_string(input_text)] )

for data in test_data:
    #print(f"Result for {data} is:")
    print(round(network.propagation(data)[-1], 3))