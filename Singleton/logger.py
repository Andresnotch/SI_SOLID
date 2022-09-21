class Bucket:
	INSTANCES = {}


def singleton(clase):
	def retrieve_instance(*args, **kwargs):
		if clase not in Bucket.INSTANCES:
			Bucket.INSTANCES[clase] = clase(*args, **kwargs)
		return Bucket.INSTANCES[clase]

	return retrieve_instance


@singleton
class data_logger:
	def __init__(self, archivo: str):
		self.archivo = archivo

	def __str__(self):
		return self.archivo

	def delete_logger(self):
		print(Bucket.INSTANCES)
		print(self.__class__)
		del Bucket.INSTANCES[self.__class__]