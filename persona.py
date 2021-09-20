from abc import ABC, abstractclassmethod
from datetime import datetime as dt

from cuenta import Cuenta
from menu import Menu
from producto import Producto
from restaurante_mesa import Mesa, Restaurante
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
	def __init__(self,nombre: str, edad: int, rfc: str, direccion: str, fecha_nacimiento: dt, restaurante: Restaurante):
		super().__init__(nombre, edad)
		self.rfc: str = rfc
		self.direccion: str = direccion
		self.fecha_nacimiento: dt = fecha_nacimiento
		self.restaurante: Restaurante = restaurante

	def abrirCuenta(self, mesa: Mesa, cliente: Cliente) -> bool:
		if mesa.cliente:
			print("Esta mesa tiene una cuenta abierta")
			return False
		mesa.cliente = cliente
		cliente.cuenta = self.tomarOrden()
		return True

	def tomarOrden(self) -> Cuenta:
		cuenta = Cuenta([], 0)
		entrada = ''
		while entrada is not 'EXIT':
			entrada = input('Ingresa el nombre del producto a agregar: ')
			if entrada in self.restaurante.menu:
				cuenta.agregarProducto(deepcopy(self.restaurante.menu.productos[entrada]))
				print("Producto agregado")
			else:
				print("El producto no existe")
		return cuenta

	def cobrarCuenta(self, mesa: Mesa) -> bool:
		if mesa.cliente and mesa.cliente.cuenta:
			mesa.cliente.cuenta.pagar()
		return True

