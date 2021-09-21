from abc import ABC
from datetime import datetime as dt

from cuenta import Cuenta
import restaurante as resto
from copy import deepcopy


class Persona(ABC):
	def __init__(self, nombre: str, edad: int):
		self.nombre: str = nombre
		self.edad: int = edad


class Cliente(Persona):
	def __init__(self, nombre: str, edad: int, tipo_consumo: str):
		super().__init__(nombre, edad)
		self.tipo_consumo: str = tipo_consumo
		self.cuenta: Cuenta or None = None


class Mesero(Persona):
	def __init__(self, nombre: str, edad: int, rfc: str, direccion: str, fecha_nacimiento: dt, restaurante: resto.Restaurante):
		super().__init__(nombre, edad)
		self.rfc: str = rfc
		self.direccion: str = direccion
		self.fecha_nacimiento: dt = fecha_nacimiento
		self.restaurante: resto.Restaurante = restaurante

	def abrirCuenta(self, m: resto.Mesa, cliente: Cliente) -> bool:
		if m.cliente:
			print("Esta mesa tiene una cuenta abierta")
			return False
		m.cliente = cliente
		cliente.cuenta = self.tomarOrden()
		return True

	def tomarOrden(self) -> Cuenta:
		cuenta = Cuenta([], 0)
		entrada = ''
		while entrada is not 'EXIT':
			entrada = input('Ingresa el nombre del producto a agregar: ')
			if entrada in self.restaurante.menu.productos:
				cuenta.agregarProducto(deepcopy(self.restaurante.menu.productos[entrada]))
				print("Producto agregado")
			elif entrada == 'EXIT':
				break
			else:
				print("El producto no existe")
		return cuenta

	def cobrarCuenta(self, m: resto.Mesa) -> bool:
		if m.cliente and m.cliente.cuenta:
			m.cliente.cuenta.pagar()
		return True

