from abc import ABC, abstractmethod
from typing import List
from random import random
from enum import Enum


class Layer(ABC):

	@property
	def parent(self):  # -> Node
		return self._parent

	@parent.setter
	def parent(self, parent):
		self._parent = parent

	@abstractmethod
	def print(self, indent: int = 0) -> str:
		pass

	@abstractmethod
	def weight(self) -> float:
		pass

	@abstractmethod
	def backprop(self, input: float) -> [float]:
		pass


class Neuron(Layer):

	def __init__(self, name: str) -> None:
		self.name = name
		self._weight = random()

	def weight(self) -> float:
		return self._weight

	def print(self, indent: int = 0) -> str:
		return ' ' * indent + '- ' + self.name + ' w: ' + str(self.weight()) + '\n'

	def backprop(self, input: float):
		return self._weight * input


class Network(Layer):

	def __init__(self, name: str) -> None:
		self.layers = []
		self.name = name

	def add_node(self, layer: Layer) -> None:
		self.layers.append(layer)
		layer.parent = self

	def delete_node(self, layer: Layer) -> None:
		self.layers.remove(layer)
		layer.parent = None

	def print(self, indent: int = 0) -> str:
		internal_structure = ' ' * indent + '+ ' + self.name + '\n'
		for child in self.layers:
			internal_structure += ' ' * indent + child.print(indent + 2)
		return internal_structure

	def weight(self) -> float:
		total_weight = 0
		for child in self.layers:
			total_weight += child.weight()
		return total_weight

	def backprop(self, input: [float]):
		result = 0
		if len(input) != len(self.layers):
			raise ValueError('Input shape does not match layer shape')
		for child, i in zip(self.layers, input):
			result += child.backprop(i)
		return result


if __name__ == "__main__":
	node1 = Neuron('1')
	node2 = Neuron('2')
	node3 = Neuron('3')

	network1 = Network('n1')
	network1.add_node(node1)
	network1.add_node(node2)
	network1.add_node(node3)

	print(network1.print())

	print(network1.backprop([1, 2, 3]))

	print(network1.weight())
