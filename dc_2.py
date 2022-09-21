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

def tiene_espacio():
	return len(self.items) < self._max_items

def recoger(self, nombre: str, cantidad: int) -> None:
	'''
	Ingresa articulos en la mochila
	'''
	for i in range(cantidad):
		if self.tiene_espacio():
			self.items.append(nombre)
		else:
			raise ValueError(f'Se alcanzo la capacidad máxima de tu mochila, {self._max_items} en total')