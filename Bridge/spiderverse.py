from abc import ABC, abstractmethod


class Variant(ABC):

	@property
	@abstractmethod
	def name(self):
		pass

	@property
	@abstractmethod
	def supername(self):
		pass

	@abstractmethod
	def attackUp(self):
		pass

	@abstractmethod
	def attackDown(self):
		pass

	@abstractmethod
	def specialUp(self):
		pass

	@abstractmethod
	def specialDown(self):
		pass

	@abstractmethod
	def gadgetLight(self):
		pass

	@abstractmethod
	def gadgetHeavy(self):
		pass


class Earth616(Variant):

	def __init__(self):
		self._name = 'Peter Parker'
		self._supername = 'Spider-Man'

	@property
	def name(self):
		return self._name

	@property
	def supername(self):
		return self._supername

	def attackUp(self):
		print(f'{self.supername} ({self.name}) has landed an Up-Attack!')

	def attackDown(self):
		print(f'{self.supername} ({self.name}) has landed an Down-Attack!')

	def specialUp(self):
		print(f'{self.supername} ({self.name}) has landed an Up-Special!')

	def specialDown(self):
		print(f'{self.supername} ({self.name}) has landed a Down-Special!')

	def gadgetLight(self):
		print(f'{self.supername} ({self.name}) has used a Light Gadget!')

	def gadgetHeavy(self):
		print(f'{self.supername} ({self.name}) has used a Heavy Gadget!')


class Earth1610(Variant):

	def __init__(self):
		self._name = 'Miles Morles'
		self._supername = 'Spider-Man'

	@property
	def name(self):
		return self._name

	@property
	def supername(self):
		return self._supername

	def attackUp(self):
		print(f'{self.supername} ({self.name}) has landed an Up-Attack!')

	def attackDown(self):
		print(f'{self.supername} ({self.name}) has landed an Down-Attack!')

	def specialUp(self):
		print(f'{self.supername} ({self.name}) has landed an Up-Special!')

	def specialDown(self):
		print(f'{self.supername} ({self.name}) has landed an Down-Special!')

	def gadgetLight(self):
		print(f'{self.supername} ({self.name}) has used a Light Gadget!')

	def gadgetHeavy(self):
		print(f'{self.supername} ({self.name}) has used a Heavy Gadget!')


class SpiderMan:
	def __init__(self, variant):
		self._variant: Variant = variant
		self._attackState = {
			'attack': 0,
			'special': 0,
			'gadget': 0
		}

	@property
	def name(self):
		return self._variant.name

	@property
	def supername(self):
		return self._variant.supername

	def attack(self):
		if self._attackState['attack'] == 0:
			self._variant.attackUp()
			self._attackState['attack'] = 1
		else:
			self._variant.attackDown()
			self._attackState['attack'] = 0

	def special(self):
		if self._attackState['special'] == 0:
			self._variant.specialUp()
			self._attackState['special'] = 1
		else:
			self._variant.specialDown()
			self._attackState['special'] = 0

	def gadget(self):
		if self._attackState['gadget'] == 0:
			self._variant.gadgetLight()
			self._attackState['gadget'] = 1
		else:
			self._variant.gadgetHeavy()
			self._attackState['gadget'] = 0