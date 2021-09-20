from producto import Producto


class Menu:
	def __init__(self, nombre: str, productos: dict):
		self.nombre: str = nombre
		self.productos: dict = productos

	def agregarProducto(self, producto: Producto) -> bool:
		if producto.nombre in self.productos:
			print("El producto: " + str(producto) + " ya existe")
			return False
		else:
			self.productos[producto.nombre] = producto
			print("producto" + str(producto) + "agregado")
			return True

	def quitarProducto(self, producto: Producto) -> bool:
		if producto.nombre in self.productos:
			del self.productos[producto.nombre]
			print("producto " + str(producto) + " eliminado")
			return True
		else:
			print("El producto: " + str(producto) + " no existe")
			return False
