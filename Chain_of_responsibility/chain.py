import random
from abc import ABC, abstractmethod


# -----------------------------------------------------------------------------
# 1.- Interface
# -----------------------------------------------------------------------------
class Manejador(ABC):
	@abstractmethod
	def siguiente(self, manejador):
		pass

	@abstractmethod
	def manejador(self, peticion):
		pass


# -----------------------------------------------------------------------------
# 2.- Manejador abstracto base
# -----------------------------------------------------------------------------
class ManejadorBase(Manejador):
	siguiente_manejador: Manejador = None

	def siguiente(self, manejador: Manejador) -> Manejador:
		''' Define al siguiente manejador '''
		self.siguiente_manejador = manejador
		return manejador

	def manejador(self, peticion: dict) -> str:
		''' Maneja la continuidad de las pruebas '''
		if self.siguiente_manejador:
			return self.siguiente_manejador.manejador(peticion)
		return None


# -----------------------------------------------------------------------------
# 3.- Manejadores en concreto
# -----------------------------------------------------------------------------
class Tarea1(ManejadorBase):
	def manejador(self, peticion: dict) -> str:
		print('-I- Revisando el tipo de prueba')
		if peticion["tipo"] == 'concurrencia':
			print('-I- Montando ambiente para concurrencia')
		elif peticion["tipo"] == 'stress':
			print('-I- Montando ambiente para stress')
		else:
			print(f'-E- No se ha encontrado un ambiente para {peticion["tipo"]}')
			return None
		return super().manejador(peticion)


class Tarea2(ManejadorBase):
	def manejador(self, peticion: dict) -> str:
		print(f'-I- Iniciando temporizador de {peticion["duracion"]} segundos')
		if peticion["duracion"] > 300:
			print(f'-E- El temporizador supera el tiempo maximo')
			return None
		return super().manejador(peticion)


class Tarea3(ManejadorBase):
	def manejador(self, peticion: dict) -> str:
		print(f'-I- Ejecutando prueba con benchmark {peticion["benchmark"]}')
		return super().manejador(peticion)


class Tarea4(ManejadorBase):
	def manejador(self, peticion: dict) -> str:
		print(f'-I- Obteniendo datos resultantes')
		print(f'-I- Añadiendo datos resultantes al reporte')
		peticion['datos_resultantes'] = {
			'exito': True if random.randint(0, 1) else False,
			'tiempo total': random.randint(1, 10)
		}
		return super().manejador(peticion)


class Tarea5(ManejadorBase):
	def manejador(self, peticion: dict) -> str:
		print(f'-I- Valorando datos resultantes')
		if peticion['datos_resultantes']['exito']:
			print(f'-I- ' + str(peticion['datos_resultantes']))
		else:
			print(f'-E- No se pudo completar la prueba: ' + str(peticion['datos_resultantes']))
		return super().manejador(peticion)


# -----------------------------------------------------------------------------
# 4.- Cliente
# -----------------------------------------------------------------------------
# Empresa de pruebas
# -----------------------------------------------------------------------------
if __name__ == "__main__":
	# Definimos las especificaciones de nuestra prueba
	especificaciones = {
		'tipo': 'concurrencia',
		'duracion': 5,
		'benchmark': 'bench1'
	}

	# Definimos los pasos para esta prueba en particular
	prueba = Tarea1()
	prueba.siguiente(Tarea2()).siguiente(Tarea3()).siguiente(Tarea4()).siguiente(Tarea5())

	# Ejecutamos la prueba
	prueba.manejador(especificaciones)
