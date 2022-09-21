from abc import ABC, abstractmethod


class Auto(ABC):

	@property
	@abstractmethod
	def tipo(self):
		pass

	@abstractmethod
	def acelerar(self):
		pass

	@abstractmethod
	def frenar(self):
		pass

	@abstractmethod
	def encender(self):
		pass

	@abstractmethod
	def moverVolante(self, direccion):
		pass


class Tesla(Auto):

	def __init__(self):
		self.name = 'Tesla Model S Plaid'
		self.encendido = False
		self.frenando = False
		self.acelerando = False
		self._tipo = "Electrico"


	def tipo(self):
		return self._tipo

	def acelerar(self):
		if (self.encendido):
			print("El " + self.name + " esta acelerando")
			self.acelerando = True
		else:
			print("Por favor pongo la tarjeta o su celular en la consola, presione el pedal de freno\n"
			      + " Y seleccione una velocidad para encender su " + self.name)

	def frenar(self):
		if (self.acelerando and self.encendido):
			print("El " + self.name + " freno completamente")
		elif (self.encendido and not self.acelerando):
			print("Pedal de freno presionado, puede apagar su " + self.name)
			self.frenando = True
		else:
			print("Pedal de freno presionado, puede encender su " + self.name)
			self.frenando = True

	def encender(self):
		if (self.frenando):
			print("Tarjeta detectada, su " + self.name + " ha encendido")
			self.frenando = False
			self.encendido = True
		else:
			print("Presione el pedal de freno para encender su " + self.name)

	def moverVolante(self, direccion):
		print("Ha girado el volante a la " + direccion)


class SubaruImprezaWRXSTI(Auto):

	def __init__(self):
		self.name = 'Subaru impreza WRX STI'
		self.encendido = False
		self.frenando = False
		self.acelerando = False
		self._tipo = "Combustion"

	def tipo(self):
		return self._tipo

	def acelerar(self):
		if (self.encendido):
			print("El " + self.name + " esta acelerando")
			self.acelerando = True
		else:
			print("Por favor inserte la llave y presione el pedal de freno\n"
			      + "para encender su " + self.name)

	def frenar(self):
		if (self.acelerando and self.encendido):
			print("El " + self.name + " freno completamente")
		elif (self.encendido and not self.acelerando):
			print("Pedal de freno presionado, puede apagar su " + self.name)
			self.frenando = True
		else:
			print("Pedal de freno presionado, puede encender su " + self.name)
			self.frenando = True

	def encender(self):
		if (self.frenando):
			print("llave insertada, dando marcha al motor... \n Su " + self.name + " ha encendido")
			self.frenando = False
			self.encendido =True
		else:
			print("Presione el pedal de freno para encender su " + self.name)

	def moverVolante(self, direccion):
		print("Ha girado el volante a la " + direccion)


class conductor:
	def __init__(self, auto: Auto):
		self._auto: Auto = auto
		self.iniciado = False

	def iniciarcoche(self):
		if (self._auto.tipo() == "Electrico"):
			self._auto.frenar()
			self._auto.encender()
			self.iniciado = True
		else:
			self._auto.frenar()
			self._auto.encender()
			print("Se calentara el auto antes de usarlo, para que suba la presion del aceite")
			self.iniciado = True

	def derrapar(self,direccion):
		if(self.iniciado):
			self._auto.acelerar()
			if(direccion == "Izquierda"):
				self._auto.moverVolante("derecha")
				print("Freno ligeramente y ahora")
				self._auto.moverVolante("izquierda")
				self._auto.acelerar()
				self._auto.moverVolante("derecha")
				print("Ha derrapado exitosamente, presiona el freno y...")
				self._auto.frenar()
			else:
				self._auto.moverVolante("izquierda")
				print("Freno ligeramente y ahora")
				self._auto.moverVolante("derecha")
				self._auto.acelerar()
				self._auto.moverVolante("izquierda")
				print("Ha derrapado exitosamente, presiona el freno y...")
				self._auto.frenar()

		else:
			print("Primero debe encender el auto")

if __name__ == '__main__':
	conductor_subie = conductor(SubaruImprezaWRXSTI())
	print("Se ha subido al Subaru Impreza WRX STI")
	conductor_subie.iniciarcoche()
	conductor_subie.derrapar("Izquierda")

	print()

	conductor_Tesla = conductor(Tesla())
	print("Se ha subido al Tesla Model S Plaid")
	conductor_Tesla.derrapar("Derecha")
	conductor_Tesla.iniciarcoche()
	conductor_Tesla.derrapar("Derecha")