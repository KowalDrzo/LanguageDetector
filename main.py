#!/usr/bin/python3

from neural_network import *

train_inputs = np.array(
    [[0, 0, 0, 0], [1, 1, 1, 1]]
)

network = NeuralNetwork(4)

print(network.weights)

train_outputs = np.array([[1, 0]]).T

train_iterations = 50000

network.train(train_inputs, train_outputs, train_iterations)

print(network.weights)

print("Testing the data")
test_data = np.array([[1, 1, 1, 1], [1, 0, 0, 1], [0, 1, 1, 1], [0, 1, 0, 1]])

for data in test_data:
    print(f"Result for {data} is:")
    print(round(network.propagation(data)[-1], 3))
