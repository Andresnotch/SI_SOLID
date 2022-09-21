from abc import ABC, abstractmethod


class Weapon(ABC):
	@abstractmethod
	def hit(self) -> int:
		pass

	@abstractmethod
	def use_weapon(self):
		pass

	@abstractmethod
	def wpn_break(self) -> None:
		pass

	@abstractmethod
	def is_broken(self) -> bool:
		pass


class Sword(Weapon):
	def __init__(self, damage: int, use: int):
		self.damage: int = damage
		self.use: int = use

	def hit(self) -> int:
		if self.is_broken():
			return 0
		self.use_weapon()
		if self.is_broken():
			self.wpn_break()
			# Weapon damages double on break!
			return self.damage * 2
		return self.damage

	def use_weapon(self):
		self.use -= 1

	def wpn_break(self) -> None:
		print('This weapon is broken!')

	def is_broken(self) -> bool:
		return self.use <= 0


class MagicWeapon(Weapon):
	_weapon: Weapon = None

	def __init__(self, weapon: Weapon, magic_damage: int) -> None:
		self._weapon = weapon
		self.magic_damage = magic_damage

	@property
	def weapon(self):
		return self._weapon

	def modify_damage(self) -> int:
		return self.magic_damage

	def hit(self) -> int:
		if self.weapon.is_broken():
			# A damaged magic weapon will damage the player!
			return self.weapon.hit() - self.modify_damage()
		return self.weapon.hit() + self.modify_damage()

	def use_weapon(self):
		self.weapon.use_weapon()

	def wpn_break(self) -> None:
		print('This weapon is broken! It will damage you if you use it!')

	def is_broken(self) -> bool:
		return self.weapon.is_broken()


class ThunderMagic(MagicWeapon):
	"""
	Thunder Magic will increase the damage by 5!
	"""
	def modify_damage(self) -> int:
		return self.magic_damage * 5


class MetalMagic(MagicWeapon):
	"""
	Metal Magic makes evey hit harder, but has lower use.
	"""
	def __init__(self, weapon: Weapon, magic_damage: int):
		super(MetalMagic, self).__init__(weapon, magic_damage)
		self._full_use = self.weapon.use

	def use_weapon(self):
		self.use -= 2

	def modify_damage(self) -> int:
		return (self._full_use - self.weapon.use) + self.magic_damage


if __name__ == '__main__':
	basic_sword = Sword(10, 3)
	print('Hit with basic sword: ' + str(basic_sword.hit()) + ' points!')
	print('Hit with basic sword: ' + str(basic_sword.hit()) + ' points!')
	print('Hit with basic sword: ' + str(basic_sword.hit()) + ' points!')
	print()
	metal_sword = MetalMagic(Sword(10, 4), 2)
	print('Hit with magic sword: ' + str(metal_sword.hit()) + ' points!')
	print('Hit with magic sword: ' + str(metal_sword.hit()) + ' points!')
	print('Hit with magic sword: ' + str(metal_sword.hit()) + ' points!')
	print('Hit with magic sword: ' + str(metal_sword.hit()) + ' points!')
