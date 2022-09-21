

class DataLogger:
	_INSTANCE = None

	def __init__(self, name: str):
		if DataLogger._INSTANCE is None:
			self.name = name
			DataLogger._INSTANCE = self

		else:
			print('There is an existing instance.')

	@classmethod
	def get_logger(cls):
		return cls._INSTANCE

	def change_logger(self, name: str):
		if DataLogger._INSTANCE is None:
			self.name = name
			DataLogger._INSTANCE = self
