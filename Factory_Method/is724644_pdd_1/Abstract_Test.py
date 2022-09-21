from abc import ABC, abstractmethod

class Test(ABC):
	@abstractmethod
	def is_true(self, int1,int2) -> bool:
		pass


class TestFactory(ABC):
	@abstractmethod
	def add_test(self,micro_type) -> Test:
		pass