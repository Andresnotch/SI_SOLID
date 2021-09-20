from abc import ABC, abstractmethod


class Producto(ABC):
	def __init__(self, nombre: str, precio: float, descripcion: str, alergenos: [str]):
		self.nombre: str = nombre
		self.precio: float = precio
		self.descripcion: str = descripcion
		self.alergenos: [str] = alergenos

	def __str__(self):
		return self.nombre

	@abstractmethod
	def no_cobrar(self, razon: str) -> bool:
		pass


class Bebida(Producto):
	def __init__(self, nombre: str, precio: float, descripcion: str, alergenos: [str], ml: float,
	             alcoholica: bool = False):
		super().__init__(nombre, precio, descripcion, alergenos)
		self.alcoholica: bool = alcoholica
		self.ml: float = ml

	def no_cobrar(self, razon: str) -> None:
		self.precio = 0


class Alimento(Producto):
	def __init__(self, nombre: str, precio: float, descripcion: str, alergenos: [str], tipoDeDieta: str, peso: float):
		super().__init__(nombre, precio, descripcion, alergenos)
		self.tipoDeDieta: str = tipoDeDieta
		self.peso: float = peso

	def no_cobrar(self, razon: str) -> None:
		self.precio = 0
