"""
Equipo:
Carlos Andrés Hidalgo Martí
Carlos Rogelio Quirarte Vázquez

Cambios: línea 137-205
"""

from __future__ import annotations
from abc import ABC
from time import sleep


class Personaje:
	def __init__(self, nombre: str):
		self.nombre = nombre
		self.mochilas = None
		self.vida = 100

	def comer(self, alimento: Alimento):
		'''
		El personaje consume los alimentos para ganar vida
		'''
		self.vida += alimento.aporte_vida


class Alimento(ABC):
	pass


# ---------------------------------------------------------------------------------------------
# * RETO
# ---------------------------------------------------------------------------------------------
# Objetivo: Agrega el metodo "demoler" con un "assert" el cual suponga que se tiene al menos
# 1 de durabilidad antes de ejecutar la acción.
#

class Herramienta:
	def __init__(self, durabilidad: int, daño):
		self.durabilidad = durabilidad
		self.daño = daño

class Martillo(Herramienta):
	'''
	El martillo es una herramienta que se puede utilizar para demoler estructuras.
	El martillo requiere 3 rocas, 3 ramitas y 2 cuerdas para que se pueda fabricar.
	La durabilidad es el número de usos.
	'''

	def __init__(self, durabilidad: int = 75, daño=17):
		super().__init__(durabilidad, daño)

	def __str__(self) -> str:
		return 'Martillo'


class Hacha(Herramienta):
	'''
	El hacha es una herramienta que se puede utilizar para talar árboles. Se puede crear
	al comienzo del juego con 1 ramita y 1 pedernal.
	'''

	def __init__(self, durabilidad: int = 100, daño=27):
		super().__init__(durabilidad, daño)

	def __str__(self) -> str:
		return 'Hacha normal'


class HachaLujo(Herramienta):
	'''
	El Hacha de lujo es una versión del Hacha normal que tiene cuatro veces más durabilidad
	y requiere pepitas de oro en lugar de pedernal. Se necesitan 4 ramitas y 2 pepitas de oro
	para fabricar.
	'''

	def __init__(self, durabilidad: int = 400, daño=27):
		super().__init__(durabilidad, daño)

	def __str__(self) -> str:
		return 'Hacha de Lujo'


class Mochila:
	'''
	La mochila tiene la capacidad de guardar un número limitado de artículos
	'''

	def __init__(self, nombre, max_items: int = 5):
		self.nombre = nombre
		self._max_items = max_items
		self.items = []

	# ---------------------------------------------------------------------------------------------
	# * RETO
	# ---------------------------------------------------------------------------------------------
	# Objetivo: recoger colecciones de objetos a la mochila. Los objetos se pueden agrupar. No hace
	# falta conocer el numero de objetos. Actualmente solo es posible incluir los nombres de los
	# articulos.
	#
	# Por ejemplo:
	#  - palitos x 5
	#  - rocas x 4
	#
	def recoger(self, nombre: str) -> None:
		'''
		Ingresa articulos en la mochila
		'''
		if len(self.items) < self._max_items:
			self.items.append(nombre)
		else:
			raise ValueError(f'Se alcanzo la capacidad máxima de tu mochila, {self._max_items} en total')

	# ---------------------------------------------------------------------------------------------
	# * RETO
	# ---------------------------------------------------------------------------------------------
	# Objetivo: Poder guardar herramientas dentro de la mochila, pero una version de la herramienta
	# a la vez. Por ejemplo, no se puede tener un Hacha normal y un Hacha de lujo en la misma mochila.
	#
	# ---------------------------------------------------------------------------------------------
	# * RETO
	# ---------------------------------------------------------------------------------------------
	# Objetivo: Consolidad las expresiones en las condicionales
	#
	# ---------------------------------------------------------------------------------------------
	# * RETO
	# ---------------------------------------------------------------------------------------------
	# La lógica de las condicionales parece algo compleja
	# Objetivo: Crear métodos para el manero de las expresiones en las condicionales
	#
	# ---------------------------------------------------------------------------------------------
	# * RETO
	# ---------------------------------------------------------------------------------------------
	# Existe código que se repite constantemente
	# Objetivo: Evitar duplicidad de código en cada una de las ramas de las condicionales
	#
	"""
	Edición 1:
		Separamos las recetas en una estructura de diccionario, para que las referencias a las recetas
		no sean redundantes a través del código. Otra ventaja que ofrece este cambio es que se pueden
		alterar los materiales y resultados de la receta en un solo lugar, y se verán reflejados en
		todas partes.
	"""
	crafts = {
		'martillo': ([('ramita', 3), ('roca', 3), ('cuerda', 2)], Martillo),
		'hacha': ([('ramita', 1), ('pedernal', 1)], Hacha),
		'hacha_lujo': ([('ramita', 4), ('pepita oro', 2)], HachaLujo)
	}

	groups: [(Herramienta,)] = [
		(Hacha, HachaLujo),
		(Martillo)
	]

	"""
	Cambio 3:
		Se aplicó la técnica de extracción de método. Con esto se simplifica el código, y permite
		la extensión de la funcionalidad para otros casos, como lo podría ser un modo creativo.
	"""
	def tiene_suficiente_material(self, herramienta):
		requerimiento, resultado = self.crafts[herramienta]
		for item, quantity in requerimiento.items():
			if self.items.count(item) < quantity:
				print("No tienes suficientes materiales")
				return False
		return True

	"""
	Cambio 4:
		Se aplicó nuevamente la técnica de extracción de método.
	"""
	def herramienta_en_grupo(self, herramienta: Herramienta):
		for g in self.groups:
			if herramienta in g and any(self.items.count(item) > 0 for item in g):
				print("Ya tienes una herramienta de este tipo")
				return True
		return False

	def fabricar(self, herramienta) -> bool:
		'''
		Fabricar herramientas a través de los artículos en tu inventario. Regresa True si se pudo
		fabricar la herramienta
		'''
		"""
		Cambio 2:
			Se arregló la lógica booleana que evitaba que se accediera al resto del código. Esto debería
			considerarse como el arreglo de un bug, ya que provocaba un error en la lógica.
		"""
		if herramienta not in self.crafts:
			return False

		requerimiento, resultado = self.crafts[herramienta]

		if not self.tiene_suficiente_material(herramienta):
			return False

		if self.herramienta_en_grupo(resultado):
			return False

		for item, quantity in requerimiento.items():
			for i in range(quantity):
				self.items.remove(item)

		self.recoger(str(resultado()))
		return True

	# ---------------------------------------------------------------------------------------------
	# * RETO
	# ---------------------------------------------------------------------------------------------
	# Objetivo: Reemplazar los números con variables de clase.
	# Se puede aplicar a todo el código, no solamente a este dunder method.
	#
	def __str__(self) -> str:
		list_items = '\n'.join(self.items)
		return f'''{self.nombre:^50}\n{"=" * 50}\n{list_items}'''


class Fogata:
	'''
	Una fogata es la clave para la supervivencia básica en el mundo. Aporta luz, calor y permite
	cocinar los alimentos. Requiere 3 césped y 2 troncos para que se pueda fabricar.
	Los personajes no pueden consumir alimentos crudos.
	'''

	def __init__(self):
		# Agrega la validación necesaria antes de fabricar una fogata
		pass

	# ---------------------------------------------------------------------------------------------
	# * RETO
	# ---------------------------------------------------------------------------------------------
	# Los alimentos tienen diferentes tiempos de cocción. No queremos tener condicionales, entonces
	# usamos refactorización. Se ha comentado parte del código original.
	# Objetivo: Usar polimorfismo para obtener el tiempo de cocción y simplificar el método. Trata de
	# usar una interface con al menos los atributos: name, tiempo_coccion, cocido
	def cocinar(self, alimento: object) -> None:
		'''
		Permite cocinar un alimento crudo en la fogata. Regresa el mismo alimento pero cocinado.
		'''
		# if alimento == 'cordero' and alimento.cocido == False:
		#     sleep(2)
		# elif alimento == 'beef' and alimento.cocido == False:
		#     sleep(5)

		if alimento.cocido == False:
			sleep(alimento.tiempo_coccion)
			alimento.cocido = True


if __name__ == '__main__':
	# Personajes
	wilson = Personaje('Wilson')

	# Items
	backpack = Mochila('Morral chico', 10)
	backpack.recoger('ramita')
	backpack.recoger('ramita')
	backpack.recoger('ramita')
	backpack.recoger('roca')
	backpack.recoger('roca')
	backpack.recoger('roca')
	backpack.recoger('cuerda')
	backpack.recoger('cuerda')
	backpack.recoger('cuerda')

	# Fabrica
	backpack.fabricar('martillo')
	backpack.fabricar('hacha')
	backpack.fabricar('hacha_lujo')

	# ---------------------------------------------------------------------------------------------
	# * RETO
	# ---------------------------------------------------------------------------------------------
	# Objetivo: Agregar al menos dos alimentos que se puedan cocinar en la fogata. Crear una fogata,
	# Cocinar los alimentos en la fogata y comer los alimentos.
	#

	# Listamos los articulos en nuestra mochila
	print(backpack)
