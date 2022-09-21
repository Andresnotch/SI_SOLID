from abc import ABC, abstractmethod


class Chair(ABC):
	def __str__(self):
		return 'Chair'


class Sofa(ABC):
	def __str__(self):
		return 'Sofa'


class Table(ABC):
	def __str__(self):
		return 'Table'


class FurnitureFactory(ABC):
	@abstractmethod
	def createChair(self) -> Chair:
		pass

	@abstractmethod
	def createSofa(self) -> Sofa:
		pass

	@abstractmethod
	def createTable(self) -> Table:
		pass
