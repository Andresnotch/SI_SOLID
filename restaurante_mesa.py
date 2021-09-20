from menu import Menu
from persona import Cliente


class Mesa:
	def __init__(self, numMesa: int, cantidadPersona: int) -> None:
		"""
		Class Mesa
		:param numMesa:
		:param cantidadPersona:
		"""
		self.numMesa: int = numMesa
		self.cantidadPersona: int = cantidadPersona
		self.cliente: Cliente or None = None

	def agregarCliente(self, cliente: Cliente) -> bool:
		if not self.cliente:
			self.cliente = cliente
			print("Cliente agregado")
		else:
			print("Aún existe un cliente en esta mesa")
			return False

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