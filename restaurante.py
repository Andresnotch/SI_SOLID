from menu import Menu
from mesa import Mesa

class Restaurante:
	def __init__(self, nombre: str, direccion: str, menu: Menu, mesas: [Mesa]) -> None:
		self.nombre = nombre
		self.direccion = direccion
		self.menu: Menu = menu
		self.mesas: [Mesa] = mesas

	def abrir(self) -> bool:
		print('restaurante abierto')
		return True

	def cerrar(self) -> bool:
		for m in self.mesas:
			m.cliente = None
		print('restaurante cerrado')
		return True