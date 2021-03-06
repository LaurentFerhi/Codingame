import sys
import math
import numpy as np
from numpy import exp, array, random, dot

class NeuronLayer():
    def __init__(self, number_of_neurons, number_of_inputs_per_neuron):
        self.synaptic_weights = 2 * random.random((number_of_inputs_per_neuron, number_of_neurons)) - 1

class NeuralNetwork():
    def __init__(self, layer1, layer2):
        self.layer1 = layer1
        self.layer2 = layer2

    def __sigmoid(self, x):
        return 1 / (1 + exp(-x))

    def __sigmoid_derivative(self, x):
        return x * (1 - x)

    def train(self, training_set_inputs, training_set_outputs, number_of_training_iterations):
        for iteration in range(number_of_training_iterations):

            output_from_layer_1, output_from_layer_2 = self.think(training_set_inputs)

            layer2_error = training_set_outputs - output_from_layer_2
            layer2_delta = layer2_error * self.__sigmoid_derivative(output_from_layer_2)
            
            layer1_error = layer2_delta.dot(self.layer2.synaptic_weights.T)
            layer1_delta = layer1_error * self.__sigmoid_derivative(output_from_layer_1)

            layer1_adjustment = training_set_inputs.T.dot(layer1_delta)
            layer2_adjustment = output_from_layer_1.T.dot(layer2_delta)

            self.layer1.synaptic_weights += layer1_adjustment
            self.layer2.synaptic_weights += layer2_adjustment

    def think(self, inputs):
        output_from_layer1 = self.__sigmoid(dot(inputs, self.layer1.synaptic_weights))
        output_from_layer2 = self.__sigmoid(dot(output_from_layer1, self.layer2.synaptic_weights))
        return output_from_layer1, output_from_layer2

tests, training_sets = [int(i) for i in input().split()]
X_test = []
for i in range(tests):
    x_test_i = input()
    X_test.append([int(i) for i in list(x_test_i)])

X_train = []
y_train = []
for i in range(training_sets):
    x_train_i, y_train_i = input().split()
    X_train.append([int(i) for i in list(x_train_i)])
    y_train.append(y_train_i)

X_train = np.array(X_train)
X_test = np.array(X_test)

i = 0
dico = {}
for label in list(set(y_train)):
    dico[label] = i
    i+=1

y_encoded = []
for label in y_train:
    y_encoded.append(dico[label])

y_train = np.array([y_encoded]).T

print(X_train.shape,y_train.shape, file=sys.stderr)

layer1 = NeuronLayer(30, X_train.shape[1])
layer2 = NeuronLayer(1, 30)
neural_network = NeuralNetwork(layer1, layer2)

neural_network.train(X_train, y_train, 60000)

for x_test_i in X_test:
    hidden_state, output = neural_network.think(x_test_i)
    print(output[0])
