"""
Authors:
Carlos Andrés Hidalgo Martí
Carlos Rogelio Quirarte Vázquez
"""

from Abstract_Factory_Method.factories import FurnitureFactory, Chair, Sofa, Table


class ContemporaryChair(Chair):
	def __str__(self):
		return 'Contemporary ' + super().__str__()


class ContemporarySofa(Sofa):
	def __str__(self):
		return 'Contemporary ' + super().__str__()


class ContemporaryTable(Table):
	def __str__(self):
		return 'Contemporary ' + super().__str__()


class ContemporaryFurnitureFactory(FurnitureFactory):
	def createChair(self) -> ContemporaryChair:
		return ContemporaryChair()

	def createSofa(self) -> ContemporarySofa:
		return ContemporarySofa()

	def createTable(self) -> ContemporaryTable:
		return ContemporaryTable()


class ModernChair(Chair):
	def __str__(self):
		return 'Modern ' + super().__str__()


class ModernSofa(Sofa):
	def __str__(self):
		return 'Modern ' + super().__str__()


class ModernTable(Table):
	def __str__(self):
		return 'Modern ' + super().__str__()


class ModernFurnitureFactory(FurnitureFactory):
	def createChair(self) -> ModernChair:
		return ModernChair()

	def createSofa(self) -> ModernSofa:
		return ModernSofa()

	def createTable(self) -> ModernTable:
		return ModernTable()


class RetroChair(Chair):
	def __str__(self):
		return 'Retro ' + super().__str__()


class RetroSofa(Sofa):
	def __str__(self):
		return 'Retro ' + super().__str__()


class RetroTable(Table):
	def __str__(self):
		return 'Retro ' + super().__str__()


class RetroFurnitureFactory(FurnitureFactory):
	def createChair(self) -> RetroChair:
		return RetroChair()

	def createSofa(self) -> RetroSofa:
		return RetroSofa()

	def createTable(self) -> RetroTable:
		return RetroTable()


if __name__ == '__main__':
	print(str(RetroFurnitureFactory().createTable()))
	print(str(ModernFurnitureFactory().createTable()))
