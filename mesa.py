


class Mesa:
	def __init__(self, numMesa: int, cantidadPersona: int) -> None:
		"""
		Class Mesa
		:param numMesa:
		:param cantidadPersona:
		"""
		self.numMesa: int = numMesa
		self.cantidadPersona: int = cantidadPersona
		self.cliente = None

	def agregarCliente(self, cliente) -> bool:
		if not self.cliente:
			self.cliente = cliente
			print("Cliente agregado")
		else:
			print("Aún existe un cliente en esta mesa")
			return False