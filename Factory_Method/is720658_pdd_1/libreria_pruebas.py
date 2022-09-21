from abc import ABC, abstractmethod

class Test(ABC):
	@abstractmethod
	def assert_true(self, *args, **kwargs) -> bool:
		pass

	@abstractmethod
	def assert_equal(self, *args, **kwargs) -> bool:
		pass


class TestFactory(ABC):
	@abstractmethod
	def create_test(self, *args, **kwargs) -> Test:
		pass

