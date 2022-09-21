"""
Equipo:
Carlos Andrés Hidalgo Martí
Carlos Rogelio Quirarte Vázquez
"""

from abc import ABC, abstractmethod
from typing import Type, TypeVar


class Network(ABC):

	def __init__(self):
		self._layers = []

	@property
	@abstractmethod
	def layers(self):
		pass

	@property
	@abstractmethod
	def inputLayer(self):
		pass

	@abstractmethod
	def reset(self):
		pass

	@abstractmethod
	def train(self, data: []) -> []:
		pass

	@abstractmethod
	def add_layer(self, layer):
		pass


class RecurrentNetwork(Network):

	def __init__(self):
		super().__init__()
		self.name = 'Recurrent Network'

	@property
	def layers(self):
		return self._layers

	@layers.setter
	def layers(self, value):
		self._layers = value

	@property
	def inputLayer(self):
		if len(self.layers):
			return self.layers[0]
		else:
			return None

	def reset(self):
		self.layers = []

	def train(self, data: []) -> []:
		print(self.name + ' Training...')

	def add_layer(self, layer):
		self.layers.append(layer)


class SequentialNetwork(Network):

	def __init__(self):
		super().__init__()
		self.name = 'Sequential Network'

	@property
	def layers(self):
		return self._layers

	@layers.setter
	def layers(self, value):
		self._layers = value

	@property
	def inputLayer(self):
		if len(self.layers):
			return self.layers[0]
		else:
			return None

	def reset(self):
		self.layers = []

	def train(self, data: []) -> []:
		print(self.name + ' Training...')

	def add_layer(self, layer):
		self.layers.append(layer)


class NetworkBuilder(ABC):

	@property
	@abstractmethod
	def network(self) -> Network:
		pass

	@abstractmethod
	def reset(self) -> None:
		pass

	@abstractmethod
	def addPreprocessing(self) -> None:
		pass

	@abstractmethod
	def addInputs(self) -> None:
		pass

	@abstractmethod
	def addHidden(self) -> None:
		pass

	@abstractmethod
	def addOutputs(self) -> None:
		pass


class RecurrentNetworkBuilder(NetworkBuilder):

	def __init__(self):
		self._network: RecurrentNetwork = RecurrentNetwork()

	@property
	def network(self) -> RecurrentNetwork:
		return self._network

	def reset(self) -> None:
		self._network: Network = RecurrentNetwork()

	def addPreprocessing(self) -> None:
		"""
		Recurrent network does not need preprocessing
		:return:
		"""
		pass

	def addInputs(self) -> None:
		self.network.add_layer('Input')

	def addHidden(self) -> None:
		self.network.add_layer('Hidden')

	def connect_recurrence(self) -> None:
		self.network.add_layer('Recurrent layer')

	def addOutputs(self) -> None:
		self.network.add_layer('Output')


class SequentialNetworkBuilder(NetworkBuilder):

	def __init__(self):
		self._network: SequentialNetwork = SequentialNetwork()

	@property
	def network(self) -> SequentialNetwork:
		return self._network

	def reset(self) -> None:
		self._network: Network = SequentialNetwork()

	def addPreprocessing(self) -> None:
		self.network.add_layer('Preprocessing')

	def addInputs(self) -> None:
		self.network.add_layer('Input')

	def addHidden(self) -> None:
		self.network.add_layer('Hidden')

	def addOutputs(self) -> None:
		self.network.add_layer('Output')


B = TypeVar('B', bound=NetworkBuilder)


class NetworkDesigner:
	"""
	Director class
	"""

	def __init__(self, builder):
		self._builder: Type[B] = builder

	@property
	def builder(self):
		return self._builder

	def changeBuilder(self, builder: NetworkBuilder) -> None:
		self._builder: NetworkBuilder = builder

	def make(self) -> Network:
		if type(self.builder) == SequentialNetworkBuilder:
			return self.create_sequential()
		elif type(self.builder) == RecurrentNetworkBuilder:
			return self.create_recurrent()
		else:
			raise ValueError('The current builder is not supported')

	def create_sequential(self) -> SequentialNetwork:
		self.builder.addPreprocessing()
		self.builder.addInputs()
		self.builder.addHidden()
		self.builder.addOutputs()
		return self.builder.network

	def create_recurrent(self) -> RecurrentNetwork:
		self.builder.addInputs()
		self.builder.addHidden()
		self.builder.connect_recurrence()
		self.builder.addOutputs()
		return self.builder.network
