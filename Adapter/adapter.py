from abc import ABC


# Esta implementación utiliza el principio de composición de objetos: el
# adaptador implementa la interfaz de un objeto y envuelve el otro

# Interface principal en funcionamiento
class Entero(ABC):
	@classmethod
	def sumar(self, *numeros) -> str:
		""" Suma n cantidad de números enteros """
		suma = 0
		for numero in numeros:
			suma += numero
		return str(suma)


# Clase que queremos adaptar sin romper el código actual
class Hexadecimal:
	def adicion(self, hex_1: str, hex_2: str) -> str:
		""" Suma dos números binarios representados como string """
		return '{0:x}'.format(int(hex_1, 16) + int(hex_2, 16))


# Adapter
class HexadecimalToEntero(Entero):
	def __init__(self, hex: Hexadecimal) -> None:
		self.hex = hex

	def sumar(self, *numeros) -> str:
		suma = '0'
		for numero in numeros:
			suma = self.hex.adicion(suma, numero)
		return str(suma)


if __name__ == "__main__":
	print(f'La suma decimal 9 + 1 + 3 = {Entero().sumar(9, 1, 3)}')
	print(f'La suma hexadecimal 0xb + 0x1 = {HexadecimalToEntero(Hexadecimal()).sumar("b", "1")}')
	print('{}'.format(hex(int('D', 16) + int('1', 16))))
