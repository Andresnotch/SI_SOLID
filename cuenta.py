from producto import Producto


class Cuenta:
	def __init__(self, productos: [Producto], total: float):
		self.productos: list = productos
		self.total: float = total

	def dividirCuenta(self, personas: int) -> None:
		cuentaDividida: float = self.total / personas
		print("Cada persona pagará " + str(cuentaDividida) + " pesos")

	def pagar(self) -> None:
		print("El total a pagar es: " + str(self.total))

	def agregarProducto(self, producto: Producto):
		self.productos.append(producto)
		self.total += producto.precio
		print("producto" + str(producto) + "agregado")

	def quitarProducto(self, producto: Producto):
		if producto in self.productos:
			self.productos.remove(producto)
			self.total -= producto.precio
			print("producto " + str(producto) + " eliminado")
		else:
			print("Producto: " + str(producto) + " no existe")
